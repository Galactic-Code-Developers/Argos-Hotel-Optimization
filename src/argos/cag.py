from dataclasses import dataclass
from typing import Callable, Tuple
import numpy as np

@dataclass
class CAGFilter:
    newton_step_fn: Callable[[np.ndarray], np.ndarray]
    contour_step_fn: Callable[[np.ndarray], np.ndarray]
    accept_threshold: float = 1e-3

    def compute_direction(
        self,
        x: np.ndarray,
        obj_grad: Callable[[np.ndarray], np.ndarray],
    ) -> np.ndarray:
        """Compute the componentwise CAG direction.

        - Use Newton step where it provides sufficient descent.
        - Otherwise fall back to contour-based correction.
        """
        g = obj_grad(x)
        d_newton = self.newton_step_fn(x)
        d_contour = self.contour_step_fn(x)

        # Predicted decrease for each component
        dec_newton = g * d_newton
        direction = np.zeros_like(x)

        for i in range(len(x)):
            if dec_newton[i] < -self.accept_threshold:
                direction[i] = d_newton[i]
            else:
                direction[i] = d_contour[i]

        return direction
