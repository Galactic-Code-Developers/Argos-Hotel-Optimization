# ARGOS Hotel Optimization Framework

This repository contains reference code, data, and experiment scripts for the paper:

The repository is organized for easy extension and reproduction of the main experimental results.
# **ARGOS: Adaptive Recursive Gradient Optimization System for Hierarchical Decision-Making**

ARGOS is a research framework that integrates:

- **Lexicographic Constraint Optimization (LCO)** – strict priority tiers  
- **Componentwise Approximated Gradient (CAG)** – selective Newton / contour filtering

The code implements:
- Lexicographic Constraint Optimization (LCO)
- Componentwise Approximated Gradient (CAG)
- The unified ARGOS operator (LCO + CAG)
- Dynamic hotel management simulation (single-property and multi-property)
- QUBO formulation helpers
- Ablation studies and hyperparameter sensitivity utilities

to produce a **stable, dynamic, and lexicographically safe** optimization engine for
hierarchical decision-making.

The initial application domain is **hotel and multi-property management**:
occupancy control, staffing, fatigue, and revenue optimization under hard service
and regulatory constraints. The framework is designed, however, to extend to
healthcare, logistics, and quantum / QUBO-based optimization.

This repository contains:

- A **Python implementation** of ARGOS (LCO + CAG)  
- A **simulated hotel environment** (single-property and multi-unit)  
- **Ablation experiments** (Newton-only vs CAG-only vs full ARGOS)  
- **Colab-ready notebooks** for reproducing the paper’s results  

---

## 1. Repository Structure

```text
argos_hotel_optimization/
├── src/
│   └── argos/
│       ├── __init__.py
│       ├── lco.py           # Lexicographic tier definitions & projections
│       ├── cag.py           # Componentwise Approximated Gradient filter
│       ├── argos_core.py    # Unified ARGOS optimizer (LCO + CAG)
│       ├── hotel_env.py     # Single-unit hotel CMDP-style environment
│       ├── multiunit.py     # Multi-property wrapper around hotel_env + ARGOS
│       └── qubo.py          # QUBO helper stubs / placeholders
│
├── experiments/
│   ├── run_single_hotel.py  # Main single-hotel experiment script
│   ├── run_multi_unit.py    # Multi-unit experiment script
│   └── run_ablation.py      # Newton-only vs CAG-only vs ARGOS comparison
│
├── notebooks/
│   ├── ARGOS_Single_Hotel_Demo.ipynb
│   ├── ARGOS_Multi_Unit_Demo.ipynb
│   └── ARGOS_Ablation_Study.ipynb
│
├── data/
│   ├── synthetic_single_hotel.csv  # Example state / metric traces
│   └── synthetic_multi_hotel.csv   # Example multi-unit traces
│
├── docs/
│   ├── INSTALL.md
│   └── USAGE.md
│
├── README.md
├── requirements.txt
└── LICENSE
