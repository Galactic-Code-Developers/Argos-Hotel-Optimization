# ARGOS Hotel Optimization Framework

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17644920.svg)](https://doi.org/10.5281/zenodo.17644920)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/Galactic-Code-Developers/argos-hotel-optimization)


The repository is organized for easy extension and reproduction of the main experimental results.

### **ARGOS: Adaptive Recursive Gradient Optimization System for Hierarchical Decision-Making**

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
```
## Data Availability

All datasets used in the ARGOS experiments are fully synthetic and openly
available on Zenodo:

**Dataset DOI:**  
[https://doi.org/10.5281/zenodo.17645085](https://doi.org/10.5281/zenodo.17645085)

[![Dataset DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17645085.svg)](https://doi.org/10.5281/zenodo.17645085)

## Software Metadata

**Name:** ARGOS — Adaptive Recursive Gradient Optimization System  
**Version:** 1.0.0  
**Release Date:** 2025  
**License:** MIT  
**Repository:** https://github.com/Galactic-Code-Developers/Argos-Hotel-Optimization  
**Programming Language:** Python 3.9+  
**Primary Dependencies:** NumPy, Pandas, Matplotlib  
**Supported Platforms:** Linux, macOS, Windows  
**Continuous Integration:** GitHub Actions (optional)  
**Documentation:** Included in `docs/` and notebooks in `notebooks/`  

**Primary Purpose:**  
Stable hierarchical optimization under strict lexicographic priorities, combining  
Lexicographic Constraint Optimization (LCO) with Componentwise Approximated Gradient (CAG).  

**Research Domains:**  
- Operations Research  
- Optimization & Control  
- Reinforcement Learning (CMDP-style)  
- Hospitality Management Systems  
- Multi-agent & Multi-unit resource allocation  

**Key Features:**  
- Lexicographically safe updates (Tier-1 invariants always preserved)  
- Componentwise selective gradient filtering (CAG)  
- Integrated LCO + CAG update engine (ARGOS Core)  
- Single-unit and multi-unit hotel environment simulators  
- Ablation tools (Newton-only, CAG-only, full ARGOS)  
- Reproducible experiments via CLI and Colab notebooks  

**Intended Users:**  
Researchers, operations analysts, optimization practitioners, and academic collaborators evaluating lexicographically constrained decision systems.

## How to Cite

If you use the ARGOS framework or its associated synthetic datasets, please cite
both the **software** and the **dataset**.

---

### 🔹 Software (ARGOS)

[![Software DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17644920.svg)](https://doi.org/10.5281/zenodo.17644920)

> Valamontes, A. (2025). **ARGOS: Adaptive Recursive Gradient Optimization
> System**. Zenodo. https://doi.org/10.5281/zenodo.17644920

---

### 🔹 Dataset (ARGOS Synthetic Hotel Optimization Datasets)

[![Dataset DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17645085.svg)](https://doi.org/10.5281/zenodo.17645085)

> Valamontes, A. (2025). **ARGOS Synthetic Hotel Optimization Datasets**.
> Zenodo. https://doi.org/10.5281/zenodo.17645085

---

### 🔹 BibTeX

```bibtex
@software{Valamontes_ARGOS_2025,
  author       = {Valamontes, Antonios},
  title        = {ARGOS: Adaptive Recursive Gradient Optimization System},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17644920},
  url          = {https://doi.org/10.5281/zenodo.17644920}
}

@dataset{Valamontes_ARGOS_Datasets_2025,
  author       = {Valamontes, Antonios},
  title        = {ARGOS Synthetic Hotel Optimization Datasets},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17645085},
  url          = {https://doi.org/10.5281/zenodo.17645085}
}
