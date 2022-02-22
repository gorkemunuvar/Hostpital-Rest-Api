KK_SEARCH_PATIENT = """SELECT patsno FROM ng_his_rshtl
                    WHERE LOWER(adi) LIKE LOWER('%{name}%') 
                    AND LOWER(soyadi) LIKE LOWER('%{surname}%')
                    AND DROJ=TO_DATE('{birthday}', 'DD/MM/YYYY')"""

KK_CREATE_PATIENT_ID = """PASTNOAL"""

KK_CREATE_PATIENT = """INSERT INTO ng_his_rshtl(patsno, adi, soyadi, droj, firmano, cep1)
                    VALUES ('{patient_id}', '{name}', '{surname}', 
                    TO_DATE('{birthday}', 'DD/MM/YYYY'), '0000', '{phone_number}')"""

KK_GET_PATIENT = """SELECT patsno, adi, soyadi, baba_adi, droj, firmano, cep1
                 FROM ng_his_rshtl WHERE adi='{name}' AND soyadi='{surname}'
                 AND cep1='{phone_number}' AND droj=TO_DATE('{birthday}', 'DD/MM/YYYY')"""
