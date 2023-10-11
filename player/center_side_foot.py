import random

def center_side_foot():
        
    ### main side
    side_list = ["L","R","B"]
    side_rnd_list = random.choices(side_list, weights= [1,4,2])
    side = side_rnd_list[0]

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
    
    return [side, foot] 