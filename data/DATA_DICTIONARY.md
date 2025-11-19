# ARGOS Dataset — Data Dictionary

This data dictionary describes the fields contained in the released CSV files.

---

## 1. `synthetic_long_horizon.csv`

| Column       | Type    | Range / Units         | Description                                                  |
|-------------|---------|------------------------|--------------------------------------------------------------|
| `day`       | int     | 0–364 (index)          | Simulation day index from the start of the horizon.         |
| `occupancy` | float   | 0.0–1.0 (fraction)     | Normalized occupancy rate (1.0 = fully occupied).           |
| `fatigue`   | float   | 0.0–1.0 (index)        | Staff fatigue index; higher values indicate more fatigue.   |
| `staff_level` | float | 0.0–1.0 (fraction)     | Normalized staffing adequacy (1.0 = fully staffed).         |
| `revpar`    | float   | currency units/room    | Revenue per available room (RevPAR), in arbitrary units.    |

---

## 2. `scenario_high_volatility.csv`

| Column       | Type    | Range / Units         | Description                                                  |
|-------------|---------|------------------------|--------------------------------------------------------------|
| `day`       | int     | 0–179 (index)          | Simulation day index.                                       |
| `occupancy` | float   | 0.0–1.0 (fraction)     | Normalized occupancy with elevated variance.                |
| `fatigue`   | float   | 0.0–1.0 (index)        | Staff fatigue index with elevated variance.                 |
| `revpar`    | float   | currency units/room    | Highly variable RevPAR under volatile market conditions.    |

---

## 3. `scenario_staff_shortage.csv`

| Column       | Type    | Range / Units         | Description                                                  |
|-------------|---------|------------------------|--------------------------------------------------------------|
| `day`       | int     | 0–179 (index)          | Simulation day index.                                       |
| `occupancy` | float   | 0.0–1.0                | Normalized occupancy rate.                                  |
| `fatigue`   | float   | 0.0–1.0                | Staff fatigue index (typically higher on average).          |
| `staff_level` | float | 0.0–1.0                | Normalized staffing level (typically lower on average).     |
| `revpar`    | float   | currency units/room    | RevPAR under staff-shortage stress conditions.              |

---

## 4. `hyperparam_sweep_results.csv`

| Column           | Type   | Range / Units            | Description                                                  |
|------------------|--------|--------------------------|--------------------------------------------------------------|
| `alpha`          | float  | > 0 (e.g., 0.01–0.1)     | Step size used in the ARGOS optimizer.                      |
| `cag_weight`     | float  | 0.0–1.0                  | Weighting factor for the CAG contour-based direction.       |
| `avg_revpar`     | float  | currency units/room      | Average RevPAR across the experiment horizon.               |
| `violations_tier1` | int  | ≥ 0                      | Count of Tier-1 feasibility violations (e.g., overbooking). |
| `fatigue_mean`   | float  | 0.0–1.0                  | Mean staff fatigue index across the horizon.                |

---

## 5. `qubo_example_matrix.csv`

Each row corresponds to one dimension of an 8×8 QUBO matrix.

| Column       | Type   | Range / Units            | Description                                                  |
|-------------|--------|--------------------------|--------------------------------------------------------------|
| `col_0`–`col_7` | int | typically -5 to +5      | QUBO coefficients \( Q_{ij} \) for binary decision vector.  |

(Actual column names may be generic numeric indices depending on CSV export; they represent the columns of the QUBO matrix.)

---

## 6. `multiunit_traffic_sim.csv`

| Column            | Type | Range / Units          | Description                                                  |
|-------------------|------|------------------------|--------------------------------------------------------------|
| `day`             | int  | 0–99 (index)           | Simulation day index.                                       |
| `hotel_0_traffic` | int  | ≥ 0 (counts)           | Approximate booking/traffic measure for hotel 0.            |
| `hotel_1_traffic` | int  | ≥ 0                    | Same for hotel 1.                                           |
| `hotel_2_traffic` | int  | ≥ 0                    | Same for hotel 2.                                           |
| `hotel_3_traffic` | int  | ≥ 0                    | Same for hotel 3.                                           |
| `hotel_4_traffic` | int  | ≥ 0                    | Same for hotel 4.                                           |

Traffic values represent relative load and are not tied to any real booking system.

---

All fields are generated synthetically; no direct mapping to any operational KPI, property, or organization exists. This makes the dataset suitable for open distribution and methodological benchmarking.
