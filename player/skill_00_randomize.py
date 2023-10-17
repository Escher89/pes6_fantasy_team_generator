import random

def overall(age):
    from team import overall_mu, overall_sigma, main_team_list

    overall = int(random.normalvariate(overall_mu,overall_sigma))

    if len(main_team_list) == 0:
        overall -= int(random.triangular(0, 100, 50))
    
    if age < 26:
        overall_age = overall + ((age - 26) * 5)
    elif age > 32:
        overall_age = overall - ((age - 32) * 3)
    else:
        overall_age = overall

    return overall, overall_age

def strength(bmi):
    x = (bmi - 22) / 10
    return x

def technique():
    x = random.triangular(0, 10, 5) / 20
    return x