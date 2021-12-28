# TODO: sorgularıda büyük küçük harfleri değiştirdim. hepsini tekrar test et.

# Table comments are the returning tables after the queries.

# | DBKOD | DBAD             |
# | K001  | AYGERIM ANA SUBE |

HOSPITALS = "SELECT dbkod, dbad FROM ng_his_lnkdbs t"


# | PROFS | ISIM      | ACIKLAMA     |
# | UZ240 | NEVROLOJI | Açıklama...  |

POLYCLINICS = "SELECT profs, isim, aciklama FROM ng_his_kabuzman WHERE kiosk='X' ORDER BY isim"



# | KABINET | ISIM        | SINIFI |
# | 69062   | 208 DAHLIYE | P      |

PROFESSIONS_BY_POLYCLINIC_ID = "SELECT kabinet, isim, sinifi FROM ng_his_glzr WHERE profs='{polyclinic_id}'"


# | DOKTOR_ID | AD   | SOYAD |
# | DR582   | Yildiz | Ayse  |

DOCTORS_BY_PROFESSION_ID = """SELECT doktor_id, soy, ad FROM ng_his_vrtkmad
                              WHERE servis_id='{profession_id}' AND doktor_id IS NOT null 
                              GROUP BY soy, ad, baba, profs, doktor_id ORDER BY soy, ad"""


# | DATAR      | D     | BASSAAT | BITSAAT | SERVIS_ID   | ISIM        |
# | 29/12/2021 | прием | 11:00   | 17:00   | 64010       | 111 dahliye |

AVAILABLE_APPOINTMENT_DATES = """SELECT ng_his_vractakvim.datar, 'прием' d, ng_his_vractakvim.bassaat,
                                 ng_his_vractakvim.bitsaat, ng_his_vractakvim.servis_id, ng_his_glzr.isim
                                 FROM ng_his_glzr, ng_his_vractakvim 
                                 WHERE ng_his_vractakvim.doktor_id='{doctor_id}' 
                                 AND ng_his_vractakvim.servis_id=ng_his_glzr.kabinet 
                                 AND ng_his_vractakvim.datar >= to_date(sysdate,'dd/mm/yyyy') 
                                 AND ng_his_vractakvim.servis_id 
                                 IN (SELECT kabinet FROM ng_his_glzr WHERE sinifi <>'S')"""

# | DATAR      | D     | BASSAAT | BITSAAT | SERVIS_ID   | ISIM        | PROFS | ARALIK |
# | 29/12/2021 | прием | 11:00   | 17:00   | 64010       | 111 dahliye | UZ001 | DEGER1 |

AVAILABLE_APPOINTMENT_TIME_REQUIREMENTS = """SELECT ng_his_vractakvim.datar, 'прием' d, 
                                             ng_his_vractakvim.bassaat, 
                                             ng_his_vractakvim.bitsaat, 
                                             ng_his_vractakvim.servis_id, 
                                             ng_his_glzr.isim, 
                                             ng_his_glzr.profs, 
                                             ng_his_kabuzman.aralik 
                                             FROM ng_his_glzr,ng_his_vractakvim ,ng_his_kabuzman 
                                             WHERE ng_his_kabuzman.profs=ng_his_glzr.profs  
                                             AND ng_his_vractakvim.doktor_id='{doctor_id}' 
                                             AND ng_his_vractakvim.servis_id=ng_his_glzr.kabinet 
                                             AND ng_his_vractakvim.datar >= to_date(sysdate,'dd/mm/yyyy') 
                                             AND ng_his_vractakvim.servis_id IN (SELECT kabinet FROM ng_his_glzr WHERE sinifi <>'S')"""


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

AVAILABLE_APPOINTMENT_TIMES = """SELECT  SIRA_NO, XDAKKIKA 
                                 FROM ng_his_ransaat 
                                 WHERE {time_interval} BETWEEN '{beginning_time}' AND '{ending_time}' 
                                 AND {time_interval} NOT IN (SELECT randevu_saati FROM ng_his_pasrandevu  
                                 WHERE iptal IS null AND KABINET_id='{profession_id}'
                                 AND datar=to_date('{appointment_date}','yyyy/mm/dd')) 
                                 AND substr(xdakkika,5,1)='0'
                                 ORDER BY sira_no"""



