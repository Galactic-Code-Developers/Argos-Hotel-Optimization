# Usage Guide

- `experiments/run_single_hotel.py`: minimal single-hotel ARGOS demo.
- `experiments/run_multi_unit.py`: multi-property ARGOS run.
- `experiments/run_ablation.py`: Newton-only vs CAG-only vs ARGOS comparison.

The `src/argos` package contains all core components:
- `lco.py`: tier structure and feasibility projection.
- `cag.py`: componentwise approximated gradient filter.
- `argos_core.py`: unified ARGOS optimizer.
- `hotel_env.py`: simplified hotel environment.
- `multiunit.py`: multi-unit extensions.
- `qubo.py`: QUBO helper stubs.


## Colab/Notebook Usage

- `notebooks/ARGOS_Single_Hotel_Demo.ipynb`
- `notebooks/ARGOS_Multi_Unit_Demo.ipynb`
- `notebooks/ARGOS_Ablation_Study.ipynb`
