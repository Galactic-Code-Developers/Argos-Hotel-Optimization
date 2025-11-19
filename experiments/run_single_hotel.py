"""Run a simple single-hotel ARGOS demonstration.

This script is illustrative and uses simplified objectives and gradients.
"""

import numpy as np

from argos.hotel_env import HotelEnvironment
from argos.lco import LexicographicTier, LexicographicTierStructure
from argos.cag import CAGFilter
from argos.argos_core import ARGOSOptimizer

def revenue_obj(x: np.ndarray) -> float:
    # Simple revenue proxy: occupancy * (50 + 100 * price)
    return - (x[0] * (50 + 100 * x[3]))

def revenue_grad(x: np.ndarray) -> np.ndarray:
    # d/dx occupancy: -(50 + 100 * price), d/dx price: -(100 * occupancy)
    g = np.zeros_like(x)
    g[0] = - (50 + 100 * x[3])
    g[3] = - (100 * x[0])
    return g

def newton_step(x: np.ndarray) -> np.ndarray:
    # Simple diagonal approximate Hessian
    H_inv = np.array([1e-3, 1.0, 1.0, 1e-3])
    return -H_inv * revenue_grad(x)

def contour_step(x: np.ndarray) -> np.ndarray:
    g = revenue_grad(x)
    norm = np.linalg.norm(g) + 1e-8
    return -0.1 * g / norm

def main():
    env = HotelEnvironment()
    x = env.reset()

    tier1 = LexicographicTier(
        name="Feasibility",
        objective=lambda x: 0.0,
        constraints=[lambda x: max(0.0, x[0] - 1.0)],  # occupancy <= 1.0
    )
    tiers = LexicographicTierStructure([tier1])

    cag = CAGFilter(newton_step_fn=newton_step, contour_step_fn=contour_step)
    argos = ARGOSOptimizer(tiers=tiers, cag=cag, step_size=0.05, highest_tier=1)

    for t in range(100):
        x = argos.step(x, revenue_grad)
        x, metrics = env.step(x)
        if t % 10 == 0:
            print(f"Epoch {t}: {metrics}")

if __name__ == "__main__":
    main()
