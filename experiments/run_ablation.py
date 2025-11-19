"""Skeleton script for ablation: Newton-only vs CAG-only vs ARGOS.

The user can extend this script to reproduce the full ablation tables from
the paper. Here we provide a minimal, illustrative structure.
"""

import numpy as np

from argos.hotel_env import HotelEnvironment
from argos.lco import LexicographicTier, LexicographicTierStructure
from argos.cag import CAGFilter
from argos.argos_core import ARGOSOptimizer

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

def run_newton_only():
    env = HotelEnvironment(seed=200)
    x = env.reset()
    for t in range(100):
        x = x - 0.05 * newton_step(x)
        x, metrics = env.step(x)
    return metrics

def run_cag_only():
    env = HotelEnvironment(seed=200)
    x = env.reset()
    cag = CAGFilter(newton_step_fn=newton_step, contour_step_fn=contour_step)
    for t in range(100):
        d = cag.compute_direction(x, revenue_grad)
        x = x - 0.05 * d
        x, metrics = env.step(x)
    return metrics

def run_argos():
    env = HotelEnvironment(seed=200)
    x = env.reset()
    tier1 = LexicographicTier(
        name="Feasibility",
        objective=lambda x: 0.0,
        constraints=[lambda x: max(0.0, x[0] - 1.0)],
    )
    tiers = LexicographicTierStructure([tier1])
    cag = CAGFilter(newton_step_fn=newton_step, contour_step_fn=contour_step)
    argos = ARGOSOptimizer(tiers=tiers, cag=cag, step_size=0.05, highest_tier=1)
    for t in range(100):
        x = argos.step(x, revenue_grad)
        x, metrics = env.step(x)
    return metrics

def main():
    m_newton = run_newton_only()
    m_cag = run_cag_only()
    m_argos = run_argos()
    print("Newton-only:", m_newton)
    print("CAG-only   :", m_cag)
    print("ARGOS      :", m_argos)

if __name__ == "__main__":
    main()
