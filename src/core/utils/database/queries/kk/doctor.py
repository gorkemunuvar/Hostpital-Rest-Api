
# | DOKTOR_ID | SOY    | AD   | BABA | PERBILGI          | RESIM |
# | DR582     | Yildiz | Ayse | null | Kulak Burun Boğaz | Blob  |

ALL_DOCTORS = """SELECT ng_his_rpsl.kullan, ng_his_rpsl.famılya, ng_his_rpsl.imya,
                 ng_his_rpsl.ocest, ng_his_rpsl.perbilgi, ng_his_prsrsmm.resim,
                 ng_hıs_prsrsmm.uzmanlık, ng_hıs_prsrsmm.egıtım, ng_hıs_prsrsmm.deneyım,
                 ng_hıs_prsrsmm.sertıfıka
                 FROM ng_his_rpsl, ng_his_prsrsmm
                 WHERE ng_his_rpsl.kullan=ng_hıs_prsrsmm.vrac_ıd(+)
                 ORDER BY ng_his_rpsl.famılya, ng_his_rpsl.imya
                 OFFSET 3 ROWS FETCH NEXT 1 ROWS ONLY"""


SEARCH_DOCTORS = """SELECT ng_his_rpsl.kullan, ng_his_rpsl.famılya, ng_his_rpsl.imya,
                    ng_his_rpsl.ocest, ng_his_rpsl.perbilgi, ng_his_prsrsmm.resim,
                    ng_hıs_prsrsmm.uzmanlık, ng_hıs_prsrsmm.egıtım, ng_hıs_prsrsmm.deneyım,
                    ng_hıs_prsrsmm.sertıfıka
                    FROM ng_his_rpsl, ng_his_prsrsmm
                    WHERE ng_his_rpsl.kullan=ng_hıs_prsrsmm.vrac_ıd(+)
                    AND
                    (LOWER(ng_his_rpsl.famılya) LIKE LOWER('%{search_string}%')
                    OR LOWER(ng_his_rpsl.imya)  LIKE LOWER('%{search_string}%')
                    OR LOWER(ng_his_rpsl.ocest) LIKE LOWER('%{search_string}%'))
                    ORDER BY ng_his_rpsl.famılya, ng_his_rpsl.imya"""


# Şu anda mobilde ihtiyaç yok.
# | DOKTOR_ID | SOY    | AD   | BABA   | PERBILGI          | RESIM | UZMANLIK    | EGITIM      | DENEYIM     | SERTIFIKA   |
# | DR582     | Yildiz | Ayse | null   | Kulak Burun Boğaz | Blob  | <long text> | <long text> | <long text> | <long text>
DOCTOR_BY_ID = """  SELECT ng_his_rpsl.kullan, ng_his_rpsl.famılya ,ng_his_rpsl.imya,ng_his_rpsl.ocest, ng_his_rpsl.perbilgi,
                    ng_hıs_prsrsmm.uzmanlık, ng_hıs_prsrsmm.egıtım, ng_hıs_prsrsmm.deneyım, ng_hıs_prsrsmm.sertıfıka,
                    NG_HIS_PRSRSMM.RESIM
                    FROM ng_his_rpsl, NG_HIS_PRSRSMM
                    WHERE ng_his_rpsl.kullan=ng_hıs_prsrsmm.vrac_ıd(+) and ng_his_rpsl.kullan='{id}'
                    ORDER BY ng_his_rpsl.famılya ,ng_his_rpsl.imya"""


# | DOKTOR_ID | SOY    | AD   | BABA   | PERBILGI          | RESIM | PROFS |
# | DR582     | Yildiz | Ayse | null   | Kulak Burun Boğaz | Blob  | UZ001 |

DOCTORS_BY_POLYCLINIC_ID = """SELECT ng_his_rpsl.kullan, ng_his_rpsl.famılya, ng_his_rpsl.imya,
                              ng_his_rpsl.ocest, ng_his_rpsl.perbilgi, ng_hıs_prsrsmm.uzmanlık,
                              ng_hıs_prsrsmm.egıtım, ng_hıs_prsrsmm.deneyım, ng_hıs_prsrsmm.sertıfıka,
                              ng_hıs_prsrsmm.resım, ng_his_glzr.kabinet, ng_his_glzr.isim, ng_his_glzr.profs
                              FROM ng_his_rpsl, ng_hıs_prsrsmm, ng_his_glzr, ng_his_yrgrv
                              WHERE ng_his_rpsl.kullan=ng_hıs_prsrsmm.vrac_ıd(+)
                              AND ng_his_yrgrv.kabınet=ng_his_glzr.kabınet
                              AND ng_his_rpsl.kullan=ng_his_yrgrv.kullan
                              AND ng_his_glzr.profs='{polyclinic_id}'
                              ORDER BY ng_his_rpsl.famılya, ng_his_rpsl.imya"""


# | DOKTOR_ID | AD   | SOYAD |
# | DR582   | Yildiz | Ayse  |

DOCTORS_BY_PROFESSION_ID = """SELECT doktor_id, soy, ad FROM ng_his_vrtkmad
                              WHERE servis_id='{profession_id}' AND doktor_id IS NOT null
                              GROUP BY soy, ad, baba, profs, doktor_id ORDER BY soy, ad"""
