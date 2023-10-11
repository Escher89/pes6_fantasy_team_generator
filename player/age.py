import random
def age(mu,sigma):
        
        age = random.normalvariate(mu,sigma)
        
        if int(age) > 37:
                x = random.choices(list(range(0,4)),weights= [7,5,3,1]) 
                age = 37 + x[0]
        
        if int(age) < 17:
                x = random.choices(list(range(-1,3)),weights= [1,3,5,7]) 
                age = 17 + x[0]
        
        return int(age)