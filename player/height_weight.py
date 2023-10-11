import random

def height_weight(mu,sigma,min,max,bmi_mu):
        height = int(random.normalvariate(mu,sigma))
        if height < min:
            height = min + random.randint(-3,3)
        if height > max:
            height = max + random.randint(-3,3)
        #print("Height: ",height)

        bmi = random.normalvariate(bmi_mu,1)
        weight = int(bmi*((height/100)*(height/100)))
        #print("Weight: ",weight) 
        return [height, weight, bmi]