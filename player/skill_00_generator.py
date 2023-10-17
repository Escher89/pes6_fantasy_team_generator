import random

def skills(points,ATTACK,DEFENCE,BALANCE,STAMINA,
           TOP_SPEED,ACCELERATION,RESPONSE,
           AGILITY,DRIBBLE_ACCURACY,DRIBBLE_SPEED,
           SHORT_PASS_ACCURACY,SHORT_PASS_SPEED,
           LONG_PASS_ACCURACY,LONG_PASS_SPEED,
           SHOT_ACCURACY,SHOT_POWER,SHOT_TECHNIQUE,
           FREE_KICK_ACCURACY,CURLING,HEADER,
           JUMP,TECHNIQUE,AGGRESSION,MENTALITY,
           KEEPER_SKILLS,TEAM_WORK):

    liste2 = [ATTACK,DEFENCE,BALANCE,STAMINA,TOP_SPEED,ACCELERATION,RESPONSE,AGILITY,DRIBBLE_ACCURACY,DRIBBLE_SPEED,SHORT_PASS_ACCURACY,SHORT_PASS_SPEED,LONG_PASS_ACCURACY,LONG_PASS_SPEED,SHOT_ACCURACY,SHOT_POWER,SHOT_TECHNIQUE,FREE_KICK_ACCURACY,CURLING,HEADER,JUMP,TECHNIQUE,AGGRESSION,MENTALITY,KEEPER_SKILLS,TEAM_WORK]
    liste = ["ATT","DEF","BAL","STA","TOP","ACC","RES","AGI","DAC","DSP","SHORT_PASS_ACCURACY","SHORT_PASS_SPEED","LONG_PASS_ACCURACY","LONG_PASS_SPEED","SHOT_ACCURACY","SHOT_POWER","SHOT_TECHNIQUE","FREE_KICK_ACCURACY","CURLING","HEADER","JUMP","TECHNIQUE","AGGRESSION","MENTALITY","KEEPER_SKILLS","TEAM_WORK"]

    y = []
    c = 0

    def test(b):
        from lists import flags
        
        if y.count(liste[b]) == 39 and list(flags.values())[b] == 0:
            liste2[b] /= 2
            flags[b] += 1
            #print(y.count(liste[b]),liste2[b],b)

        if y.count(liste[b]) == 44 and list(flags.values())[b] == 1:
            liste2[b] /= 2
            flags[b] += 1
            #print(y.count(liste[b]),liste2[b],b)

        if y.count(liste[b]) == 49 and list(flags.values())[b] == 2:
            liste2[b] = 0
            flags[b] += 1
            #print(y.count(liste[b]),liste2[b],b)

    while points != 0:
        a = random.choices(liste,liste2)
        y.extend(a)
        points -= 1

        while c != 26:
            test(c)
            c += 1
        c = 0

    z = 0
    q = 50

    ATT = y.count(liste[z]) + q
    z += 1
    DEF = y.count(liste[z]) + q
    z += 1
    BAL = y.count(liste[z]) + q
    z += 1
    STA = y.count(liste[z]) + q
    z += 1
    TOP = y.count(liste[z]) + q
    z += 1
    ACC = y.count(liste[z]) + q
    z += 1
    RES = y.count(liste[z]) + q
    z += 1
    AGI = y.count(liste[z]) + q
    z += 1
    DAC = y.count(liste[z]) + q
    z += 1
    DSP = y.count(liste[z]) + q
    z += 1
    SPA = y.count(liste[z]) + q
    z += 1
    SPS = y.count(liste[z]) + q
    z += 1
    LPA = y.count(liste[z]) + q
    z += 1
    LPS = y.count(liste[z]) + q
    z += 1
    SAC = y.count(liste[z]) + q
    z += 1
    SPO = y.count(liste[z]) + q
    z += 1
    STE = y.count(liste[z]) + q
    z += 1
    FKA = y.count(liste[z]) + q
    z += 1
    CUR = y.count(liste[z]) + q
    z += 1
    HEA = y.count(liste[z]) + q
    z += 1
    JUM = y.count(liste[z]) + q
    z += 1
    TEC = y.count(liste[z]) + q
    z += 1
    AGG = y.count(liste[z]) + q
    z += 1
    MEN = y.count(liste[z]) + q
    z += 1
    KEE = y.count(liste[z]) + q
    z += 1
    TEA = y.count(liste[z]) + q

    liste3 = [ATT,DEF,BAL,STA,TOP,ACC,RES,AGI,DAC,DSP,SPA,SPS,LPA,LPS,SAC,SPO,STE,FKA,CUR,HEA,JUM,TEC,AGG,MEN,KEE,TEA]

    return liste3