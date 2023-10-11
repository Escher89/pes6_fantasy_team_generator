import random

def name_changer(name):
    
    def containsVowels(name):
        #name = name.lower()
        for char in name:
            if char in "aeiou":
                return True
        return False
  
    vowels = ["a","e","i","o","u"]
    if len(name) > 2 and containsVowels(name) == True: 
        z = -1
        x = -1
        if random.randint(1,2) == 1:
            while x == -1:
                z += 1
                x = name.rfind(vowels[z], 1)
                if x != -1:
                    break
        else:
            while x == -1:
                z += 1
                x = name.find(vowels[z], 1)
                if x != -1:
                    break
        vowels.pop(z)
        y = list(name)
        y[x] = vowels[random.randint(0,3)]
        a = "".join(y)
        print("After: ", a)
    else:
        print("After: ", name)
        print("Name is too short or doesn't contain any vowels")

name_changer(input("Before: "))