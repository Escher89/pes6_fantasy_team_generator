import random, csv

def nat_name():
    from team import team_nat, foreign_ratio 
    from lists import nat_list
    
    foreign = random.randint(1,int(foreign_ratio))
    
    if foreign != 1:
        player_nat = team_nat
    else: player_nat = "Belgium" #random.choice(nat_list)
    
    if player_nat in nat_list:
            nat_index = nat_list.index(player_nat)
    
    def name_joiner(y):
    ### Name    
        if "/" in y[2]:
            b = y[2].split("/")        
            a = random.randint(0,len(b) - 1)
            d = b[a]
            y.pop(2)
            y.append(d)

    ### 2nd prefix
        if "/" in y[1]:
            b = y[1].split("/")        
            a = random.randint(0,len(b) - 1)
            d = b[a]
            y.pop(1)
            y.insert(1,d)

    ### 1st prefix
        if "/" in y[0]:
            b = y[0].split("/")        
            a = random.randint(0,len(b) - 1)
            d = b[a]
            y.pop(0)
            y.insert(0,d)
        
        z = y.count("")

        while z != 0:
            y.remove("")
            z = y.count("")
            break
        player_name_str = str.strip(' '.join(y))
        return player_name_str
    
    ### name picker
    if foreign != 1:
        with open(f"player_names/{team_nat}.csv","r") as names_csv:  
            csvFile = csv.reader(names_csv)  
            rows = list(csvFile)    
            
            x = random.randint(0,len(rows) - 1)
            y = rows[x]
        player_name_str = name_joiner(y)
        
    else:   
        with open(f"player_names/Belgium.csv","r") as names_csv:  
            csvFile = csv.reader(names_csv)  
            rows = list(csvFile)    
            
            x = random.randint(0,len(rows) - 1)
            y = rows[x]
        player_name_str = name_joiner(y)

    return [nat_index, player_name_str, player_nat]

def shirt_name(name):
    if len(name) <= 4:
        split = list(name)
        split.insert(1," ")
        split.insert(1," ")
        split.insert(1," ")
        split.insert(5," ")
        split.insert(5," ")
        split.insert(5," ")
        split.insert(9," ")
        split.insert(9," ")
        split.insert(9," ")
        x = ''.join(split)
    elif len(name) == 5:
        split = list(name)
        split.insert(1," ")
        split.insert(1," ")
        split.insert(4," ")
        split.insert(4," ")
        split.insert(7," ")
        split.insert(7," ")
        split.insert(10," ")
        split.insert(10," ")
        x = ''.join(split)
    elif len(name) == 6:
        split = list(name)
        split.insert(1," ")
        split.insert(3," ")
        split.insert(5," ")
        split.insert(7," ")
        split.insert(9," ")
        x = ''.join(split)
    elif len(name) == 7:
        split = list(name)
        split.insert(1," ")
        split.insert(3," ")
        split.insert(5," ")
        split.insert(7," ")
        split.insert(9," ")
        split.insert(11," ")
        x = ''.join(split)
    else:
        x = name
    return x