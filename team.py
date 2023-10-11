import random
#import csv

print()
print("_-PES 6 Fantasy Team Genarator-_")
print()

player_qt = random.randint(25,30)
print("Players:", player_qt)

from lists import nat_list

print("Average skill:")
overall_mu = 6 #float(input("Input 0-8: "))
overall_sigma = 1

foreign_ratio =  5 #input("Input foreigner ratio 1 to ")

for team_nat in nat_list:
    team_nat = "Germany" #input("Country: ")
    if team_nat in nat_list:
        break
    
print()

## Tactic
defender_list = random.choices([3, 4, 5], weights= [2, 3, 1])
defender = defender_list[0]
if defender == 5:
    mid_var_list = random.choices([2, 3, 4], weights= [1, 4, 1])
    midfielder = mid_var_list[0]
elif defender == 4:
    midfielder = random.randint(3,5)
else:
    mid_var_list = random.choices([4, 5, 6], weights= [4, 4, 1])
    midfielder = mid_var_list[0]

attacker = 10 - defender - midfielder

print (f"Tactic: {defender}-{midfielder}-{attacker}")

## Defence
#cwp - sweeper
cwp = 0
if (defender == 3 or defender == 5) and random.randint(0,1) == 1:
    cwp = 1

#cb - center back
cb = 0
if (defender == 3 or defender == 5) and cwp == 1:
    cb = 2
elif (defender == 3 or defender == 5) and cwp == 0:
    cb = 3
else: cb = 2

#sb - side back
sb =  0
if defender == 3:
    sb = 0
else: sb = 2

## Midfield
#dmf - defending midfielder
dmf = 0
if cwp == 1:
    dmf = 0
elif midfielder == 2:
    dmf = 0
elif defender == 5:
    dmf = random.randint(0,1)
elif midfielder == 5 or midfielder == 3:
    dmf = random.randint(0,2)
else: dmf = random.randint(0,2)

#wb - wing back
wb = 0
if defender == 3:
    wb = 2
else: wb = 0

#cmf - central midfielder
cmf = 0
if cwp == 1:
    cmf = 2
elif defender == 3 and midfielder == 4 and dmf == 0:
    cmf = 2
elif defender == 3 and midfielder == 4 and dmf == 1:
    cmf = 1
elif defender == 3 and midfielder == 4 and dmf == 2:
    cmf = 0
elif dmf == 0 and (midfielder == 3 or midfielder == 5):
    cmf_rand_lst = random.choices([2, 3], weights= [2, 1])
    cmf = cmf_rand_lst[0]
elif dmf == 0:
    cmf = 2
elif dmf == 1 and midfielder == 4:
    cmf = random.randint(0,1)
elif dmf == 2 and (midfielder == 3 or midfielder == 5):
    cmf = random.randint(0,1)
else: cmf = random.randint(0,2)

#smf - side midfielder
smf = 0
if wb == 2:
    smf = 0    
elif midfielder == 3 and dmf > 0:
    smf = 0
elif midfielder - (dmf + cmf) > 1:
    smf = 2 #random.randint(0,2)
else: smf = 0

#amf - attacking midfielder
amf_var = dmf + wb + cmf + smf
amf = midfielder - amf_var
if amf < 0:
    amf = 0

#fw - forward winger
fw = 0
if defender == 5 and midfielder == 2:
    fw = random.randint(0,2)
elif smf == 1:
    fw = random.randint(0,1)
elif wb + smf == 0 and attacker == 3:
    fw = random.randint(1,2)
elif attacker == 2:
    fw_list = random.choices([0, 1], weights=[4,1])
    fw = fw_list[0]
else: fw = 0

#ss - second striker
ss = 0
if attacker == 1:
    ss_list = random.choices([0, 1], weights= [5, 1])
    ss = ss_list[0]
elif attacker == 2 and amf == 0:
    ss = random.randint(0,1)
elif attacker == 3 and fw == 0:
    ss_list = random.choices([2, 3], weights= [5, 1])
    ss = ss_list[0]
