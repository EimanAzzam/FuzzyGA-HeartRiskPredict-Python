import pandas as pd
import numpy as np
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt

# Read data from Excel file into a DataFrame
df = pd.read_excel(r'C:\Users\Hp\Downloads\HeartAttackTrain.xlsx')

# Convert DataFrame to NumPy array
data_array = df.to_numpy()


# mapping of parameters
x_age = np.arange(0, 90, 1) # 18 - 90
x_chol = np.arange(0, 400, 1) # 120 - 400
x_bp = np.arange(0, 200, 1) # 60 - 200
x_heartrate = np.arange(0, 110, 1) # 40 -110
x_exercise = np.arange(0, 20, 1) # 0 - 20 
x_BMI = np.arange(0, 40, 1) # 18 - 40
y_risk = np.linspace(0, 1, 100) # 0 - 1

risk_low = mf.trapmf(y_risk, [0, 0, 0.25, 0.5])
risk_mid = mf.trimf(y_risk, [0.25, 0.5, 0.75]) 
risk_high = mf.trapmf(y_risk, [0.75, 1, 1, 1])

def fitness(target,output):
    ans = abs(target - output)
    if ans == 0:
        return 99999
    else:
        return abs(1/ans)
    
def membership(b1,b2,b3,b4,b5,b6):

    count = 0
    #ensure all positive values
    b1 = abs(b1)
    b2 = abs(b2)
    b3 = abs(b3)
    b4 = abs(b4)
    b5 = abs(b5)
    b6 = abs(b6)

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

    target_sum = 0
    output_sum = 0
    
    for i in range(10):
        input_age = data_array[count][0]
        input_chol = data_array[count][1]
        input_bp_raw = data_array[count][2]
        num, denom = map(int, input_bp_raw.split('/'))
        input_bp = denom + (1/3) * (num - denom)
        input_heartrate = data_array[count][3]
        input_exercise = data_array[count][4]
        input_BMI = data_array[count][5]
        input_risk = data_array[count][6]
        count = count + 1
        #Fuzzify input to get membership values
        age_fit_low = fuzz.interp_membership(x_age, age_low, input_age)
        age_fit_mid = fuzz.interp_membership(x_age, age_mid, input_age)
        age_fit_high = fuzz.interp_membership(x_age, age_high, input_age)

        chol_fit_low = fuzz.interp_membership(x_chol, chol_low, input_chol)
        chol_fit_mid = fuzz.interp_membership(x_chol, chol_mid, input_chol)
        chol_fit_high = fuzz.interp_membership(x_chol, chol_high, input_chol)

        bp_fit_low = fuzz.interp_membership(x_bp, bp_low, input_bp)
        bp_fit_mid = fuzz.interp_membership(x_bp, bp_mid, input_bp)
        bp_fit_high = fuzz.interp_membership(x_bp, bp_high, input_bp)

        heartrate_fit_low = fuzz.interp_membership(x_heartrate, heartrate_low, input_heartrate)
        heartrate_fit_mid = fuzz.interp_membership(x_heartrate, heartrate_mid, input_heartrate)
        heartrate_fit_high = fuzz.interp_membership(x_heartrate, heartrate_high, input_heartrate)

        exercise_fit_low = fuzz.interp_membership(x_exercise, exercise_low, input_exercise)
        exercise_fit_mid = fuzz.interp_membership(x_exercise, exercise_mid, input_exercise)
        exercise_fit_high = fuzz.interp_membership(x_exercise, exercise_high, input_exercise)

        BMI_fit_low = fuzz.interp_membership(x_BMI, BMI_low, input_BMI)
        BMI_fit_mid = fuzz.interp_membership(x_BMI, BMI_mid, input_BMI)
        BMI_fit_high = fuzz.interp_membership(x_BMI, BMI_high, input_BMI)

        #create rule base
        rule1 = np.fmin(np.fmin(np.fmin(chol_fit_high,bp_fit_high),heartrate_fit_high),risk_high)
        rule2 = np.fmin(np.fmin(heartrate_fit_high,exercise_fit_low),risk_high)
        rule3 = np.fmin(np.fmin(exercise_fit_low,BMI_fit_high),risk_high)
        rule4 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(age_fit_high,chol_fit_mid),bp_fit_mid),heartrate_fit_mid),exercise_fit_low),BMI_fit_mid),risk_high)
        rule5 = np.fmin(np.fmin(np.fmin(np.fmin(chol_fit_mid,bp_fit_mid),heartrate_fit_mid),exercise_fit_mid),risk_mid)
        rule6 = np.fmin(np.fmin(np.fmin(np.fmin(chol_fit_mid,bp_fit_mid),heartrate_fit_mid),exercise_fit_high),risk_mid)
        rule7 = np.fmin(np.fmin(chol_fit_low,bp_fit_mid),risk_mid)
        rule8 = np.fmin(np.fmin(chol_fit_mid,bp_fit_low),risk_mid)
        rule9 = np.fmin(np.fmin(exercise_fit_high,BMI_fit_high),risk_mid)
        rule10 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(chol_fit_mid,bp_fit_mid),heartrate_fit_mid),exercise_fit_low),BMI_fit_mid),risk_mid)
        rule11 = np.fmin(np.fmin(np.fmin(chol_fit_low,bp_fit_low),heartrate_fit_low),risk_low)
        rule12 = np.fmin(np.fmin(exercise_fit_high,BMI_fit_mid),risk_low)
        rule13 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(chol_fit_mid,bp_fit_mid),heartrate_fit_mid),exercise_fit_low),BMI_fit_low),risk_mid)
        rule14 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(chol_fit_mid,bp_fit_mid),heartrate_fit_mid),exercise_fit_mid),BMI_fit_low),risk_low)
        rule15 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(chol_fit_mid,bp_fit_mid),heartrate_fit_mid),exercise_fit_high),BMI_fit_low),risk_low)
        rule16 = np.fmin(np.fmin(np.fmin(age_fit_low,exercise_fit_mid),BMI_fit_mid),risk_low)
        rule17 = np.fmin(np.fmin(np.fmin(age_fit_mid,exercise_fit_mid),BMI_fit_mid),risk_mid)
        rule18 = np.fmin(np.fmin(np.fmin(age_fit_high,exercise_fit_mid),BMI_fit_mid),risk_mid)
    
        #get fuzzified output referring to rule base
        out_low =   np.fmax(np.fmax(np.fmax(np.fmax
                    (rule11,rule12),rule14),rule15),rule16)
        out_mid =   np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax
                    (rule5,rule6),rule7),rule8),rule9),rule10),rule13),rule17),rule18)
        out_high =  np.fmax(np.fmax(np.fmax
                    (rule1,rule2),rule3),rule4)
        
        #defuzzification
        out_risk = np.fmax(np.fmax(out_low,out_mid), out_high)
        defuzzified  = fuzz.defuzz(y_risk, out_risk, 'centroid')
        result = fuzz.interp_membership(y_risk, out_risk, defuzzified)

        target_sum = target_sum + input_risk
        output_sum = output_sum + defuzzified
    
    target = target_sum/10
    output = output_sum/10

    fitness_avg = fitness(target,output)
    return fitness_avg


