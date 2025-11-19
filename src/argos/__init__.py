"""ARGOS: Adaptive Recursive Gradient Optimization System.

This package implements:
- Lexicographic Constraint Optimization (LCO)
- Componentwise Approximated Gradient (CAG)
- The unified ARGOS operator
- Hotel management simulation environments
- Multi-unit extensions and QUBO helpers
"""

from .lco import LexicographicTierStructure
from .cag import CAGFilter
from .argos_core import ARGOSOptimizer
from .hotel_env import HotelEnvironment
from .multiunit import MultiUnitHotelSystem
