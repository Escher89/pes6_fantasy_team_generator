import csv
import random
    
# opening the CSV file  
with open('player_names/Netherlands.csv', mode ='r')as file:  
      
# reading the CSV file  
    csvFile = csv.reader(file)  
    rows = list(csvFile)    
    
    x = random.randint(0,len(rows) - 1)
    y = rows[x]
    print(y)

### Name    
    if "/" in y[-1]:
        b = y[-1].split("/")        
        if len(b) == 2:
            a = random.randint(0,len(b) - 1)
            if a == 0:
                b.pop(0)
                d = b[0]
            else:
                b.pop(1)
                d = b[0]
            y.pop(-1)
            y.append(d)
        if len(b) == 3:
            a = random.randint(0,len(b) - 1)
            if a == 0:
                b.pop(0)
                b.pop(0)
                d = b[0]
            elif a == 1:
                b.pop(0)
                b.pop(-1)
                d = b[0]
            else:
                b.pop(-1)
                b.pop(-1)
                d = b[0]  
            y.pop(-1)
            y.append(d)

### 2nd prefix
    if "/" in y[1]:
        b = y[1].split("/")        
        if len(b) == 2:
            a = random.randint(0,len(b) - 1)
            if a == 0:
                b.pop(0)
                d = b[0]
            else:
                b.pop(1)
                d = b[0]
            y.pop(1)
            y.insert(1,d)
        if len(b) == 3:
            a = random.randint(0,len(b) - 1)
            if a == 0:
                b.pop(0)
                b.pop(0)
                d = b[0]
            elif a == 1:
                b.pop(0)
                b.pop(-1)
                d = b[0]
            else:
                b.pop(-1)
                b.pop(-1)
                d = b[0]  
            y.pop(1)
            y.insert(1,d)

### 1st prefix
    if "/" in y[0]:
        b = y[0].split("/")        
        if len(b) == 2:
            a = random.randint(0,len(b) - 1)
            if a == 0:
                b.pop(0)
                d = b[0]
            else:
                b.pop(1)
                d = b[0]
            y.pop(0)
            y.insert(0,d)
        if len(b) == 3:
            a = random.randint(0,len(b) - 1)
            if a == 0:
                b.pop(0)
                b.pop(0)
                d = b[0]
            elif a == 1:
                b.pop(0)
                b.pop(-1)
                d = b[0]
            else:
                b.pop(-1)
                b.pop(-1)
                d = b[0]  
            y.pop(0)
            y.insert(0,d)
    
    z = y.count("")

    while z != 0:
        y.remove("")
        z = y.count("")
        break

    c = str.strip(' '.join(y))
    
    print(c)