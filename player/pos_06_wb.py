import random

def wb():
    ### NAME AND NATIONALITY ###
    from player.nat_name import nat_name, shirt_name

    def number():
        from lists import shirt_nr
        from team import dmf
        
        if dmf > 0 and 6 in shirt_nr:
            shirt_nr.remove(6)
            number = shirt_nr[0]
            shirt_nr.append(6)
            shirt_nr.sort()
        else:
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
        from team import dmf, cmf, main_team_list
        from lists import types_wb, sub_roles_wb

        if len(main_team_list) > 0:
            if dmf + cmf > 2 and "wb_iwb" in types_wb:
                types_wb.remove("wb_iwb")
                role = random.choice(types_wb)
            else:
                role = random.choice(types_wb)

            if role == "wb_iwb":
                if "wb_iwb" in types_wb:
                    types_wb.remove("wb_iwb")
            return role
        else:
            role = random.choice(sub_roles_wb)
            #sub_roles_wb.remove(role)
            return role
    player_role = role()
     
    def side_foot():
        ### main side
        from lists import wb_side_list, sub_wb_side_list
        from team import main_team_list
        
        if len(main_team_list) > 0:
            if "L" in wb_side_list:   
                wb_side_list.remove("R")
                wb_side_rnd_list = random.choices(wb_side_list, weights= [4,1])
                side = wb_side_rnd_list[0]
                wb_side_list.append("R")
                wb_side_list.remove("L")
            else:
                wb_side_rnd_list = random.choices(wb_side_list, weights= [4,1])
                side = wb_side_rnd_list[0]
        else:
            if "L" in sub_wb_side_list:   
                sub_wb_side_list.remove("R")
                wb_side_rnd_list = random.choices(sub_wb_side_list, weights= [4,1])
                side = wb_side_rnd_list[0]
                sub_wb_side_list.append("R")
                sub_wb_side_list.remove("L")
            else:
                wb_side_rnd_list = random.choices(sub_wb_side_list, weights= [4,1])
                side = wb_side_rnd_list[0]
        
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
        if player_role == "wb_iwb":
            if side == "L":
                foot = "R"
            if side == "R":
                foot = "L"
            if side == "B":
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
    from player.skill_00_generator import skill
    ATTACK = skill(player_role,0)
    DEFENCE = skill(player_role,1)
    BALANCE = skill(player_role,2) + str_fac
    STAMINA = skill(player_role,3)
    TOP_SPEED = skill(player_role,4)
    ACCELERATION = skill(player_role,5)
    RESPONSE = skill(player_role,6)
    AGILITY = skill(player_role,7)
    DRIBBLE_ACCURACY = skill(player_role,8)
    DRIBBLE_SPEED = skill(player_role,9)
    SHORT_PASS_ACCURACY = skill(player_role,10)
    SHORT_PASS_SPEED = skill(player_role,11)
    LONG_PASS_ACCURACY = skill(player_role,12)
    LONG_PASS_SPEED = skill(player_role,13)
    SHOT_ACCURACY = skill(player_role,14)
    SHOT_POWER = skill(player_role,15)
    SHOT_TECHNIQUE = skill(player_role,16)
    FREE_KICK_ACCURACY = skill(player_role,17)
    CURLING = skill(player_role,18)
    HEADER = skill(player_role,19)
    JUMP = skill(player_role,20)
    TECHNIQUE = skill(player_role,21)
    AGGRESSION = skill(player_role,22)
    MENTALITY = skill(player_role,23)
    KEEPER_SKILLS = skill(player_role,24)
    TEAM_WORK = skill(player_role,25)

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
        roles = ["wb_wb", "wb_cwb", "wb_iwb"]
        x = roles.index(player_role)
        GK =  [0, 0, 0]
        CWP = [0, 0, 0]
        CB =  [0, 0, 0]
        SB =  [choices(1,2), choices(1,3), choices(1,1)]
        DMF = [0, 0, choices(1,1)]
        WB =  [1, 1, 1]
        CMF = [0, 0, choices(2,1)]
        SMF = [choices(3,1), choices(2,1), choices(4,1)]
        AMF = [0, 0, 0]
        FW =  [0, choices(6,1), 0]
        SS =  [0, 0, 0]
        CF =  [0, 0, 0]
        return GK[x], CWP[x], CB[x], SB[x], DMF[x], WB[x], CMF[x], SMF[x], AMF[x], FW[x], SS[x], CF[x]
    
    GK, CWP, CB, SB, DMF, WB, CMF, SMF, AMF, FW, SS, CF = second_pos()
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