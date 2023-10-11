def starting_eleven():
    from team import main_team_list

    print("---SQUAD PLAYER---")
     
    ### registered position
    player_pos = main_team_list[0]
    main_team_list.remove(player_pos)

    ### player type
    from lists import csv_list

    if player_pos == "GK":
        from player.pos_00_gk import gk
        a = gk()
        csv_list.append(a)
    if player_pos == "CWP":
        from player.pos_02_cwp import cwp
        b = cwp()
        csv_list.append(b)
    if player_pos == "CB":
        from player.pos_03_cb import cb
        c = cb()
        csv_list.append(c)
    if player_pos == "SB":
        from player.pos_04_sb import sb
        d = sb()
        csv_list.append(d)
    if player_pos == "DMF":
        from player.pos_05_dmf import dmf
        e = dmf()
        csv_list.append(e)
    if player_pos == "WB":
        from player.pos_06_wb import wb
        f = wb()
        csv_list.append(f)
    if player_pos == "CMF":
        from player.pos_07_cmf import cmf
        g = cmf()
        csv_list.append(g)
    if player_pos == "SMF":
        from player.pos_08_smf import smf
        h = smf()
        csv_list.append(h)
    if player_pos == "AMF":
        from player.pos_09_amf import amf
        i = amf()
        csv_list.append(i)
    if player_pos == "FW":
        from player.pos_10_fw import fw
        j = fw()
        csv_list.append(j)
    if player_pos == "SS":
        from player.pos_11_ss import ss
        k = ss()
        csv_list.append(k)
    if player_pos == "CF":
        from player.pos_12_cf import cf
        l = cf()
        csv_list.append(l)
       
    print()
    
    return

def substitutes():                          
    from team import subs_list

    print("---SUBS---")
     
    ### registered position
    player_pos = subs_list[0]
    subs_list.remove(player_pos)

    ### player type
    from lists import csv_list

    if player_pos == "GK":
        from player.pos_00_gk import gk
        a = gk()
        csv_list.append(a)
    if player_pos == "CWP":
        from player.pos_02_cwp import cwp
        b = cwp()
        csv_list.append(b)
    if player_pos == "CB":
        from player.pos_03_cb import cb
        c = cb()
        csv_list.append(c)
    if player_pos == "SB":
        from player.pos_04_sb import sb
        d = sb()
        csv_list.append(d)
    if player_pos == "DMF":
        from player.pos_05_dmf import dmf
        e = dmf()
        csv_list.append(e)
    if player_pos == "WB":
        from player.pos_06_wb import wb
        f = wb()
        csv_list.append(f)
    if player_pos == "CMF":
        from player.pos_07_cmf import cmf
        g = cmf()
        csv_list.append(g)
    if player_pos == "SMF":
        from player.pos_08_smf import smf
        h = smf()
        csv_list.append(h)
    if player_pos == "AMF":
        from player.pos_09_amf import amf
        i = amf()
        csv_list.append(i)
    if player_pos == "FW":
        from player.pos_10_fw import fw
        j = fw()
        csv_list.append(j)
    if player_pos == "SS":
        from player.pos_11_ss import ss
        k = ss()
        csv_list.append(k)
    if player_pos == "CF":
        from player.pos_12_cf import cf
        l = cf()
        csv_list.append(l)
       
    print()
    
    return

from team import main_team_list, subs_list

while len(main_team_list) > 0:
    starting_eleven()

while len(subs_list) > 0:
    substitutes()

import csv

filename = "csv_export.csv"

from lists import csv_list

with open(filename, 'w', newline='') as csv_output:  
    csvwriter = csv.writer(csv_output) 
    csvwriter.writerows(csv_list)