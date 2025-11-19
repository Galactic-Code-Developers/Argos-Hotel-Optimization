from dataclasses import dataclass
from typing import Callable
import numpy as np

from .lco import LexicographicTierStructure
from .cag import CAGFilter

@dataclass
class ARGOSOptimizer:
    tiers: LexicographicTierStructure
    cag: CAGFilter
    step_size: float = 0.05
    highest_tier: int = 4  # up to which tier we enforce feasibility

    def step(
        self,
        x: np.ndarray,
        revenue_grad: Callable[[np.ndarray], np.ndarray],
    ) -> np.ndarray:
        """One ARGOS update step.

        - Compute CAG direction for the revenue objective (Tier 4).
        - Apply step inside feasible region defined by higher tiers.
        """
        q = self.cag.compute_direction(x, revenue_grad)
        x_new = x - self.step_size * q
        # Project onto highest-tier feasible set
        x_proj = self.tiers.project(x_new, self.highest_tier - 1)
        return x_proj
