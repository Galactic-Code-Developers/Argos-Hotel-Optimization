"""Run a simple multi-unit ARGOS demonstration."""

import numpy as np

from argos.hotel_env import HotelEnvironment
from argos.lco import LexicographicTier, LexicographicTierStructure
from argos.cag import CAGFilter
from argos.argos_core import ARGOSOptimizer
from argos.multiunit import MultiUnitHotelSystem

def revenue_grad(x: np.ndarray) -> np.ndarray:
    g = np.zeros_like(x)
    g[0] = - (50 + 100 * x[3])
    g[3] = - (100 * x[0])
    return g

def newton_step(x: np.ndarray) -> np.ndarray:
    H_inv = np.array([1e-3, 1.0, 1.0, 1e-3])
    return -H_inv * revenue_grad(x)

def contour_step(x: np.ndarray) -> np.ndarray:
    g = revenue_grad(x)
    norm = np.linalg.norm(g) + 1e-8
    return -0.1 * g / norm

def make_argos():
    tier1 = LexicographicTier(
        name="Feasibility",
        objective=lambda x: 0.0,
        constraints=[lambda x: max(0.0, x[0] - 1.0)],
    )
    tiers = LexicographicTierStructure([tier1])
    cag = CAGFilter(newton_step_fn=newton_step, contour_step_fn=contour_step)
    return ARGOSOptimizer(tiers=tiers, cag=cag, step_size=0.05, highest_tier=1)

def main():
    envs = [HotelEnvironment(seed=100 + i) for i in range(3)]
    optims = [make_argos() for _ in envs]
    system = MultiUnitHotelSystem(envs=envs, optimizers=optims)

    states = system.reset()
    for t in range(100):
        grads = [revenue_grad for _ in states]
        out = system.step(states, grads)
        states = out["states"]
        if t % 10 == 0:
            print(f"Epoch {t}: {out['metrics']}")

if __name__ == "__main__":
    main()