################################
# new queries
################################

# get doctors by polyclinic id
POLYCLINIC_BY_ID = """select ng_his_vrtkmad.doktor_id,ng_his_vrtkmad.soy,ng_his_vrtkmad.ad,ng_his_vrtkmad.baba vr,ng_his_vrtkmad.profs ,
                      ng_hıs_prsrsmm.perbılgı , dbms_lob.getlength(NG_HIS_PRSRSMM.RESIM) "RESIM"
                      from ng_his_vrtkmad ,NG_HIS_PRSRSMM 
                      where  ng_his_vrtkmad.doktor_ıd=ng_hıs_prsrsmm.vrac_ıd and
                      ng_his_vrtkmad.profs='UZ001'  and ng_his_vrtkmad.doktor_id IS not null 
                      GROUP BY  ng_his_vrtkmad.doktor_id,ng_his_vrtkmad.soy,ng_his_vrtkmad.ad,ng_his_vrtkmad.baba ,ng_his_vrtkmad.profs ,
                      ng_hıs_prsrsmm.perbılgı, dbms_lob.getlength(ng_hıs_prsrsmm.resım)   order by ng_his_vrtkmad.soy,ng_his_vrtkmad.ad"""



ALL_DOCTORS = """select ng_his_vrtkmad.doktor_id,ng_his_vrtkmad.soy,ng_his_vrtkmad.ad,ng_his_vrtkmad.baba,ng_his_vrtkmad.profs,ng_his_vrtkmad.perbılgı ,
                 dbms_lob.getlength(NG_HIS_PRSRSMM.RESIM) "RESIM"
                 from ng_his_vrtkmad ,NG_HIS_PRSRSMM 
                 where  ng_his_vrtkmad.doktor_ıd=ng_hıs_prsrsmm.vrac_ıd and ng_his_vrtkmad.doktor_id IS not null 
                 GROUP BY  ng_his_vrtkmad.doktor_id,ng_his_vrtkmad.soy,ng_his_vrtkmad.ad,ng_his_vrtkmad.baba ,ng_his_vrtkmad.profs ,ng_his_vrtkmad.perbılgı ,
                 dbms_lob.getlength(ng_hıs_prsrsmm.resım)   order by ng_his_vrtkmad.soy,ng_his_vrtkmad.ad"""



DOCTOR_DETAIL = """select ng_his_vrtkmad.doktor_id,ng_his_vrtkmad.soy,ng_his_vrtkmad.ad,ng_his_vrtkmad.baba,ng_his_vrtkmad.profs,ng_his_vrtkmad.perbılgı ,
                   dbms_lob.getlength(NG_HIS_PRSRSMM.RESIM) "RESIM",ng_hıs_prsrsmm.uzmanlık,ng_hıs_prsrsmm.egıtım,ng_hıs_prsrsmm.deneyım,ng_hıs_prsrsmm.sertıfıka
                   from ng_his_vrtkmad ,NG_HIS_PRSRSMM 
                   where  ng_his_vrtkmad.doktor_ıd=ng_hıs_prsrsmm.vrac_ıd and ng_his_vrtkmad.doktor_id IS not null 
                   GROUP BY  ng_his_vrtkmad.doktor_id,ng_his_vrtkmad.soy,ng_his_vrtkmad.ad,ng_his_vrtkmad.baba ,ng_his_vrtkmad.profs ,ng_his_vrtkmad.perbılgı ,
                   dbms_lob.getlength(ng_hıs_prsrsmm.resım),ng_hıs_prsrsmm.uzmanlık,ng_hıs_prsrsmm.egıtım,ng_hıs_prsrsmm.deneyım,ng_hıs_prsrsmm.sertıfıka
                   order by ng_his_vrtkmad.soy,ng_his_vrtkmad.ad"""