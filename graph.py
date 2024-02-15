import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import skfuzzy.membership as mf

# mapping of parameters
x_age = np.arange(0, 90, 1) # 18 - 90
x_chol = np.arange(0, 400, 1) # 120 - 400
x_bp = np.arange(0, 200, 1) # 60 - 200
x_heartrate = np.arange(0, 110, 1) # 40 -110
x_exercise = np.arange(0, 20, 1) # 0 - 20 
x_BMI = np.arange(0, 40, 1) # 18 - 40
y_risk = np.linspace(0, 1, 100) # 0 - 1

# based on gen 99
b1 = 25.14
b2 = 249.915
b3 = 5
b4 = 13.65
b5 = 0.48
b6 = 17.5754

age_1 = 20+b1
age_2 = 20+(2*b1)
chol_1 = 50+b2
chol_2 = 50+(2*b2)
bp_1 = 70+b3
bp_2 = 70+(2*b3)
hr_1 = 60+b4
hr_2 = 60+(2*b4)
ex_1 = 5+b5
ex_2 = 5+(2*b5)
BMI_1 = 10+b6
BMI_2 = 10+(2*b6)

# Define ranges
age_1_range = (21, 55)
age_2_range = (22, 90)
chol_1_range = (51, 225)
chol_2_range = (52, 400)
bp_1_range = (71, 135)
bp_2_range = (72, 200)
hr_1_range = (61, 85)
hr_2_range = (62, 110)
ex_1_range = (6, 12.5)
ex_2_range = (7, 20)
BMI_1_range = (11, 25)
BMI_2_range = (12, 40)

# Adjust values to fall within range
age_1 = max(min(age_1, age_1_range[1]), age_1_range[0])
age_2 = max(min(age_2, age_2_range[1]), age_2_range[0])
chol_1 = max(min(chol_1, chol_1_range[1]), chol_1_range[0])
chol_2 = max(min(chol_2, chol_2_range[1]), chol_2_range[0])
bp_1 = max(min(bp_1, bp_1_range[1]), bp_1_range[0])
bp_2 = max(min(bp_2, bp_2_range[1]), bp_2_range[0])
hr_1 = max(min(hr_1, hr_1_range[1]), hr_1_range[0])
hr_2 = max(min(hr_2, hr_2_range[1]), hr_2_range[0])
ex_1 = max(min(ex_1, ex_1_range[1]), ex_1_range[0])
ex_2 = max(min(ex_2, ex_2_range[1]), ex_2_range[0])
BMI_1 = max(min(BMI_1, BMI_1_range[1]), BMI_1_range[0])
BMI_2 = max(min(BMI_2, BMI_2_range[1]), BMI_2_range[0])


# Assertions for age_1, age_2
assert 20 <= age_1 and age_1 <= age_2 and age_2 <= 90

# Assertions for chol_1, chol_2
assert 50 <= chol_1 and chol_1 <= chol_2 and chol_2 <= 400

# Assertions for bp_1, bp_2
assert 70 <= bp_1 and bp_1 <= bp_2 and bp_2 <= 200

# Assertions for hr_1, hr_2
assert 60 <= hr_1 and hr_1 <= hr_2 and hr_2 <= 110

# Assertions for ex_1, ex_2
assert 5 <= ex_1 and ex_1 <= ex_2 and ex_2 <= 20

# Assertions for BMI_1, BMI_2
assert 10 <= BMI_1 and BMI_1 <= BMI_2 and BMI_2 <= 40


#define membership functions using passed parameters
age_low = mf.trapmf(x_age, [0, 0, 20, age_1])
age_mid = mf.trimf(x_age, [20, age_1, age_2]) 
age_high = mf.trapmf(x_age, [age_1, age_2, 90, 90])

chol_low = mf.trapmf(x_chol, [0, 0, 50, chol_1])
chol_mid = mf.trimf(x_chol, [50, chol_1, chol_2]) 
chol_high = mf.trapmf(x_chol, [chol_1, chol_2, 400, 400])

