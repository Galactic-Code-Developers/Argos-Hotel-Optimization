"""Minimal placeholder for QUBO-related helpers.

This module does not implement a full QUBO stack but provides stubs and
interfaces consistent with the ARGOS QUBO formulation described in the
paper.
"""

from dataclasses import dataclass
import numpy as np

@dataclass
class QUBOModel:
    Q: np.ndarray
    q: np.ndarray
    c: float = 0.0

    def energy(self, z: np.ndarray) -> float:
        return float(z.T @ self.Q @ z + self.q.T @ z + self.c)
