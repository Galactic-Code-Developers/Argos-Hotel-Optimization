from dataclasses import dataclass, field
from typing import Callable, List, Dict, Any
import numpy as np

@dataclass
class LexicographicTier:
    name: str
    objective: Callable[[np.ndarray], float]
    constraints: List[Callable[[np.ndarray], float]] = field(default_factory=list)

@dataclass
class LexicographicTierStructure:
    tiers: List[LexicographicTier]

    def feasible(self, x: np.ndarray, k: int) -> bool:
        """Check feasibility up to and including tier k (1-indexed)."""
        for idx in range(k):
            tier = self.tiers[idx]
            for g in tier.constraints:
                if g(x) > 0.0:
                    return False
        return True

    def project(self, x: np.ndarray, k: int) -> np.ndarray:
        """Simple feasibility projection: backtrack step until feasible.

        This is a placeholder; in a production system, replace with a more
        sophisticated projection operator.
        """
        if self.feasible(x, k):
            return x
        step = 0.5
        x_proj = x.copy()
        for _ in range(20):
            x_proj = (1 - step) * x_proj
            if self.feasible(x_proj, k):
                break
        return x_proj
