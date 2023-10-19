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