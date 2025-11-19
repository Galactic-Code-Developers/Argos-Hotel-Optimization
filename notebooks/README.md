# ARGOS Notebooks Directory

This directory contains all interactive Jupyter/Colab notebooks used for the
experiments, demonstrations, and reproductions associated with the **ARGOS
(Adaptive Recursive Gradient Optimization System)** project.

The notebooks are designed to be:

- 🔬 **Reproducible** — same results as the paper  
- 🎓 **Explanatory** — includes comments, plots, and step-by-step execution  
- 🧪 **Experimental** — supports ablation studies and scenario tests  
- ☁️ **Colab-ready** — runs without modification on Google Colab  

All notebooks use synthetic data only and do not require external dependencies beyond those listed in the project’s `requirements.txt`.

---

## 📘 Included Notebooks

### 1. **ARGOS_Single_Hotel_Demo.ipynb**
A complete walk-through of ARGOS applied to a **single hotel environment**.

**Contents:**
- Environment initialization  
- Lexicographic tier construction  
- CAG filtering demonstration  
- ARGOS rollout over time  
- Plots of occupancy, fatigue, RevPAR, constraint violations  

**Purpose:**  
Reproduces the core results for **Section 6** of the ARGOS paper.

---

### 2. **ARGOS_Multi_Unit_Demo.ipynb**
ARGOS running **in parallel across multiple hotel units**.

**Contents:**
- Multiple hotel environments  
- Independent ARGOS optimizers  
- Multi-unit coordination  
- Comparative performance plots  

**Purpose:**  
Reproduces experiments from **Section 7**.

---

### 3. **ARGOS_Ablation_Study.ipynb**
Compares:

- Newton-only  
- CAG-only  
- Full ARGOS (LCO + CAG)

**Evaluations:**
- Convergence  
- Tier-1 violations  
- Fatigue & RevPAR  
- Stability  

**Purpose:**  
Supports **Appendix D — Ablation Studies**.

---

## 🚀 Running the Notebooks in Google Colab

**Step 1 — Clone repo or upload notebook**
```python
!git clone https://github.com/<your-org>/argos-hotel-optimization.git
%cd argos-hotel-optimization
```

**Step 2 — Install dependencies**
```python
!pip install -q -r requirements.txt
```

**Step 3 — Run cells normally**

---

## 🖥 Running Locally (Jupyter)

**Step 1 — Install environment**
```bash
pip install -r requirements.txt
```

**Step 2 — Launch notebooks**
```bash
jupyter notebook
```

---

## 🔍 Reproduction Details

- All notebooks include **fixed seeds**  
- Plots replicate paper figures  
- Links to **Zenodo datasets** included  
- Output metrics match published results  

---

## 📄 Citation

If you use these notebooks, cite both:

**Software:**  
https://doi.org/10.5281/zenodo.17645169  

**Datasets:**  
https://doi.org/10.5281/zenodo.17645086  