bp_low = mf.trapmf(x_bp, [0, 0, 70, bp_1])
bp_mid = mf.trimf(x_bp, [70, bp_1, bp_2]) 
bp_high = mf.trapmf(x_bp, [bp_1, bp_2, 200, 200])

heartrate_low = mf.trapmf(x_heartrate, [0, 0, 60, hr_1])
heartrate_mid = mf.trimf(x_heartrate, [60, hr_1, hr_2]) 
heartrate_high = mf.trapmf(x_heartrate, [hr_1, hr_2, 110, 110])

exercise_low = mf.trapmf(x_exercise, [0, 0, 5, ex_1])
exercise_mid = mf.trimf(x_exercise, [5, ex_1, ex_2]) 
exercise_high = mf.trapmf(x_exercise, [ex_1, ex_2, 20, 20])

BMI_low = mf.trapmf(x_BMI, [0, 0, 10, BMI_1])
BMI_mid = mf.trimf(x_BMI, [10, BMI_1, BMI_2]) 
BMI_high = mf.trapmf(x_BMI, [BMI_1, BMI_2, 40, 40])

risk_low = mf.trapmf(y_risk, [0, 0, 0.25, 0.5])
risk_mid = mf.trimf(y_risk, [0.25, 0.5, 0.75]) 
risk_high = mf.trapmf(y_risk, [0.75, 1, 1, 1])

fig, (ax0, ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(nrows = 7, figsize =(10, 25))

ax0.plot(x_age, age_low, 'r', linewidth = 2, label = 'Young')
ax0.plot(x_age, age_mid, 'g', linewidth = 2, label = 'Middle')
ax0.plot(x_age, age_high, 'b', linewidth = 2, label = 'Old')
ax0.set_title('age')
ax0.legend()

ax1.plot(x_chol, chol_low, 'r', linewidth = 2, label = 'Low')
ax1.plot(x_chol, chol_mid, 'g', linewidth = 2, label = 'Middle')
ax1.plot(x_chol, chol_high, 'b', linewidth = 2, label = 'High')
ax1.set_title('Blood Pressure')
ax1.legend()

ax2.plot(x_bp, bp_low, 'r', linewidth = 2, label = 'Low')
ax2.plot(x_bp, bp_mid, 'g', linewidth = 2, label = 'Middle')
ax2.plot(x_bp, bp_high, 'b', linewidth = 2, label = 'High')
ax2.set_title('Colestrol')
ax2.legend()

ax2.plot(x_heartrate, heartrate_low, 'r', linewidth = 2, label = 'Low')
ax2.plot(x_heartrate, heartrate_mid, 'g', linewidth = 2, label = 'Middle')
ax2.plot(x_heartrate, heartrate_high, 'b', linewidth = 2, label = 'High')
ax2.set_title('Colestro')
ax2.legend()

ax4.plot(x_exercise, exercise_low, 'r', linewidth = 2, label = 'Low')
ax4.plot(x_exercise, exercise_mid, 'g', linewidth = 2, label = 'Middle')
ax4.plot(x_exercise, exercise_high, 'b', linewidth = 2, label = 'High')
ax4.set_title('exercise')
ax4.legend()

ax5.plot(x_BMI, BMI_low, 'r', linewidth = 2, label = 'Low')
ax5.plot(x_BMI, BMI_mid, 'g', linewidth = 2, label = 'Middle')
ax5.plot(x_BMI, BMI_high, 'b', linewidth = 2, label = 'High')
ax5.set_title('BMI')
ax5.legend()

ax6.plot(y_risk, risk_low, 'g', linewidth = 2, label = 'Little')
ax6.plot(y_risk, risk_mid, 'b', linewidth = 2, label = 'Middle')
ax6.plot(y_risk, risk_high, 'y', linewidth = 2, label = 'High')
ax6.set_title('Risk')
ax6.legend()

plt.tight_layout()