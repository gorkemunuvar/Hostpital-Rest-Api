

KK_IS_APPOINTMENT_TAKEN = """SELECT hasta_id FROM ng_his_pasrandevu 
                          WHERE randevu_saati='{time}' AND datar=TO_DATE('{date}', 'DD/MM/YYYY') 
                          AND kabinet_id='{profession_id}' 
                          AND (doktor_id='{doctor_id}' OR doktor_id IS null) 
                          AND IPTAL IS NULL"""
"""<doctor_id> can be passed null if there is no doctor."""

KK_CREATE_APPOINTMENT_ID = """SELECT NG_HIS_RNDSRN.NEXTVAL FROM DUAL"""


KK_CREATE_APPOINTMENT = """INSERT INTO ng_his_pasrandevu(randevu_id, randevu_saati, hasta_id,
                        kabinet_id, doktor_id, datar, patsiyet, personel_log, aciklama, loglar)
                        VALUES ({id}, '{time}', '{patient_id}',
                        '{profession_id}', '{doctor_id}', TO_DATE('{date}', 'DD/MM/YYYY'), 
                        INITCAP('{patient_surname}')||' '||SUBSTR('{patient_name}', 1, 1)||'.',
                        'NGMED'||' '||TO_CHAR(SYSDATE, 'DD/MM/YYYY HH24:MI:SS'), '{note}',
                        '{profession_id}'||NULL||TO_DATE('{date}', 'DD/MM/YYYY')||'{time}')"""
"""<doctor_id> and <note> can be passed null if there is no data."""


KK_ACTIVE_APPOINTMENTS = """SELECT ng_his_pasrandevu.datar, ng_his_pasrandevu.randevu_saati,
                         ng_his_pasrandevu.kabinet_id, ng_his_glzr.isim, ng_his_pasrandevu.doktor_id,
                         ng_his_rpsl.imya dortoradi, ng_his_rpsl.familya doktorsoyadi, ng_his_rshtl.adi hastaadi,
                         ng_his_rshtl.soyadi hastasoyadi, ng_his_rshtl.baba_adi hastababaadi, 
                         ng_his_rshtl.droj hastadogumtarihi, ng_his_pasrandevu.randevu_id
                         FROM ng_his_pasrandevu, ng_his_rshtl, ng_his_glzr, ng_his_rpsl
                         WHERE ng_his_pasrandevu.hasta_id = ng_his_rshtl.patsno
                         AND ng_his_pasrandevu.kabinet_id = ng_his_glzr.kabinet
                         AND ng_his_rpsl.kullan(+) = ng_his_pasrandevu.doktor_id
                         AND ng_his_pasrandevu.iptal is null
                         AND ng_his_pasrandevu.hasta_id = '{patient_id}'
                         AND TO_DATE(ng_his_pasrandevu.datar, 'DD/MM/YYYY') >= TO_DATE(sysdate, 'DD/MM/YYYY')
                         ORDER BY ng_his_pasrandevu.datar, ng_his_pasrandevu.randevu_saati ASC"""


KK_PAST_APPOINTMENTS = """SELECT ng_his_pasrandevu.datar, ng_his_pasrandevu.randevu_saati,
                       ng_his_pasrandevu.kabinet_id, ng_his_glzr.isim, ng_his_pasrandevu.doktor_id, 
                       ng_his_rpsl.imya dortoradi, ng_his_rpsl.familya doktorsoyadi, ng_his_rshtl.adi hastaadi,
                       ng_his_rshtl.soyadi hastasoyadi, ng_his_rshtl.baba_adi hastababaadi,
                       ng_his_rshtl.droj hastadogumtarihi, ng_his_pasrandevu.randevu_id
                       FROM ng_his_pasrandevu, ng_his_rshtl, ng_his_glzr, ng_his_rpsl
                       WHERE ng_his_pasrandevu.hasta_id=ng_his_rshtl.patsno
                       AND ng_his_pasrandevu.kabinet_id=ng_his_glzr.kabinet
                       AND ng_his_rpsl.kullan(+)=ng_his_pasrandevu.doktor_id
                       AND ng_his_pasrandevu.iptal is null
                       AND ng_his_pasrandevu.hasta_id='{patient_id}'
                       AND TO_DATE(ng_his_pasrandevu.datar, 'DD/MM/YYYY') < TO_DATE(sysdate, 'DD/MM/YYYY')
                       ORDER BY ng_his_pasrandevu.datar, ng_his_pasrandevu.randevu_saati ASC"""

KK_IS_APPOINTMENT_EXIST = """SELECT randevu_id FROM ng_his_pasrandevu WHERE randevu_id={appointment_id}"""

KK_CANCEL_APPOINTMENT = """UPDATE NG_HIS_PASRANDEVU SET IPTAL='X',
                        IPTALTUR='D', LOGLAR=NULL,
                        IPTAL_TAR=TO_DATE(SYSDATE,'DD/MM/YYYY'),
                        IPTAL_LOG=SUBSTR(USER, 1, 6)||' '||TO_CHAR(SYSDATE,'DD/MM/YYYY HH24:MI:SS')
                        WHERE NG_HIS_PASRANDEVU.randevu_id='{appointment_id}'"""
