import random

def fw():
    
    ### NAME AND NATIONALITY ###
    from player.nat_name import nat_name

    def number():
        from lists import shirt_nr
        if 7 in shirt_nr:
            number = 7
            shirt_nr.remove(7)
            shirt_nr.sort()
        elif 11 in shirt_nr:
            number = 11
            shirt_nr.remove(11)
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
    
    def role():
        from lists import types_fw, types_amf, types_ss, sub_roles_fw, sub_roles_amf, sub_roles_ss
        from team import main_team_list

        if len(main_team_list) > 0:
            if "enganche" not in types_amf and "advanced playmaker" in types_fw:
                    types_fw.remove("advanced playmaker")

            role = random.choice(types_fw)

            if role == "winger":
                types_fw.append("winger")
            if role == "inverted winger":
                types_fw.append("inverted winger")
            if role == "inside forward":
                types_fw.append("inside forward")
            
            ### variety
            if role in types_fw:
                types_fw.remove(role)
            if role in types_ss:
                types_ss.remove(role)
            
            return role
        else:
            if "enganche" not in sub_roles_amf and "advanced playmaker" in sub_roles_fw:
                    sub_roles_fw.remove("advanced playmaker")

            role = random.choice(sub_roles_fw)

            if role == "winger":
                sub_roles_fw.append("winger")
            if role == "inverted winger":
                sub_roles_fw.append("inverted winger")
            if role == "inside forward":
                sub_roles_fw.append("inside forward")
            
            ### variety
            if role in sub_roles_fw:
                sub_roles_fw.remove(role)
            if role in sub_roles_ss:
                sub_roles_ss.remove(role)
            
            return role
    player_role = role()
        
    def side_foot():
        ### main side
        from lists import smf_side_list, sub_smf_side_list
        from team import main_team_list
        
        if len(main_team_list) > 0:
            if "L" in smf_side_list:   
                smf_side_list.remove("R")
                smf_side_rnd_list = random.choices(smf_side_list, weights= [4,1])
                side = smf_side_rnd_list[0]
                smf_side_list.append("R")
                smf_side_list.remove("L")
            else:
                smf_side_rnd_list = random.choices(smf_side_list, weights= [4,1])
                side = smf_side_rnd_list[0]
        else:
            if "L" in sub_smf_side_list:   
                sub_smf_side_list.remove("R")
                smf_side_rnd_list = random.choices(sub_smf_side_list, weights= [4,1])
                side = smf_side_rnd_list[0]
                sub_smf_side_list.append("R")
                sub_smf_side_list.remove("L")
            else:
                smf_side_rnd_list = random.choices(sub_smf_side_list, weights= [4,1])
                side = smf_side_rnd_list[0]
    
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
        if side == "inside forward" or side == "inverted winger":
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

    if player_role == "wide target man": 
        mu = 185
        sigma = 5
        height_min = 180
        height_max = 202
        bmi_mu = 23.5    
    else:
        mu = 178
        sigma = 5
        height_min = 160
        height_max = 202
        bmi_mu = 23.0

    def ID_func():
        from lists import x
        x[0] += 1
        return str(x[0])

    ID = ID_func()
    CALLNAME = "0"
    NATIONALITY, NAME, PLAYER_NAT = nat_name()
    SHIRT_NAME = NAME.upper()
    AGE = age(age_mu,age_sigma)
    POS_DEFAULT = "10"
    GK = "0"
    CWP = "0"
    CB = "0"
    SB = "0"
    DMF = "0"
    WB = "0"
    CMF = "0"
    SMF = "0"
    AMF = "0"
    WF = "1"
    SS = "0"
    CF = "0"
    HEIGHT, WEIGHT, bmi = height_weight(mu,sigma,height_min,height_max,bmi_mu)
    FAV_SIDE, FOOT = side_foot()
    CONSISTENCY = str(0)
    CONDITION = str(0)
    INJURY_TOLERANCE = str(0)
    WEAK_FOOT_ACCURACY = str(0)
    WEAK_FOOT_FREQUENCY = str(0)
    ATTACK = str(0)
    DEFENCE = str(0)
    BALANCE = str(0)
    STAMINA = str(0)
    TOP_SPEED = str(0)
    ACCELERATION = str(0)
    RESPONSE = str(0)
    AGILITY = str(0)
    DRIBBLE_ACCURACY = str(0)
    DRIBBLE_SPEED = str(0)
    SHORT_PASS_ACCURACY = str(0)
    SHORT_PASS_SPEED = str(0)
    LONG_PASS_ACCURACY = str(0)
    LONG_PASS_SPEED = str(0)
    SHOT_ACCURACY = str(0)
    SHOT_POWER = str(0)
    SHOT_TECHNIQUE = str(0)
    FREE_KICK_ACCURACY = str(0)
    CURLING = str(0)
    HEADER = str(0)
    JUMP = str(0)
    TECHNIQUE = str(0)
    AGGRESSION = str(0)
    MENTALITY = str(0)
    KEEPER_SKILLS = str(0)
    TEAM_WORK = str(0)
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
    GOAL_CELEBRATION_1 = str(0)
    GOAL_CELEBRATION_2 = str(0)
    DRIBBLE = str(0)
    FREE_KICK = str(0)
    PENALTY = str(0)
    DROP = str(0)
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
    INTERNATIONAL_NUMBER = str(0)
    CLASSIC_NUMBER = str(0)
    CLUB_TEAM = str(0)
    CLUB_NUMBER = str(number())

    rows = [ID,NAME,SHIRT_NAME,CALLNAME,NATIONALITY,AGE,POS_DEFAULT,GK,CWP,CB,SB,DMF,WB,CMF,SMF,AMF,WF,SS,CF,WEIGHT,HEIGHT,FOOT,FAV_SIDE,CONSISTENCY,CONDITION,INJURY_TOLERANCE,WEAK_FOOT_ACCURACY,WEAK_FOOT_FREQUENCY,ATTACK,DEFENCE,BALANCE,STAMINA,TOP_SPEED,ACCELERATION,RESPONSE,AGILITY,DRIBBLE_ACCURACY,DRIBBLE_SPEED,SHORT_PASS_ACCURACY,SHORT_PASS_SPEED,LONG_PASS_ACCURACY,LONG_PASS_SPEED,SHOT_ACCURACY,SHOT_POWER,SHOT_TECHNIQUE,FREE_KICK_ACCURACY,CURLING,HEADER,JUMP,TECHNIQUE,AGGRESSION,MENTALITY,KEEPER_SKILLS,TEAM_WORK,DRIBBLING,TACTICAL_DRIBBLE,POSITIONING,REACTION,PLAYMAKING,PASSING,SCORING,ONE_ONE_SCORE,POST_PLAYER,LINES,MIDDLE_SHOOTING,SIDE,CENTRE,PENALTIES,ONE_TOUCH_PASS,OUTSIDE,MARKING,SLIDING,COVERING,D_LINE_CONTROL,PENALTY_STOPPER,ONE_ON_ONE_STOPPER,LONG_THROW,GOAL_CELEBRATION_1,GOAL_CELEBRATION_2,DRIBBLE,FREE_KICK,PENALTY,DROP,SKIN_COLOR,FACE_TYPE,PRESET_FACE_NUMBER,HEAD_WIDTH,NECK_LENGTH,NECK_WIDTH,SHOULDER_HEIGHT,SHOULDER_WIDTH,CHEST_MEASUREMENT,WAIST_CIRCUMFERENCE,ARM_CIRCUMFERENCE,LEG_CIRCUMFERENCE,CALF_CIRCUMFERENCE,LEG_LENGTH,WRISTBAND,WRISTBAND_COLOR,INTERNATIONAL_NUMBER,CLASSIC_NUMBER,CLUB_TEAM,CLUB_NUMBER]

    print("Position: FW   #",CLUB_NUMBER)
    print(f"Name: {NAME} ({PLAYER_NAT}) [{NATIONALITY}]")
    print("Role: ",player_role)
    print(f"Height: {float(HEIGHT)/100.0} m")
    print(f"Weight: {WEIGHT} kg")
    print("Age: ",AGE)
    print(f"Foot: {FOOT}    Side: {FAV_SIDE}")

    return rows