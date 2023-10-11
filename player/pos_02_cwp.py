import random

def cwp():
    position = "cwp"
    ### NAME AND NATIONALITY ###
    from player.nat_name import nat_name

    def number():
        from lists import shirt_nr
        if 5 in shirt_nr:
            number = 5
            shirt_nr.remove(5)
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
        role = "sweeper"
        return role
    player_role = role()
           
    ### SIDE AND FOOR FOR CENTER POSITIONS ###
    from player.center_side_foot import center_side_foot
 
    ### HEIGHT AND WEIGHT ###
    from player.height_weight import height_weight

    mu = 185
    sigma = 5
    height_min = 175
    height_max = 202
    bmi_mu = 23.5

    
    ### SKILLS ###
    def factor():
        from player.skill_00_randomize import overall, starting_eleven_bonus, age_factor
        fac = overall() + starting_eleven_bonus() + age_factor(AGE)
        return fac    

    def attack_01():
        from player.skill_01_attack import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def defence_02():
        from player.skill_02_defence import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def balance_03():
        from player.skill_03_balance import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def stamina_04():
        from player.skill_04_stamina import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def top_speed_05():
        from player.skill_05_top_speed import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def acceleration_06():
        from player.skill_06_acceleration import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def response_07():
        from player.skill_07_response import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def agility_08():
        from player.skill_08_agility import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def dribble_acc_09():
        from player.skill_09_dribble_acc import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def dribble_spd_10():
        from player.skill_10_dribble_spd import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def short_pass_acc_11():
        from player.skill_11_short_pass_acc import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def short_pass_spd_12():
        from player.skill_12_short_pass_spd import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def long_pass_acc_13():
        from player.skill_13_long_pass_acc import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def long_pass_spd_14():
        from player.skill_14_long_pass_spd import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def shot_acc_15():
        from player.skill_15_shot_acc import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def shot_power_16():
        from player.skill_16_shot_power import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def shot_tech_17():
        from player.skill_17_shot_tech import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def free_kick_acc_18():
        from player.skill_18_free_kick_acc import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def curling_19():
        from player.skill_19_curling import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def header_20():
        from player.skill_20_header import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def jump_21():
        from player.skill_21_jump import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def technique_22():
        from player.skill_22_technique import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def aggression_23():
        from player.skill_23_aggression import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def mentality_24():
        from player.skill_24_mentality import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def keeper_skills_25():
        from player.skill_25_keeper_skills import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
    def team_work_26():
        from player.skill_26_team_work import skill_role_cwp, skill_pos
        x = int(factor() * 5 + ((skill_role_cwp[player_role] + skill_pos[position]) / 2)) 
        return x
    
      
    def ID_func():
        from lists import x
        x[0] += 1
        return str(x[0])

    ID = ID_func()
    CALLNAME = "0"
    NATIONALITY, NAME, PLAYER_NAT = nat_name()
    SHIRT_NAME = NAME.upper()
    #AGE = age(age_mu,age_sigma)
    POS_DEFAULT = "2"
    GK = "0"
    CWP = "1"
    CB = "0"
    SB = "0"
    DMF = "0"
    WB = "0"
    CMF = "0"
    SMF = "0"
    AMF = "0"
    WF = "0"
    SS = "0"
    CF = "0"
    HEIGHT, WEIGHT = height_weight(mu,sigma,height_min,height_max,bmi_mu)
    FAV_SIDE, FOOT= center_side_foot()
    CONSISTENCY = str(0)
    CONDITION = str(0)
    INJURY_TOLERANCE = str(0)
    WEAK_FOOT_ACCURACY = str(0)
    WEAK_FOOT_FREQUENCY = str(0)
    ATTACK = attack_01()
    DEFENCE = defence_02()
    BALANCE = balance_03()
    STAMINA = stamina_04()
    TOP_SPEED = top_speed_05()
    ACCELERATION = acceleration_06()
    RESPONSE = response_07()
    AGILITY = agility_08()
    DRIBBLE_ACCURACY = dribble_acc_09()
    DRIBBLE_SPEED = dribble_spd_10()
    SHORT_PASS_ACCURACY = short_pass_acc_11()
    SHORT_PASS_SPEED = short_pass_spd_12()
    LONG_PASS_ACCURACY = long_pass_acc_13()
    LONG_PASS_SPEED = long_pass_spd_14()
    SHOT_ACCURACY = shot_acc_15()
    SHOT_POWER = shot_power_16()
    SHOT_TECHNIQUE = shot_tech_17()
    FREE_KICK_ACCURACY = free_kick_acc_18()
    CURLING = curling_19()
    HEADER = header_20()
    JUMP = jump_21()
    TECHNIQUE = technique_22()
    AGGRESSION = aggression_23()
    MENTALITY = mentality_24()
    KEEPER_SKILLS = keeper_skills_25()
    TEAM_WORK = team_work_26()
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

    print("Position: CWP   #",CLUB_NUMBER)
    print(f"Name: {NAME} ({PLAYER_NAT}) [{NATIONALITY}]")
    print("Role: ",player_role)
    print(f"Height: {float(HEIGHT)/100.0} m")
    print(f"Weight: {WEIGHT} kg")
    print("Age: ",AGE)
    print(f"Foot: {FOOT}    Side: {FAV_SIDE}")
    print()
    print("Attack: ", ATTACK)

    return rows