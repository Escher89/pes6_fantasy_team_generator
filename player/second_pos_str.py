def second_pos_str(GK,CWP,CB,SB,DMF,WB,CMF,SMF,AMF,FW,SS,CF):
    liste = [GK,CWP,CB,SB,DMF,WB,CMF,SMF,AMF,FW,SS,CF]
    liste2 =["GK","CWP","CB","SB","DMF","WB","CMF","SMF","AMF","FW","SS","CF"]
    x = 0
    y = []
    while x != 12:
        if liste[x] == 1:
            y.append(liste2[x])
        x += 1
    return y

def pos_rand(GK, CWP, CB, SB, DMF, WB, CMF, SMF, AMF, FW, SS, CF):
    pos_list = [GK, CWP, CB, SB, DMF, WB, CMF, SMF, AMF, FW, SS, CF]
    w = 0
    x = 0
    y = []

    if pos_list[x] == 1:
        y.append(w)
    w += 2
    x += 1
    while x != 12:
        if pos_list[x] == 1:
            y.append(w)
        w += 1
        x += 1
    return y

def final_position(POS_DEFAULT):
    y ={0: "GK",
        2: "CWP",
        3: "CB",
        4: "SB",
        5: "DMF",
        6: "WB",
        7: "CMF",
        8: "SMF",
        9: "AMF",
        10: "FW",
        11: "SS",
        12: "CF"}
    x = y.get(POS_DEFAULT)
    return x