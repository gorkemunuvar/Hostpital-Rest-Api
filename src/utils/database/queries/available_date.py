# | DATAR      | D     | BASSAAT | BITSAAT | SERVIS_ID   | ISIM        |
# | 29/12/2021 | прием | 11:00   | 17:00   | 64010       | 111 dahliye |


AVAILABLE_DATES_BY_DOCTOR_ID = """SELECT ng_his_vractakvim.datar, 'прием' d, ng_his_vractakvim.bassaat,
                                  ng_his_vractakvim.bitsaat, ng_his_vractakvim.servis_id, ng_his_glzr.isim
                                  FROM ng_his_glzr, ng_his_vractakvim
                                  WHERE ng_his_vractakvim.doktor_id='{doctor_id}'
                                  AND ng_his_vractakvim.servis_id=ng_his_glzr.kabinet
                                  AND TO_DATE(ng_his_vractakvim.datar,'DD/MM/YYYY') >= TO_DATE(sysdate,'DD/MM/YYYY')
                                  AND ng_his_vractakvim.servis_id
                                  IN (SELECT kabinet FROM ng_his_glzr WHERE sinifi <>'S')
                                  ORDER BY ng_his_vractakvim.datar ASC"""


# AVAILABLE_DATES_BY_DOCTOR_ID = """SELECT ng_his_vractakvim.datar, 'прием' d, ng_his_vractakvim.bassaat,
#                                   ng_his_vractakvim.bitsaat, ng_his_vractakvim.servis_id, ng_his_glzr.isim
#                                   FROM ng_his_glzr, ng_his_vractakvim
#                                   WHERE ng_his_vractakvim.doktor_id='DR595'
#                                   AND ng_his_vractakvim.servis_id=ng_his_glzr.kabinet
#                                   AND TO_DATE(ng_his_vractakvim.datar,'DD/MM/YYYY') >= TO_DATE(sysdate,'DD/MM/YYYY')
#                                   AND ng_his_vractakvim.servis_id
#                                   IN (SELECT kabinet FROM ng_his_glzr WHERE sinifi <>'S')
#                                   ORDER BY ng_his_vractakvim.datar ASC"""



AVAILABLE_DATES_WITHOUT_DOCTOR = """SELECT ng_his_vractakvim.datar, 'прием' d, ng_his_vractakvim.bassaat,
                                    ng_his_vractakvim.bitsaat, ng_his_vractakvim.servis_id, ng_his_glzr.isim
                                    FROM ng_his_glzr, ng_his_vractakvim
                                    WHERE ng_his_vractakvim.servis_id=ng_his_glzr.kabinet
                                    AND TO_DATE(ng_his_vractakvim.datar, 'DD/MM/YYYY') >= TO_DATE(sysdate,'DD/MM/YYYY')
                                    AND ng_his_vractakvim.servis_id
                                    IN (SELECT kabinet FROM ng_his_glzr WHERE sinifi ='L')
                                    ORDER BY ng_his_vractakvim.datar ASC"""
