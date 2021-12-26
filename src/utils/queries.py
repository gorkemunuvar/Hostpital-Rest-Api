# Table comments are the returning tables after the queries.

# | DBKOD | DBAD             |
# | K001  | AYGERIM ANA SUBE |

HOSPITALS = "select DBKOD,DBAD from NG_HIS_LNKDBS t"


# | PROFS | ISIM      | ACIKLAMA     |
# | UZ240 | NEVROLOJI | Açıklama...  |

POLYCLINICS = "select profs,isim, aciklama from ng_his_kabuzman where kiosk='X'order by isim"

# | KABINET | ISIM        | SINIFI |
# | 69062   | 208 DAHLIYE | P      |

PROFESSIONS_BY_POLYCLINIC_ID = "select KABINET,ISIM,SINIFI from ng_his_glzr WHERE PROFS='{polyclinic_id}'"


# | DOKTOR_ID | AD   | SOYAD |
# | DR582   | Yildiz | Ayse  |

DOCTORS_BY_PROFESSION_ID = """SELECT doktor_id,soy,ad from ng_his_vrtkmad
                              where servis_id='{profession_id}' and doktor_id IS not null 
                              GROUP BY soy,ad,baba,profs,doktor_id  order by soy,ad"""


# | DATAR      | D     | BASSAAT | BITSAAT | SERVIS_ID   | ISIM        |
# | 29/12/2021 | прием | 11:00   | 17:00   | 64010       | 111 dahliye |

AVAILABLE_APPOINTMENT_DATES = """select ng_his_vractakvim.datar, 'прием' d, ng_his_vractakvim.bassaat,
                                 ng_his_vractakvim.bitsaat,ng_his_vractakvim.servis_id ,ng_his_glzr.isim
                                 from ng_his_glzr,ng_his_vractakvim 
                                 where ng_his_vractakvim.doktor_id='{doctor_id}' 
                                 and ng_his_vractakvim.servis_id=ng_his_glzr.kabinet 
                                 and ng_his_vractakvim.datar>=to_date(sysdate,'dd/mm/yyyy') 
                                 and ng_his_vractakvim.servis_id 
                                 IN (select kabinet from ng_his_glzr where sinifi <>'S')"""

# | DATAR      | D     | BASSAAT | BITSAAT | SERVIS_ID   | ISIM        | PROFS | ARALIK |
# | 29/12/2021 | прием | 11:00   | 17:00   | 64010       | 111 dahliye | UZ001 | DEGER1 |

AVAILABLE_APPOINTMENT_TIME_REQUIREMENTS = """select ng_his_vractakvim.datar, 'прием' d, 
                                             ng_his_vractakvim.bassaat, 
                                             ng_his_vractakvim.bitsaat, 
                                             ng_his_vractakvim.servis_id, 
                                             ng_his_glzr.isim, 
                                             ng_his_glzr.profs, 
                                             ng_his_kabuzman.aralik 
                                             from ng_his_glzr,ng_his_vractakvim ,ng_his_kabuzman 
                                             where ng_his_kabuzman.profs=ng_his_glzr.profs  
                                             and ng_his_vractakvim.doktor_id='{doctor_id}' 
                                             and ng_his_vractakvim.servis_id=ng_his_glzr.kabinet 
                                             and ng_his_vractakvim.datar>=to_date(sysdate,'dd/mm/yyyy') 
                                             and ng_his_vractakvim.servis_id in (select kabinet from ng_his_glzr where sinifi <>'S')"""


# -- string format --
# beginning_time = 07:00
# ending_time = 17:00
# time_interval = DEGER1
# profession_id = 64010
# appointment_date = 2021/12/29

# | SIRA_NO | XDAKKIKA |
# | 85      | 07:00    |
# | 91      | 07:30    |
# ...

AVAILABLE_APPOINTMENT_TIMES = """select  SIRA_NO, XDAKKIKA 
                                 from ng_his_ransaat 
                                 where {time_interval} BETWEEN '{beginning_time}' AND '{ending_time}' 
                                 and {time_interval} not in (select randevu_saati from ng_his_pasrandevu  
                                 where iptal is null and KABINET_id='{profession_id}'
                                 and datar=to_date('{appointment_date}','yyyy/mm/dd')) 
                                 and substr(xdakkika,5,1)='0'
                                 ORDER BY SIRA_NO"""
