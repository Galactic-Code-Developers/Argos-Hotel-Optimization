from dataclasses import dataclass
from typing import List, Dict, Any, Callable
import numpy as np

from .hotel_env import HotelEnvironment
from .argos_core import ARGOSOptimizer

@dataclass
class MultiUnitHotelSystem:
    envs: List[HotelEnvironment]
    optimizers: List[ARGOSOptimizer]

    def reset(self) -> List[np.ndarray]:
        return [env.reset() for env in self.envs]

    def step(
        self,
        states: List[np.ndarray],
        revenue_grads: List[Callable[[np.ndarray], np.ndarray]],
    ) -> Dict[str, Any]:
        new_states = []
        all_metrics: List[Dict[str, float]] = []
        for env, opt, x, g in zip(self.envs, self.optimizers, states, revenue_grads):
            x_opt = opt.step(x, g)
            x_next, metrics = env.step(x_opt)
            new_states.append(x_next)
            all_metrics.append(metrics)
        return {"states": new_states, "metrics": all_metrics}
