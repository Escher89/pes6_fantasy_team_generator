nat_list = ["Austria","Belgium","Bulgaria","Croatia","Czech","Denmark","England","Finland","France","Germany","Greece","Hungary","Ireland","Italy","Latvia","Netherlands","Northern Ireland",
            "Norway","Poland","Portugal","Romania","Russia","Scotland","Serbia and Montenegro","Slovakia","Slovenia","Spain","Sweden","Switzerland","Turkey","Ukraine","Wales","Angola",
            "Cameroon","Cote d'Ivoire","Ghana","Nigeria","South Africa","Togo","Tunisia","Costa Rica","Mexico","Trinidad and Tobago","United States","Argentina","Brazil","Chile","Colombia",
            "Ecuador","Paraguay","Peru","Uruguay","Iran","Japan","Saudi Arabia","South Korea","Australia","Bosnia and Herzegovinia","Estonia","Israel","Honduras","Jamaica","Panama","Bolivia",
            "Venezuela","China","Uzbekistan","Albania","Cyprus","Iceland","Armenia","Belarus","Georgia","Liechtenstein","Lithuania","Algeria","Benin","Bukina Faso","Cape Verde","Congo","DR Congo",
            "Egypt","Equatorial Guinea","Gabon","Gambia","Guinea","Guinea-Bissau","Kenya","Liberia","Libya","Morocco","Mozambique","Senegal","Sierra Leone","Zambia","Zimbabwe","Canada","Grenada",
            "Guadeloupe","Martinique","Oman","New Zealand","Other"]

csv_list = []

all_roles = ["gk_gk", "gk_sk",
             "cwp_sw",
             "cb_cb", "cb_bpd", "cb_wcb", "cb_ncb",
             "sb_fb", "sb_wb", "sb_nfb", "sb_cwb", "sb_iwb",
             "dmf_dm","dmf_dlp", "dmf_bwm", "dmf_a", "dmf_hb", "dmf_rpm", "dmf_rga", "dmf_vol",
             "wb_wb", "wb_cwb", "wb_iwb",
             "cmf_cm", "cmf_bwm", "cmf_dlp", "cmf_bbm", "cmf_rpm", "cmf_mez", "cmf_car", "cmf_ap",
             "smf_wm", "smf_w", "smf_dw", "smf_wp", "smf_iw",
             "amf_am", "amf_ap", "amf_t", "amf_eg", "amf_ss",
             "fw_w", "fw_ap", "fw_if", "fw_t", "fw_wtm", "fw_rmd", "fw_iw",
             "ss_dlf", "ss_pf", "ss_t", "ss_f9",
             "cf_p", "cf_cf", "cf_af", "cf_tm"]

types_cb3 = ["cb_cb", "cb_bpd", "cb_wcb", "cb_wcb", "cb_ncb"]
types_dmf = ["dmf_dm","dmf_dlp", "dmf_bwm", "dmf_a", "dmf_hb", "dmf_rpm", "dmf_rga", "dmf_vol"]
types_wb = ["wb_wb", "wb_cwb", "wb_iwb"]
types_cmf = ["cmf_cm", "cmf_bwm", "cmf_dlp", "cmf_bbm", "cmf_rpm", "cmf_mez", "cmf_car", "cmf_ap"]
types_smf = ["smf_wm", "smf_w", "smf_dw", "smf_wp", "smf_iw"]
types_amf = ["amf_am", "amf_ap", "amf_t", "amf_eg", "amf_ss"]
types_fw = ["fw_w","fw_ap", "fw_if", "fw_t", "fw_wtm", "fw_rmd", "fw_iw"]
types_ss = ["ss_dlf", "ss_pf", "ss_t", "ss_f9"]
types_cf = ["cf_p", "cf_cf", "cf_af", "cf_tm"]

### lists for subs ###
sub_roles_dmf = ["dmf_dm","dmf_dlp", "dmf_bwm", "dmf_a", "dmf_hb", "dmf_rpm", "dmf_rga", "dmf_vol"]
sub_roles_wb = ["wb_wb", "wb_cwb", "wb_iwb"]
sub_roles_cmf = ["cmf_cm", "cmf_bwm", "cmf_dlp", "cmf_bbm", "cmf_rpm", "cmf_mez", "cmf_car", "cmf_ap"]
sub_roles_smf = ["smf_wm", "smf_w", "smf_dw", "smf_wp", "smf_iw"]
sub_roles_amf = ["amf_am", "amf_ap", "amf_t", "amf_eg", "amf_ss"]
sub_roles_fw = ["fw_w","fw_ap", "fw_if", "fw_t", "fw_wtm", "fw_rmd", "fw_iw"]
sub_roles_ss = ["ss_dlf", "ss_pf", "ss_t", "ss_f9"]
sub_roles_cf = ["cf_p", "cf_cf", "cf_af", "cf_tm", "cf_p", "cf_cf", "cf_af", "cf_tm"]

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