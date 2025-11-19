# ARGOS Dataset Directory

[![Dataset DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17645085.svg)](https://doi.org/10.5281/zenodo.17645085)

This directory contains all synthetic datasets used for experiments, ablation
studies, and reproducibility in the **ARGOS (Adaptive Recursive Gradient
Optimization System)** project.

All datasets are fully synthetic, generated using the ARGOS
hotel-environment simulator, and are safe for open distribution under the MIT
License.

The synthetic datasets used for all experiments are openly available on Zenodo
under the DOI: https://doi.org/10.5281/zenodo.17645085.

---

## 1. `synthetic_long_horizon.csv`
**Long-horizon 365-day simulation** of a single hotel environment.

**Columns:**
- `day` – simulation day index  
- `occupancy` – normalized occupancy rate (0–1)  
- `fatigue` – staff fatigue index  
- `staff_level` – staffing adequacy (0–1)  
- `revpar` – revenue per available room  

**Purpose:**  
Used for stability and convergence evaluations in long-horizon experiments.

---

## 2. `scenario_high_volatility.csv`
High-variance demand and noise scenario (180 days).

**Columns:**
- `day`  
- `occupancy` (high volatility)  
- `fatigue` (high volatility)  
- `revpar` (large fluctuations)

**Purpose:**  
Tests ARGOS under extreme market volatility and non-stationary dynamics.

---

## 3. `scenario_staff_shortage.csv`
Staff-shortage stress-test scenario (180 days).

**Columns:**
- `day`  
- `occupancy`  
- `fatigue` (elevated fatigue)  
- `staff_level` (reduced staffing)  
- `revpar`

**Purpose:**  
Evaluates lexicographic Tier-1 feasibility and fatigue control under constrained
resource conditions.

---

## 4. `hyperparam_sweep_results.csv`
Synthetic results from sweeping ARGOS hyperparameters.

**Columns:**
- `alpha` – step size  
- `cag_weight` – contour-filter weight  
- `avg_revpar`  
- `violations_tier1`  
- `fatigue_mean`

**Purpose:**  
Supports Appendix E (Hyperparameter Sensitivity Analysis).

---

## 5. `qubo_example_matrix.csv`
An 8×8 example QUBO matrix.

**Purpose:**  
Demonstrates the binary-optimization interface used for future QUBO/quantum
extensions.

---

## 6. `multiunit_traffic_sim.csv`
Synthetic booking-traffic simulation for **5 hotel units** over 100 days.

**Columns:**
- `day`
- `hotel_0_traffic`
- `hotel_1_traffic`
- `hotel_2_traffic`
- `hotel_3_traffic`
- `hotel_4_traffic`

**Purpose:**  
Used in multi-unit scaling experiments and Appendix D (Parallelization + Ablation).

---

## Data Origin and Ethics

- All datasets are **fully synthetic**  
- No personal or operational real hotel data is included  
- Generated only for academic reproducibility and benchmarking  

---

## How to Load the Data (Python)

```python
import pandas as pd

df = pd.read_csv("data/synthetic_long_horizon.csv")
print(df.head())
