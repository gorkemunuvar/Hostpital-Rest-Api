# | PROFS | ISIM      | ACIKLAMA     |
# | UZ240 | NEVROLOJI | Açıklama...  |

POLYCLINICS = "SELECT profs, isim, aciklama, resim FROM ng_his_kabuzman WHERE kiosk='X' ORDER BY isim"


SEARCH_POLYCLINICS = """SELECT profs, isim, aciklama, resim FROM ng_his_kabuzman
                        WHERE kiosk='X' AND LOWER(isim)
                        LIKE LOWER('%{search_string}%')
                        ORDER BY isim"""
