import csv
import random

def starting_eleven():
    from team import nat_list, team_nat, main_team_list, shirt_nr_1to11
    foreign = random.randint(1,8)
    age_weight = list(range(1,14))+list(range(12,0,-1)) 
    
    print("---Player---")

    ### nationality
    if foreign != 1:
        player_nat = team_nat
    else: player_nat = random.choice(nat_list)
    
    ### name picker
    if foreign != 1:
        with open (f"player_names/{team_nat}.csv","r") as names_csv:
            names = csv.reader(names_csv)
            player_name = random.choice(list(names))
            player_name_str = ''.join(player_name)
            print(f"Name: {player_name_str} ({team_nat})")
    else:
        with open ("player_names/Belgium.csv","r") as names_csv:
            names = csv.reader(names_csv)
            player_name = random.choice(list(names))
            player_name_str = ''.join(player_name)
            print(f"Name: {player_name_str} (Belgium)")

    print("Nationality: ", player_nat)

    ### age
    player_age = random.choices(range(16,41), weights = age_weight)
    print("Age: ", player_age[0])
    #print(age_weight)

    ### shirt number
    player_nr = shirt_nr_1to11[0]
    shirt_nr_1to11.remove(player_nr)
    print("Shirt#: ", player_nr)
    
##################################### registered position
    player_pos = main_team_list[0]
    main_team_list.remove(player_pos)
    print("Position: ", player_pos)
    #print(main_team_list)

    ### player type
    
    if player_pos == "GK":
        from player.pos_00_gk import gk
        gk()
    if player_pos == "CWP":
        from player.pos_02_cwp import cwp
        cwp()
    if player_pos == "CB":
        from player.pos_03_cb import cb
        cb()
    if player_pos == "SB":
        from player_types import sb
        sb()
    if player_pos == "DMF":
        from player_types import dmf
        dmf()
    if player_pos == "WB":
        from player_types import wb
        wb()
    if player_pos == "CMF":
        from player_types import cmf
        cmf()
    if player_pos == "SMF":
        from player_types import smf
        smf()
    if player_pos == "AMF":
        from player_types import amf
        amf()
    if player_pos == "FW":
        from player_types import fw
        fw()
    if player_pos == "SS":
        from player_types import ss
        ss()
    if player_pos == "CF":
        from player_types import cf
        cf()
    
    ### 2nd positions

    print()
    return

starting_eleven()
starting_eleven()
starting_eleven()
starting_eleven()
starting_eleven()
starting_eleven()
starting_eleven()
starting_eleven()
starting_eleven()
starting_eleven()
starting_eleven()