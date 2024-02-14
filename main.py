
import numpy as np
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt

# mapping of parameters
x_age = np.arange(0, 90, 1) # 18 - 90
x_chol = np.arange(0, 400, 1) # 120 - 400
x_bp = np.arange(0, 200, 1) # 60 - 200
x_heartrate = np.arange(0, 110, 1) # 40 -110
x_exercise = np.arange(0, 20, 1) # 0 - 20 
x_BMI = np.arange(0, 40, 1) # 18 - 40
y_risk = np.arange(0, 1, 0.01) # 0 - 1

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

    #test parameters
    input_age = 87
    input_chol = 313
    input_bp = 91
    input_heartrate = 110
    input_exercise = 14.79
    input_BMI = 29.33
    input_risk = 0

    #define membership functions using passed parameters
    age_low = mf.trapmf(x_age, [0, 0, 20, 20+b1])
    age_mid = mf.trimf(x_age, [20, 20+b1, 20+2*b1]) 
    age_high = mf.trapmf(x_age, [20+b1, 20+2*b1, 90, 100])

    chol_low = mf.trapmf(x_chol, [0, 0, 50, 50+b2])
    chol_mid = mf.trimf(x_chol, [50, 50+b2, 50+2*b2]) 
    chol_high = mf.trapmf(x_chol, [50+b2, 50+2*b2, 400, 400])

    bp_low = mf.trapmf(x_bp, [0, 0, 70, 70+b3])
    bp_mid = mf.trimf(x_bp, [70, 70+b3, 70+2*b3]) 
    bp_high = mf.trapmf(x_bp, [70+b3, 70+2*b3, 200, 200])

    heartrate_low = mf.trapmf(x_heartrate, [0, 0, 60, 60+b4])
    heartrate_mid = mf.trimf(x_heartrate, [60, 60+b4, 60+2*b4]) 
    heartrate_high = mf.trapmf(x_heartrate, [60+b4, 60+2*b4, 110, 110])

    exercise_low = mf.trapmf(x_exercise, [0, 0, 5, 5+b5])
    exercise_mid = mf.trimf(x_exercise, [5, 5+b5, 5+2*b5]) 
    exercise_high = mf.trapmf(x_exercise, [5+b5, 5+2*b5, 20, 20])

    BMI_low = mf.trapmf(x_BMI, [0, 0, 10, 10+b6])
    BMI_mid = mf.trimf(x_BMI, [10, 10+b6, 10+2*b6]) 
    BMI_high = mf.trapmf(x_BMI, [10+b6, 10+2*b6, 40, 40])



    target_sum = 0
    output_sum = 0
    for i in range(10):
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
        rule1 = np.fmin(np.fmin(chol_fit_high,bp_fit_high),heartrate_fit_high)
        rule2 = np.fmin(heartrate_fit_high,exercise_fit_low)
        rule3 = np.fmin(exercise_fit_low,BMI_fit_high)
        rule4 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(age_fit_high,chol_fit_mid),bp_fit_mid),heartrate_fit_mid),exercise_fit_low),BMI_fit_mid)
        rule5 = np.fmin(np.fmin(np.fmin(chol_fit_mid,bp_fit_mid),heartrate_fit_mid),exercise_fit_mid)
        rule6 = np.fmin(np.fmin(np.fmin(chol_fit_mid,bp_fit_mid),heartrate_fit_mid),exercise_fit_high)
        rule7 = np.fmin(chol_fit_low,bp_fit_mid)
        rule8 = np.fmin(chol_fit_mid,bp_fit_low)
        rule9 = np.fmin(exercise_fit_high,BMI_fit_high)
        rule10 = np.fmin(np.fmin(np.fmin(np.fmin(chol_fit_mid,bp_fit_mid),heartrate_fit_mid),exercise_fit_low),BMI_fit_mid)
        rule11 = np.fmin(np.fmin(chol_fit_low,bp_fit_low),heartrate_fit_low)
        rule12 = np.fmin(exercise_fit_high,BMI_fit_mid)
        rule13 = np.fmin(np.fmin(np.fmin(np.fmin(chol_fit_mid,bp_fit_mid),heartrate_fit_mid),exercise_fit_low),BMI_fit_low)
        rule14 = np.fmin(np.fmin(np.fmin(np.fmin(chol_fit_mid,bp_fit_mid),heartrate_fit_mid),exercise_fit_mid),BMI_fit_low)
        rule15 = np.fmin(np.fmin(np.fmin(np.fmin(chol_fit_mid,bp_fit_mid),heartrate_fit_mid),exercise_fit_high),BMI_fit_low)
        rule16 = np.fmin(np.fmin(age_fit_low,exercise_fit_mid),BMI_fit_mid)
        rule17 = np.fmin(np.fmin(age_fit_mid,exercise_fit_mid),BMI_fit_mid)
        rule18 = np.fmin(np.fmin(age_fit_high,exercise_fit_mid),BMI_fit_mid)
    
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
        # result = fuzz.interp_membership(y_risk, out_risk, defuzzified)

        target_sum += defuzzified
        output_sum += input_risk
    
    target = target_sum/10
    output = output_sum/10

    fitness_avg = fitness(target,output)
    return fitness_avg


#generate solutions
solutions = []
for s in range(500):
    solutions.append((np.random.uniform(1,35),
                      np.random.uniform(1,175),
                      np.random.uniform(1,65),
                      np.random.uniform(1,50),
                      np.random.uniform(1,7.5),
                      np.random.uniform(1,14)))

# create membership functions
for gen in range(1000):
    rankedsolutions = []
    for s in solutions:
        rankedsolutions.append((membership(s[0],s[1],s[2],s[3],s[4],s[5]),s))
    rankedsolutions.sort(reverse=True)

    print(f"=== Gen {gen} best solutionss ===")
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
        


            


