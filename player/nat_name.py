import random, csv
def nat_name():
        from team import team_nat, foreign_ratio 
        from lists import nat_list
        
        foreign = random.randint(1,int(foreign_ratio))
        
        if foreign != 1:
            player_nat = team_nat
        else: player_nat = random.choice(nat_list)
        
        if player_nat in nat_list:
               nat_index = nat_list.index(player_nat)

        ### name picker
        if foreign != 1:
            with open (f"player_names/{team_nat}.csv","r") as names_csv:
                names = csv.reader(names_csv)
                player_name = random.choice(list(names))
                player_name_str = ''.join(player_name)
        else:
            with open ("player_names/Belgium.csv","r") as names_csv:
                names = csv.reader(names_csv)
                player_name = random.choice(list(names))
                player_name_str = ''.join(player_name)

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