import random

def overall():
    from team import overall_mu, overall_sigma
    overall = random.normalvariate(overall_mu,overall_sigma)
    #print("Overall: ",overall)
    return overall

def starting_eleven_bonus():
    from team import main_team_list
    if len(main_team_list) > 0:
        s_e_b = random.triangular(0,2,1)
    else:
        s_e_b = 0.0
    return s_e_b

def age_factor(age):
    lst_16to28 = [-2,-1.805,-1.615,-1.43,-1.25,-1.075,-0.905,-0.74,-0.58,-0.425,-0.275,-0.13,0]
    lst_29to40 = [-0.135,-0.285,-0.44,-0.6-0.765,-0,935,-1.11,-1.29,-1.475,-1.665,-1.86,-2.06]
    if age < 29:
        a_f = lst_16to28[age - 16]
    else:
        a_f = lst_29to40[age - 29]
    return a_f

starting_eleven_bonus()