nat_list = ["Austria","Belgium","Bulgaria","Croatia","Czech","Denmark","England","Finland","France","Germany","Greece","Hungary","Ireland","Italy","Latvia","Netherlands","Northern Ireland",
            "Norway","Poland","Portugal","Romania","Russia","Scotland","Serbia and Montenegro","Slovakia","Slovenia","Spain","Sweden","Switzerland","Turkey","Ukraine","Wales","Angola",
            "Cameroon","Cote d'Ivoire","Ghana","Nigeria","South Africa","Togo","Tunisia","Costa Rica","Mexico","Trinidad and Tobago","United States","Argentina","Brazil","Chile","Colombia",
            "Ecuador","Paraguay","Peru","Uruguay","Iran","Japan","Saudi Arabia","South Korea","Australia","Bosnia and Herzegovinia","Estonia","Israel","Honduras","Jamaica","Panama","Bolivia",
            "Venezuela","China","Uzbekistan","Albania","Cyprus","Iceland","Armenia","Belarus","Georgia","Liechtenstein","Lithuania","Algeria","Benin","Bukina Faso","Cape Verde","Congo","DR Congo",
            "Egypt","Equatorial Guinea","Gabon","Gambia","Guinea","Guinea-Bissau","Kenya","Liberia","Libya","Morocco","Mozambique","Senegal","Sierra Leone","Zambia","Zimbabwe","Canada","Grenada",
            "Guadeloupe","Martinique","Oman","New Zealand","Other"]

csv_list = []

types_cb3 = ["center back", "ball playing center back", "wide center back", "wide center back", "no non-sense center back"]
types_dmf = ["defensive midfielder","deep lying playmaker", "ball winning midfielder", "anchor man", "half back", "regista", "segundo volante"]
types_wb = ["wing back", "complete wing back", "inverted wing back"]
types_cmf = ["central midfielder", "deep lying playmaker", "box to box midfielder", "advanced playmaker", "ball winning midfielder", "vertical playmaker", "mezzala", "carrilero"]
types_smf = ["wide midflieder", "winger", "defensive winger", "wide playmaker", "inverted winger"]
types_amf = ["offensive midfielder", "advanced playmaker", "trequatista", "enganche", "shadow striker"]
types_fw = ["winger","advanced playmaker", "inside forward", "trequatista", "wide target man", "raumdeuter", "inverted winger"]
types_ss = ["deep lying forward", "pressing forward", "trequatista", "false nine"]
types_cf = ["advanced forward", "target man", "poacher", "complete forward"]

### lists for subs ###
sub_roles_dmf = ["defensive midfielder","deep lying playmaker", "ball winning midfielder", "anchor man", "half back", "regista", "segundo volante"]
sub_roles_wb = ["wing back", "complete wing back", "inverted wing back"]
sub_roles_cmf = ["central midfielder", "deep lying playmaker", "box to box midfielder", "advanced playmaker", "ball winning midfielder", "vertical playmaker", "mezzala", "carrilero"]
sub_roles_smf = ["wide midflieder", "winger", "defensive winger", "wide playmaker", "inverted winger"]
sub_roles_amf = ["offensive midfielder", "advanced playmaker", "trequatista", "enganche", "shadow striker"]
sub_roles_fw = ["winger","advanced playmaker", "inside forward", "trequatista", "wide target man", "raumdeuter", "inverted winger"]
sub_roles_ss = ["deep lying forward", "pressing forward", "trequatista", "false nine"]
sub_roles_cf = ["advanced forward", "target man", "poacher", "complete forward", "advanced forward", "target man", "poacher", "complete forward"]

sub_sb_side_list = ["L", "R", "B"]
sub_wb_side_list = ["L", "R", "B"]
sub_smf_side_list = ["L", "R", "B"]
sub_fw_side_list = ["L", "R", "B"]

sb_side_list = ["L", "R", "B"]
wb_side_list = ["L", "R", "B"]
smf_side_list = ["L", "R", "B"]
fw_side_list = ["L", "R", "B"]

x = [0]
shirt_nr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

flags = {0: 0,
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0,
        7 : 0,
        8 : 0,
        9 : 0,
        10 : 0,
        11 : 0,
        12 : 0,
        13 : 0,
        14 : 0,
        15 : 0,
        16 : 0,
        17 : 0,
        18 : 0,
        19 : 0,
        20 : 0,
        21 : 0,
        22 : 0,
        23 : 0,
        24 : 0,
        25 : 0}