# ARGOS Synthetic Hotel Optimization Datasets — Data Descriptor

## Background & Summary

The ARGOS (Adaptive Recursive Gradient Optimization System) framework integrates
Lexicographic Constraint Optimization (LCO) with a Componentwise Approximated
Gradient (CAG) filter to enable stable, lexicographically safe optimization in
hierarchical decision-making problems. To support reproducibility and to
facilitate independent evaluation of ARGOS, we release a suite of fully
synthetic datasets that emulate hotel and multi-unit management scenarios under
varied operating conditions.

The datasets capture key dimensions of hotel operations, including occupancy,
staffing levels, staff fatigue, and revenue per available room (RevPAR), as well
as higher-level constructs such as scenario volatility, resource constraints, and
multi-property traffic patterns. No real hotel operational data or personal data
are used: all records are synthesized from a controlled stochastic simulator.

These datasets are intended as a reproducible testbed for:

- Lexicographic optimization under strict Tier-1 “feasibility” constraints,
- Evaluation of componentwise gradient filtering (CAG),
- Benchmarking of ARGOS against baseline optimization methods, and
- Future extensions to QUBO/quantum-hybrid hotel management formulations.

## Methods

### Simulation Framework

All datasets are generated using a stylized CMDP-like hotel environment
implemented within the ARGOS codebase. The environment describes a single hotel
(or a collection of hotels) through a state vector including normalized
occupancy, staff level, staff fatigue index, and pricing/revenue variables.

At each simulated time step, the environment evolves according to:

- deterministic dynamics capturing baseline demand and staffing trends,
- stochastic noise terms representing unmodeled variability,
- scenario-specific modifications (e.g., increased volatility or reduced staff).

ARGOS and baseline controllers produce candidate actions (price adjustments,
staffing decisions, or control signals), which are mapped to state transitions.
For the released datasets, the underlying policy is fixed and the primary focus
is on the resulting trajectories rather than policy optimization itself.

### Scenarios

We provide several distinct scenario families:

- **Long-horizon baseline:** 365-day single-hotel operation under moderate
  noise, used to study stability and convergence.

- **High-volatility scenario:** 180-day simulation with amplified noise on
  occupancy, fatigue, and RevPAR to test robustness under non-stationary,
  high-variance conditions.

- **Staff-shortage scenario:** 180-day simulation where staff levels are
  systematically reduced and fatigue is typically elevated, stressing Tier-1
  feasibility (minimum staff) and Tier-3 “staff well-being” priorities.

- **Multi-unit traffic:** 100-day simulation of booking traffic across multiple
  hotel units, approximating heterogeneous demand across properties.

- **Hyperparameter sweep:** summary statistics across varying step sizes and
  CAG weighting coefficients, illustrating the sensitivity of performance and
  Tier-1 violations to hyperparameter choices.

- **QUBO example:** a small random QUBO matrix for demonstration of
  binary-optimization interfaces; no direct trajectory data is associated.

## Data Records

All datasets are provided as CSV files in the `data/` directory of the ARGOS
repository (and mirrored in the Zenodo deposition). The main files are:

1. `synthetic_long_horizon.csv` — 365 daily records of a single-hotel
   environment with columns: `day`, `occupancy`, `fatigue`, `staff_level`,
   `revpar`.

2. `scenario_high_volatility.csv` — 180 daily records under increased
   volatility with columns: `day`, `occupancy`, `fatigue`, `revpar`.

3. `scenario_staff_shortage.csv` — 180 daily records under staff-shortage
   stress with columns: `day`, `occupancy`, `fatigue`, `staff_level`, `revpar`.

4. `hyperparam_sweep_results.csv` — summary statistics for combinations of
   step size `alpha` and `cag_weight`, with columns: `alpha`, `cag_weight`,
   `avg_revpar`, `violations_tier1`, `fatigue_mean`.

5. `qubo_example_matrix.csv` — an 8×8 QUBO coefficient matrix, stored in
   wide form with each row representing one dimension of the binary quadratic
   form.

6. `multiunit_traffic_sim.csv` — 100-day multi-unit booking traffic simulation
   with columns: `day`, `hotel_0_traffic`–`hotel_4_traffic`.

Each file is accompanied by a data dictionary (see below), describing the
semantic meaning, type, and range of each column.

## Technical Validation

Because the data are synthetic, validation focuses on internal consistency and
plausibility rather than on comparison with an external ground truth.

- **Internal consistency:** the simulator enforces reasonable bounds on
  occupancy (0–1), staff levels (0–1), and fatigue indices (0–1). RevPAR values
  follow plausible distributions for mid-tier hotels but do not reproduce any
  specific operator’s financials.

- **Scenario behavior:** high-volatility scenarios show visibly increased
  variance in occupancy and revenue; staff-shortage scenarios show lower average
  staff levels and generally higher fatigue. These patterns were inspected
  visually via time-series plots and summary statistics.

- **Hyperparameter sensitivity:** the hyperparameter sweep dataset is generated
  using repeated runs with fixed seeds, ensuring stable comparisons between
  configurations while still reflecting stochastic variability within runs.

- **Reproducibility:** the Python scripts and notebooks used to generate these
  datasets are included in the ARGOS repository, enabling full regeneration
  under controlled seeds.

## Usage Notes

The datasets are designed for:

- Reproducing the experiments reported in the ARGOS paper,
- Extending the analysis with additional baselines or ablations,
- Serving as controlled environments for studying lexicographic / hierarchical
  optimization techniques.

Users should note that the datasets:

- Do not represent any specific real hotel or chain,
- Should not be used for financial forecasting or business decisions,
- May be adapted or extended by modifying the ARGOS simulation code and
  regenerating trajectories with different parameter choices.

When using these datasets in publications or derived work, please cite the ARGOS
paper and (optionally) the Zenodo dataset DOI.
