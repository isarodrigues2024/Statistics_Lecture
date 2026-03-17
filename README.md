# Statistics_Lecture
Statistics lecture
# 🧪 Continuous Glucose Monitoring (CGM) & Interval Exercise

## 📌 Project Overview

This project simulates a **non-invasive CGM patch** to study the effect of **interval exercise (HIIT)** on glucose levels using Python.

It combines:

* Descriptive statistics
* Hypothesis testing
* Correlation & regression
* Signal processing (FFT & Welch)

---

## 🎯 Research Question

Does interval exercise significantly reduce glucose levels?

---

## 🧠 Hypotheses

* **H0:** Exercise has no effect on glucose
* **H1:** Exercise reduces glucose

---

## 🧑‍💻 Code

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, signal
from sklearn.linear_model import LinearRegression

np.random.seed(42)

# -----------------------------
# 1. Simulate CGM data
# -----------------------------
t = np.arange(0, 288)

glucose = 100 + 10*np.sin(2*np.pi*t/288)

# Meal spikes
for meal in [60, 140, 220]:
    glucose += 35*np.exp(-(t - meal)**2 / 60)

# Exercise effect
exercise_periods = [(80, 100), (180, 200)]
for start, end in exercise_periods:
    glucose[start:end] -= 15

# Noise
glucose += np.random.normal(0, 5, len(glucose))

# -----------------------------
# 2. Basic statistics
# -----------------------------
print("Mean:", np.mean(glucose))
print("Std:", np.std(glucose, ddof=1))
print("Var:", np.var(glucose, ddof=1))
print("Median:", np.median(glucose))

plt.hist(glucose)
plt.title("Glucose Distribution")
plt.show()

# -----------------------------
# 3. Hypothesis testing
# -----------------------------

# One-sample test
print(stats.ttest_1samp(glucose, 100))

# Independent test (morning vs evening)
morning = glucose[:144]
evening = glucose[144:]
print(stats.ttest_ind(morning, evening))

# Paired test (before vs during exercise)
before = glucose[70:80]
during = glucose[80:90]
print(stats.ttest_rel(before, during))

# ANOVA
afternoon = glucose[96:192]
night = glucose[192:]
print(stats.f_oneway(morning, afternoon, night))

# -----------------------------
# 4. Correlation & Regression
# -----------------------------

# Simulated insulin
insulin = 0.5 * glucose + np.random.normal(0, 10, len(glucose))

print(stats.pearsonr(glucose, insulin))

X = glucose.reshape(-1, 1)
y = insulin

model = LinearRegression()
model.fit(X, y)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# -----------------------------
# 5. Signal processing
# -----------------------------

# FFT
fft_vals = np.fft.fft(glucose)

# Welch
freqs, psd = signal.welch(glucose, fs=1)

plt.plot(freqs, psd)
plt.title("Power Spectrum")
plt.show()

# -----------------------------
# 6. Visualization
# -----------------------------

plt.plot(t, glucose)
for start, end in exercise_periods:
    plt.axvspan(start, end, alpha=0.3)

plt.title("CGM with Exercise")
plt.xlabel("Time")
plt.ylabel("Glucose")
plt.show()
```

---

## 📊 Results Interpretation

* Exercise periods show decreased glucose
* Statistical tests indicate significance (depending on p-value)
* Correlation shows relationship between glucose and insulin
* Frequency analysis reveals periodic patterns

---

## 🚀 How to Run

```bash
pip install numpy matplotlib scipy scikit-learn
python cgm_project.py
```

---

## 🔬 Future Work

* Add real CGM data
* Improve physiological modeling
* Detect exercise automatically
* Multi-patient simulation

---

## 📁 Project Structure

```
CGM_Project/
│── README.md
│── cgm_project.py
│── figures/
│── data/ (optional)
```

---

## 🧠 Learning Outcomes

* Apply hypothesis testing
* Understand biomedical signals
* Use Python for data analysis
* Combine statistics + physiology
