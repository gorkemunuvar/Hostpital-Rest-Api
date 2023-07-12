NEWS = """SELECT id, tarih, ru_baslik, ru_haber, ru_resim
          FROM (SELECT t.*, row_number() OVER (ORDER BY tarih DESC) r
          FROM ng_haberler t)   
          WHERE r BETWEEN {start} AND {end} """