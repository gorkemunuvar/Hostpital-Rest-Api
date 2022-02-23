# | KABINET | ISIM        | SINIFI |
# | 69062   | 208 DAHLIYE | P      |

PROFESSIONS_BY_POLYCLINIC_ID = """SELECT kabinet, isim, sinifi FROM ng_his_glzr
                                  WHERE psff is null and  profs='{polyclinic_id}'"""
