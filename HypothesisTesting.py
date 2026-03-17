# Hypothesis Testing
## Use mean value here
# Hypothesis Testing - Statistics Spring 2026
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, signal
from sklearn.linear_model import LinearRegression
np.random.seed(1)
# Continuous glucose monitoring (CGM)
# -----------------------------
# 1. Simulate CGM data
# -----------------------------
# Time: 24 hours sampled every 5 minutes (288 points)
t = np.arange(0,288)
# Baseline glucose (~100 mg/dL)
baseline = 100
# Simulate daily glucose with meals (spikes)
glucose = basiline +10*np.sin(2*np.pi*t/288)
 # circadian rhythm
 
 # add meal spikes
 for meal_time in [50, 120, 200]:
     glucose += 40*np.exp(-(t-meal_time)**2/50)
# add noise
glucose += np.random.normal(0,5,len(t))

# -----------------------------
# 2. Basic statistics
# -----------------------------
print("Mean glucose:", np.mean(glucose))
print("Std glucose:", np.std(glucose, ddof=1))
print("Variance glucose:", np.var(glucose, ddof=1))
print("Median glucose:", np.median(glucose))

plt.hist(glucose)
plt.title("Glucose Distribution")
plt.xlabel("mg/dL")
plt.show()