#generate solutions
solutions = []
for s in range(500):
    solutions.append((np.random.uniform(1,35),
                      np.random.uniform(1,175),
                      np.random.uniform(1,65 ),
                      np.random.uniform(1,25 ),
                      np.random.uniform(1,7.5),
                      np.random.uniform(1,14 )))

for gen in range(100):
    rankedsolutions = []
    for s in solutions:
        rankedsolutions.append((membership(s[0],s[1],s[2],s[3],s[4],s[5]),s))
    rankedsolutions.sort(reverse=True)

    print(f"=== Gen {gen} best solutions ===")
    print(rankedsolutions[0])

    bestsolutions = rankedsolutions[:100]

    elements_0 = []
    elements_1 = []
    elements_2 = []
    elements_3 = []
    elements_4 = []
    elements_5 = []
    for s in bestsolutions:
        elements_0.append(s[1][0])
        elements_1.append(s[1][1])
        elements_2.append(s[1][2])
        elements_3.append(s[1][3])
        elements_4.append(s[1][4])
        elements_5.append(s[1][5])

    newGen = []
    for s in range(500):
        e0 = np.random.choice(elements_0) * np.random.uniform(0.95,1.05)
        e1 = np.random.choice(elements_1) * np.random.uniform(0.95,1.05)
        e2 = np.random.choice(elements_2) * np.random.uniform(0.95,1.05)
        e3 = np.random.choice(elements_3) * np.random.uniform(0.95,1.05)
        e4 = np.random.choice(elements_4) * np.random.uniform(0.95,1.05)
        e5 = np.random.choice(elements_5) * np.random.uniform(0.95,1.05)

        newGen.append((e0,e1,e2,e3,e4,e5))

    solutions = newGen
        


            


