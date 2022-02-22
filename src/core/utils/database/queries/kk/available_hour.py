
##################################################
# -- AVAILABLE_HOURS String Format --
# beginning_time = 07:00
# ending_time = 17:00
# time_interval = DEGER1
# profession_id = 64010
# appointment_date = 2021/12/29
##################################################

# | SIRA_NO | XDAKKIKA |
# | 85      | 07:00    |
# | 91      | 07:30    |
# ...

KK_AVAILABLE_HOURS = """SELECT  SIRA_NO, XDAKKIKA
                     FROM ng_his_ransaat
                     WHERE {time_interval} BETWEEN '{beginning_time}' AND '{ending_time}'
                     AND {time_interval} NOT IN (SELECT randevu_saati FROM ng_his_pasrandevu
                     WHERE iptal IS null AND KABINET_id='{profession_id}'
                     AND TO_DATE(datar, 'yyyy/mm/dd')=TO_DATE('{appointment_date}','yyyy/mm/dd'))
                     AND substr(xdakkika,5,1)='0'
                     ORDER BY sira_no"""


# | DATAR      | D     | BASSAAT | BITSAAT | SERVIS_ID   | ISIM        | PROFS | ARALIK |
# | 29/12/2021 | прием | 11:00   | 17:00   | 64010       | 111 dahliye | UZ001 | DEGER1 |

KK_AVAILABLE_HOUR_REQUIREMENTS_BY_DOCTOR_ID = """SELECT ng_his_vractakvim.datar, 'прием' d, ng_his_vractakvim.bassaat,
                                              ng_his_vractakvim.bitsaat, ng_his_vractakvim.servis_id,
                                              ng_his_glzr.isim, ng_his_glzr.profs, ng_his_kabuzman.aralik
                                              FROM ng_his_glzr,ng_his_vractakvim ,ng_his_kabuzman
                                              WHERE ng_his_kabuzman.profs=ng_his_glzr.profs
                                              AND ng_his_vractakvim.doktor_id='{doctor_id}'
                                              AND ng_his_vractakvim.servis_id=ng_his_glzr.kabinet
                                              AND TO_DATE(ng_his_vractakvim.datar, 'dd/mm/yyyy') >= TO_DATE(sysdate, 'dd/mm/yyyy')
                                              AND ng_his_vractakvim.servis_id IN (SELECT kabinet FROM ng_his_glzr
                                              WHERE sinifi <>'S')"""


KK_AVAILABLE_HOUR_REQUIREMENTS_BY_PROFESSION = """SELECT ng_his_vractakvim.datar, 'прием' d, ng_his_vractakvim.bassaat,
                                               ng_his_vractakvim.bitsaat, ng_his_vractakvim.servis_id,
                                               ng_his_glzr.isim, ng_his_glzr.profs, ng_his_kabuzman.aralik
                                               FROM ng_his_glzr,ng_his_vractakvim ,ng_his_kabuzman
                                               WHERE ng_his_kabuzman.profs=ng_his_glzr.profs
                                               AND ng_his_vractakvim.servis_id=ng_his_glzr.kabinet
                                               AND TO_DATE(ng_his_vractakvim.datar, 'dd/mm/yyyy') >= TO_DATE(sysdate,'dd/mm/yyyy')
                                               AND ng_his_vractakvim.servis_id IN (SELECT kabinet FROM ng_his_glzr
                                               WHERE sinifi <>'S')"""