elif attacker - fw > 1:
    ss = 1
else: ss = 0

#cf - center forward
cf = attacker - fw - ss

#check
check = "No"
positions = cwp, cb, sb, dmf, wb, cmf, smf, amf, fw, ss, cf
count = sum(positions)
if 10 - count == 0:
    check = "Yes"

print(f"CWP:{cwp} CB:{cb} SB:{sb}")
print(f"DMF:{dmf} WB:{wb} CMF:{cmf} SMF:{smf} AMF:{amf}")
print(f"FW:{fw} SS:{ss} CF:{cf}")
print(f"OK?:{check}")

### List of starting eleven player's registered positions
main_team_list = ["GK"] * 1 + ["CWP"] * cwp + ["CB"] * cb + ["SB"] * sb + ["DMF"] * dmf + ["WB"] * wb + ["CMF"] * cmf + ["SMF"] * smf + ["AMF"] * amf + ["FW"] * fw + ["SS"] * ss + ["CF"] * cf

gk_squad = 3
cwp_squad = cwp * 2
cb_squad = cb * 2
sb_squad = sb * 2
dmf_squad = dmf * 2
wb_squad = wb * 2
cmf_squad = cmf * 2
smf_squad = smf * 2
amf_squad = amf * 2
fw_squad = fw * 2
ss_squad = ss * 2
cf_squad = cf * 2
    
overflow = sum([gk_squad,cwp_squad,cb_squad,sb_squad,dmf_squad,wb_squad,cmf_squad,smf_squad,amf_squad,fw_squad,ss_squad,cf_squad])

of_squad = player_qt - overflow

used_positions = []
if cwp > 0:
    used_positions.append("cwp")
if cb > 0:
    used_positions.append("cb")
if sb > 0:
    used_positions.append("sb")
if dmf > 0:
    used_positions.append("dmf")
if wb > 0:
    used_positions.append("wb")
if cmf > 0:
    used_positions.append("cmf")
if smf > 0:
    used_positions.append("smf")
if amf > 0:
    used_positions.append("amf")
if fw > 0:
    used_positions.append("fw")
if ss > 0:
    used_positions.append("ss")
if cf > 0:
    used_positions.append("cf")

#print()
#print(f"Used Positions: {used_positions}")
#print(f"Overflow players: {of_squad}")

of_player1 = 0
of_player2 = 0
of_player3 = 0
of_player4 = 0
of_player5 = 0
of_player6 = 0
of_player7 = 0

used_positions2=used_positions.copy()
used_positions2.append("gk")

if of_squad > 0 and len(used_positions) > 0:
    of_player1 = random.choice(used_positions)
    used_positions.remove(of_player1)
    of_squad = of_squad - 1
elif of_squad > 0:
    of_player1 = random.choice(used_positions2)
    used_positions2.remove(of_player1)
    of_squad = of_squad - 1
    
if of_squad > 0 and len(used_positions) > 0:
    of_player2 = random.choice(used_positions)
    used_positions.remove(of_player2)
    of_squad = of_squad - 1
elif of_squad > 0:
    of_player2 = random.choice(used_positions2)
    used_positions2.remove(of_player2)
    of_squad = of_squad - 1

if of_squad > 0 and len(used_positions) > 0:
    of_player3 = random.choice(used_positions)
    used_positions.remove(of_player3)
    of_squad = of_squad - 1
elif of_squad > 0:
    of_player3 = random.choice(used_positions2)
    used_positions2.remove(of_player3)
    of_squad = of_squad - 1

if of_squad > 0 and len(used_positions) > 0:
    of_player4 = random.choice(used_positions)
    used_positions.remove(of_player4)
    of_squad = of_squad - 1
elif of_squad > 0:
    of_player4 = random.choice(used_positions2)
    used_positions2.remove(of_player4)
    of_squad = of_squad - 1

