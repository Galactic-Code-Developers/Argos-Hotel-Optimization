from dataclasses import dataclass
from typing import Dict, Any, Tuple
import numpy as np

@dataclass
class HotelEnvironment:
    n_rooms: int = 150
    base_demand: float = 0.85
    noise_scale: float = 0.1
    seed: int = 123

    def __post_init__(self):
        self.rng = np.random.default_rng(self.seed)

    def reset(self) -> np.ndarray:
        """Return an initial state vector x."""
        # Example state: [occupancy_ratio, staff_level, fatigue_index, price_level]
        return np.array([0.7, 0.9, 0.3, 0.5], dtype=float)

    def step(self, x: np.ndarray) -> Tuple[np.ndarray, Dict[str, float]]:
        """Simulate one epoch.

        This is only a schematic placeholder. The real system should
        replace this with a full CMDP transition model.
        """
        demand_shock = self.rng.normal(0.0, self.noise_scale)
        occupancy = np.clip(x[0] + 0.05 * demand_shock, 0.0, 1.2)
        staff = np.clip(x[1] - 0.01 * occupancy, 0.0, 1.0)
        fatigue = np.clip(x[2] + 0.02 * occupancy, 0.0, 1.0)
        price = np.clip(x[3], 0.0, 1.0)

        # Very simple revenue proxy
        revpar = occupancy * (50 + 100 * price)

        x_next = np.array([occupancy, staff, fatigue, price], dtype=float)
        metrics = {
            "occupancy": float(occupancy),
            "staff": float(staff),
            "fatigue": float(fatigue),
            "revpar": float(revpar),
        }
        return x_next, metrics
