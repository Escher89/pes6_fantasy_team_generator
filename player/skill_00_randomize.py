import random

def overall():
    from team import overall_mu, overall_sigma
    overall = random.normalvariate(overall_mu,overall_sigma)
    x = overall / 100 + 0.8
    #print("Overall: ",overall)
    return x

def starting_eleven_bonus():
    from team import main_team_list
    if len(main_team_list) > 0:
        s_e_b = 1.0
    else:
        s_e_b = random.triangular(0.5, 1.0, 0.75)
    return s_e_b

def age_factor(age):
    lst_16to28 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    lst_29to40 = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    if age < 29:
        a_f = lst_16to28[age - 16]
        a = 0.2/13 * a_f + 0.8 
    else:
        a_f = lst_29to40[age - 29]
        a = 0.2/13 * a_f + 0.8
    return a

def strength(bmi):
    x = bmi - 20
    y = random.triangular(1, 8, 6)
    z = (x + y) / 10
    return z

def technique():
    x = random.triangular(1, 8, 6)
    return x