if of_squad > 0 and len(used_positions) > 0:
    of_player5 = random.choice(used_positions)
    used_positions.remove(of_player5)
    of_squad = of_squad - 1
elif of_squad > 0:
    of_player5 = random.choice(used_positions2)
    used_positions2.remove(of_player5)
    of_squad = of_squad - 1

if of_squad > 0 and len(used_positions) > 0:
    of_player6 = random.choice(used_positions)
    used_positions.remove(of_player6)
    of_squad = of_squad - 1
elif of_squad > 0:
    of_player6 = random.choice(used_positions2)
    used_positions2.remove(of_player6)
    of_squad = of_squad - 1

if of_squad > 0 and len(used_positions) > 0:
    of_player7 = random.choice(used_positions)
    used_positions.remove(of_player7)
    of_squad = of_squad - 1
elif of_squad > 0:
    of_player7 = random.choice(used_positions2)
    used_positions2.remove(of_player7)
    of_squad = of_squad - 1

#print(used_positions)
overflow_list = []
if of_player1 != 0:
    overflow_list.append(of_player1)
if of_player2 != 0:
    overflow_list.append(of_player2)
if of_player3 != 0:
    overflow_list.append(of_player3)
if of_player4 != 0:
    overflow_list.append(of_player4)
if of_player5 != 0:
    overflow_list.append(of_player5)
if of_player6 != 0:
    overflow_list.append(of_player6)
if of_player7 != 0:
    overflow_list.append(of_player7)

#print(f"Overflow positions: {overflow_list}")
print()
print("---Squad---")
gk_squad = gk_squad + overflow_list.count("gk")
print(f" GK:    {gk_squad}")
cwp_squad = cwp_squad + overflow_list.count("cwp")
print(f"CWP:    {cwp_squad}")
cb_squad = cb_squad + overflow_list.count("cb")
print(f" CB:    {cb_squad}")
sb_squad = sb_squad + overflow_list.count("sb")
print(f" SB:    {sb_squad}")
dmf_squad = dmf_squad + overflow_list.count("dmf")
print(f"DMF:    {dmf_squad}")
wb_squad = wb_squad + overflow_list.count("wb")
print(f" WB:    {wb_squad}")
cmf_squad = cmf_squad + overflow_list.count("cmf")
print(f"CMF:    {cmf_squad}")
smf_squad = smf_squad + overflow_list.count("smf")
print(f"SMF:    {smf_squad}")
amf_squad = amf_squad + overflow_list.count("amf")
print(f"AMF:    {amf_squad}")
fw_squad = fw_squad + overflow_list.count("fw")
print(f" FW:    {fw_squad}")
ss_squad = ss_squad + overflow_list.count("ss")
print(f" SS:    {ss_squad}")
cf_squad = cf_squad + overflow_list.count("cf")
print(f" CF:    {cf_squad}")
print()

###
#print(main_team_list)

### List of all players registered positions
squad_list = ["GK"] * gk_squad + ["CWP"] * cwp_squad + ["CB"] * cb_squad + ["SB"] * sb_squad + ["DMF"] * dmf_squad + ["WB"] * wb_squad + ["CMF"] * cmf_squad + ["SMF"] * smf_squad + ["AMF"] * amf_squad + ["FW"] * fw_squad + ["SS"] * ss_squad + ["CF"] * cf_squad
#print(squad_str_list)

### List of non starting 11 registered position 
subs_list = ["GK"] * (gk_squad-1) + ["CWP"] * (cwp_squad-cwp) + ["CB"] * (cb_squad-cb) + ["SB"] * (sb_squad-sb) + ["DMF"] * (dmf_squad-dmf) + ["WB"] * (wb_squad-wb) + ["CMF"] * (cmf_squad-cmf) + ["SMF"] * (smf_squad-smf) + ["AMF"] * (amf_squad-amf) + ["FW"] * (fw_squad-fw) + ["SS"] * (ss_squad-ss) + ["CF"] * (cf_squad-cf)
#print(subs_list)

import players