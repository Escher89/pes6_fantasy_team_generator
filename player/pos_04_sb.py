import random

def sb():
    position = "sb"
    ### NAME AND NATIONALITY ###
    from player.nat_name import nat_name, shirt_name

    def number():
        from lists import shirt_nr
        
        number = shirt_nr[0]
        shirt_nr.pop(0)

        return number

    ### AGE ###
    from player.age import age
    from team import main_team_list
    if len(main_team_list) > 0:
        age_mu = 27
        age_sigma = 2.5
    else:
        age_mu = 27
        age_sigma = 5
    
    AGE = age(age_mu,age_sigma)
    
    def role():       
        from team import defender, main_team_list
        roles = ["full back", "wing back", "no non-sense full back", "complete wing back", "inverted wing back"]
        
        if len(main_team_list) > 0:
            if defender == 5:
                roles.remove("full back") 
                roles.remove("no non-sense full back")
                roles.remove("inverted wing back")
                role = random.choice(roles)
            else:
                role = random.choice(roles)
            return role
        else:
            role = random.choice(roles)
            return role
        
    player_role = role()
        
    def side_foot():
        ### main side
        from lists import sb_side_list, sub_sb_side_list
        from team import main_team_list
        
        if len(main_team_list) > 0:
            if "L" in sb_side_list:   
                sb_side_list.remove("R")
                sb_side_rnd_list = random.choices(sb_side_list, weights= [4,1])
                side = sb_side_rnd_list[0]
                sb_side_list.append("R")
                sb_side_list.remove("L")
            else:
                sb_side_rnd_list = random.choices(sb_side_list, weights= [4,1])
                side = sb_side_rnd_list[0]
        else:
            if "L" in sub_sb_side_list:   
                sub_sb_side_list.remove("R")
                sb_side_rnd_list = random.choices(sub_sb_side_list, weights= [4,1])
                side = sb_side_rnd_list[0]
                sub_sb_side_list.append("R")
                sub_sb_side_list.remove("L")
            else:
                sb_side_rnd_list = random.choices(sub_sb_side_list, weights= [4,1])
                side = sb_side_rnd_list[0]

        ### main foot
        foot_list = ["L", "R"]
        
        if side == "L":
            lst = random.choices(foot_list, weights={8,1})
            foot = lst[0]
        if side == "R":
            lst = random.choices(foot_list, weights=[1,8])
            foot = lst[0]
        if side == "B":
            lst = random.choices(foot_list, weights=[1,4])
            foot = lst[0]
        
        ### special rule for inverted roles
        if player_role == "inverted wing back":
            if side == "L":
                foot = "R"
            elif side == "R":
                foot = "L"
            else:
                lst = random.choices(foot_list, weights=[1,4])
                foot = lst[0]

        return [side, foot] 

    ### HEIGHT AND WEIGHT ###
    from player.height_weight import height_weight

    mu = 178
    sigma = 5
    height_min = 160
    height_max = 202
    bmi_mu = 23.0

    HEIGHT, WEIGHT, bmi = height_weight(mu,sigma,height_min,height_max,bmi_mu)

    def ID_func():
        from lists import x
        x[0] += 1
        return str(x[0])
    
    ### SUB SKILLS ### 
    from player.skill_00_randomize import strength, technique
    str_fac = strength(bmi)
    tec_fac = technique()

    from player.skill_00_randomize import overall
    points = overall(AGE) 

    ### SKILLS ###
    from player.skill_01_attack import skill_role_sb, skill_pos
    ATTACK = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_02_defence import skill_role_sb, skill_pos
    DEFENCE = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_03_balance import skill_role_sb, skill_pos
    BALANCE = (skill_role_sb[player_role] + skill_pos[position]) / 2  + str_fac

    from player.skill_04_stamina import skill_role_sb, skill_pos
    STAMINA = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_05_top_speed import skill_role_sb, skill_pos
    TOP_SPEED = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_06_acceleration import skill_role_sb, skill_pos
    ACCELERATION = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_07_response import skill_role_sb, skill_pos
    RESPONSE = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_08_agility import skill_role_sb, skill_pos
    AGILITY = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_09_dribble_acc import skill_role_sb, skill_pos
    DRIBBLE_ACCURACY = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_10_dribble_spd import skill_role_sb, skill_pos
    DRIBBLE_SPEED = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_11_short_pass_acc import skill_role_sb, skill_pos
    SHORT_PASS_ACCURACY = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_12_short_pass_spd import skill_role_sb, skill_pos
    SHORT_PASS_SPEED = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_13_long_pass_acc import skill_role_sb, skill_pos
    LONG_PASS_ACCURACY = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_14_long_pass_spd import skill_role_sb, skill_pos
    LONG_PASS_SPEED = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_15_shot_acc import skill_role_sb, skill_pos
    SHOT_ACCURACY = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_16_shot_power import skill_role_sb, skill_pos
    SHOT_POWER = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_17_shot_tech import skill_role_sb, skill_pos
    SHOT_TECHNIQUE = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_18_free_kick_acc import skill_role_sb, skill_pos
    FREE_KICK_ACCURACY = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_19_curling import skill_role_sb, skill_pos
    CURLING = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_20_header import skill_role_sb, skill_pos
    HEADER = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_21_jump import skill_role_sb, skill_pos
    JUMP = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_22_technique import skill_role_sb, skill_pos
    TECHNIQUE = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_23_aggression import skill_role_sb, skill_pos
    AGGRESSION = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_24_mentality import skill_role_sb, skill_pos
    MENTALITY = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_25_keeper_skills import skill_role_sb, skill_pos
    KEEPER_SKILLS = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_26_team_work import skill_role_sb, skill_pos
    TEAM_WORK = (skill_role_sb[player_role] + skill_pos[position]) / 2

    from player.skill_00_generator import skills
    ATT,DEF,BAL,STA,TOP,ACC,RES,AGI,DAC,DSP,SPA,SPS,LPA,LPS,SAC,SPO,STE,FKA,CUR,HEA,JUM,TEC,AGG,MEN,KEE,TEA = skills(points,ATTACK,DEFENCE,BALANCE,STAMINA,
                                                                                                                    TOP_SPEED,ACCELERATION,RESPONSE,
                                                                                                                    AGILITY,DRIBBLE_ACCURACY,DRIBBLE_SPEED,
                                                                                                                    SHORT_PASS_ACCURACY,SHORT_PASS_SPEED,
                                                                                                                    LONG_PASS_ACCURACY,LONG_PASS_SPEED,
                                                                                                                    SHOT_ACCURACY,SHOT_POWER,SHOT_TECHNIQUE,
                                                                                                                    FREE_KICK_ACCURACY,CURLING,HEADER,
                                                                                                                    JUMP,TECHNIQUE,AGGRESSION,MENTALITY,
                                                                                                                    KEEPER_SKILLS,TEAM_WORK)

    ### 2nd positions ###
    def second_pos():
        def choices(y,z):
            x = random.choices([0,1], weights=[y,z])[0]
            return x
        roles = ["full back", "wing back", "no non-sense full back", "complete wing back", "inverted wing back"]
        x = roles.index(player_role)
        GK = [0, 0, 0, 0, 0]
        CWP = [0, 0, 0, 0, 0]
        CB = [choices(1,1), 0, choices(1,2), 0, choices(4,1)]
        SB = [1, 1, 1, 1, 1]
        DMF = [choices(1,8), 0, 0, 0, choices(1,1)]
        WB = [0, choices(1,2), 0, choices(1,3), choices(1,2)]
        CMF = [0, 0, 0, 0, choices(2,1)]
        SMF = [0, 0, 0, choices(2,1), 0]
        AMF = [0, 0, 0, 0, 0]
        FW = [0, 0, 0, choices(4,1), 0]
        SS = [0, 0, 0, 0, 0]
        CF = [0, 0, 0, 0, 0]
        return GK[x], CWP[x], CB[x], SB[x], DMF[x], WB[x], CMF[x], SMF[x], AMF[x], FW[x], SS[x], CF[x]
    
    GK, CWP, CB, SB, DMF, WB, CMF, SMF, AMF, FW, SS, CF = second_pos()
    from player.second_pos_str import second_pos_str
    second_positions = second_pos_str(GK,CWP,CB,SB,DMF,WB,CMF,SMF,AMF,FW,SS,CF)

    from player.second_pos_str import second_pos_str
    second_positions = second_pos_str(GK,CWP,CB,SB,DMF,WB,CMF,SMF,AMF,FW,SS,CF)


    def ID_func():
        from lists import x
        x[0] += 1
        return str(x[0])

    ID = ID_func()
    CALLNAME = "0"
    NATIONALITY, NAME, PLAYER_NAT = nat_name()
    SHIRT_NAME = shirt_name(NAME)
    
    from player.second_pos_str import pos_rand, final_position
    pos_list = pos_rand(GK, CWP, CB, SB, DMF, WB, CMF, SMF, AMF, FW, SS, CF)
    POS_DEFAULT = random.choice(pos_list)
    
    FAV_SIDE, FOOT = side_foot()
    CONSISTENCY = str(0)
    CONDITION = str(0)
    INJURY_TOLERANCE = str(0)
    WEAK_FOOT_ACCURACY = str(0)
    WEAK_FOOT_FREQUENCY = str(0)
    
    ### ABILITYS ###
    DRIBBLING = str(0)
    TACTICAL_DRIBBLE = str(0)
    POSITIONING = str(0)
    REACTION = str(0)
    PLAYMAKING = str(0)
    PASSING = str(0)
    SCORING = str(0)
    ONE_ONE_SCORE = str(0)
    POST_PLAYER = str(0)
    LINES = str(0)
    MIDDLE_SHOOTING = str(0)
    SIDE = str(0)
    CENTRE = str(0)
    PENALTIES = str(0)
    ONE_TOUCH_PASS = str(0)
    OUTSIDE = str(0)
    MARKING = str(0)
    SLIDING = str(0)
    COVERING = str(0)
    D_LINE_CONTROL = str(0)
    PENALTY_STOPPER = str(0)
    ONE_ON_ONE_STOPPER = str(0)
    LONG_THROW = str(0)

    ### MOVEMENT ###
    GOAL_CELEBRATION_1 = str(0)
    GOAL_CELEBRATION_2 = str(0)
    DRIBBLE = str(0)
    FREE_KICK = str(0)
    PENALTY = str(0)
    DROP = str(0)

    ### APPEARANCE ###
    SKIN_COLOR = str(0)
    FACE_TYPE = str(0)
    PRESET_FACE_NUMBER = str(0)
    HEAD_WIDTH = str(0)
    NECK_LENGTH = str(0)
    NECK_WIDTH = str(0)
    SHOULDER_HEIGHT = str(0)
    SHOULDER_WIDTH = str(0)
    CHEST_MEASUREMENT = str(0)
    WAIST_CIRCUMFERENCE = str(0)
    ARM_CIRCUMFERENCE =	str(0)
    LEG_CIRCUMFERENCE = str(0)
    CALF_CIRCUMFERENCE = str(0)
    LEG_LENGTH = str(0)
    WRISTBAND = str(0)
    WRISTBAND_COLOR = str(0)
    
    ### TEAM & NUMBERS ###
    INTERNATIONAL_NUMBER = str(0)
    CLASSIC_NUMBER = str(0)
    CLUB_TEAM = str(0)
    CLUB_NUMBER = str(number())

    rows = [ID,NAME,SHIRT_NAME,CALLNAME,NATIONALITY,AGE,POS_DEFAULT,GK,CWP,CB,SB,DMF,WB,CMF,SMF,AMF,FW,SS,CF,
            WEIGHT,HEIGHT,FOOT,FAV_SIDE,CONSISTENCY,CONDITION,INJURY_TOLERANCE,WEAK_FOOT_ACCURACY,WEAK_FOOT_FREQUENCY,
            ATT,DEF,BAL,STA,TOP,ACC,RES,AGI,DAC,DSP,SPA,SPS,LPA,LPS,SAC,SPO,STE,FKA,CUR,HEA,JUM,TEC,AGG,MEN,KEE,TEA,
            DRIBBLING,TACTICAL_DRIBBLE,POSITIONING,REACTION,PLAYMAKING,PASSING,SCORING,ONE_ONE_SCORE,POST_PLAYER,LINES,MIDDLE_SHOOTING,SIDE,CENTRE,PENALTIES,ONE_TOUCH_PASS,OUTSIDE,MARKING,SLIDING,COVERING,D_LINE_CONTROL,PENALTY_STOPPER,ONE_ON_ONE_STOPPER,LONG_THROW,
            GOAL_CELEBRATION_1,GOAL_CELEBRATION_2,DRIBBLE,FREE_KICK,PENALTY,DROP,
            SKIN_COLOR,FACE_TYPE,PRESET_FACE_NUMBER,HEAD_WIDTH,NECK_LENGTH,NECK_WIDTH,SHOULDER_HEIGHT,SHOULDER_WIDTH,CHEST_MEASUREMENT,WAIST_CIRCUMFERENCE,ARM_CIRCUMFERENCE,LEG_CIRCUMFERENCE,CALF_CIRCUMFERENCE,LEG_LENGTH,WRISTBAND,WRISTBAND_COLOR,
            INTERNATIONAL_NUMBER,CLASSIC_NUMBER,CLUB_TEAM,CLUB_NUMBER]

    print(f"Position: {final_position(POS_DEFAULT)}   #",CLUB_NUMBER, second_positions)
    print(f"Name: {NAME} ({PLAYER_NAT}) [{NATIONALITY}]")
    print("Role: ",player_role)
    print(f"Height: {float(HEIGHT)/100.0:.2f} m")
    print(f"Weight: {WEIGHT} kg")
    print("Age: ",AGE)
    print(f"Foot: {FOOT}    Side: {FAV_SIDE}")
    print("Attack: ", ATT)
    print("Defence: ", DEF)
    print("Balance: ", BAL)
    print("Stamina: ", STA)
    print("Top Speed: ", TOP)
    print("Acceleration: ", ACC)
    print("Response: ", RES)
    print("Agility: ", AGI)
    print("Dribble Accuracy: ", DAC)
    print("Dribble Speed: ", DSP)
    print("Short Pass Accuracy: ", SPA)
    print("Short Pass Speed: ", SPS)
    print("Long Pass Accuracy: ", LPA)
    print("Long Pass Speed: ", LPS)
    print("Shot Accuracy: ", SAC)
    print("Shot Power: ", SPO)
    print("Shot Technique: ", STE)
    print("Free Kick Accuracy: ", FKA)
    print("Curling: ", CUR)
    print("Header: ", HEA)
    print("Jump: ", JUM)
    print("Technique: ", TEC)
    print("Aggression: ", AGG)
    print("Mentality: ", MEN)
    print("Keeper Skills: ", KEE)
    print("Teamwork: ", TEA)
    return rows