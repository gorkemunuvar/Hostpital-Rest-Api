import random

test_doctors_data = [
    {
        'id': '1',
        'name': 'Smadiyarova',
        'surname': 'Nelly Sandybaevna',
        'description': 'Kulak burun boğaz uzmanı (çocuklar ve yetişkinler)',
        'image_path': '/static/images/doctors/doctor1.png',
        'profession': """Tıbbi uygulamada kullanılmasına izin verilen modern önleme, teşhis, tedavi ve rehabilitasyon yöntemlerini kullanarak uzmanlık alanında nitelikli tıbbi bakım sağlar.

Geniş bir profilin ayaktan hasta
kabulüne yol açar : - sinüzit tedavisi;
- pürülan rinit;
- kronik bademcik iltihabı, bademcik iltihabı;
- bronko-pulmoner hastalıklar;
- farenjit, rinit, adenoidler, orta kulak iltihabı;
- nazal septumdaki operasyonlar;
- SARS, akut solunum yolu enfeksiyonları ve çeşitli soğuk algınlığı;
- Tonsilor aparatı ile oldukça etkili tedavi;
- sinüs hastalıklarının donanım tedavisi ("guguk kuşu"),
- donanım "pnömasaj";
- İşitsel duyarlılığın belirlenmesi (Odyometri);
- KBB endoskopisi;
- "ses tonu" üzerine fizyoterapi;
- paratonsiller (peri-medial) apsenin açılması, kulak çınlaması;
- novokain ablukası;
- orta kulağın işlevi, kulak zarının hareketlilik derecesi ve işitsel kemikçiklerin iletimi hakkında nesnel bir çalışma yöntemi (Timpanometri);
- akut ve kronik laringotrakeit için ilaçların gırtlak içine infüzyonu.""",
        'education': """Высшее медицинское образование.

Актюбинская государственная медицинская академия, 1994-2000.

Специальность - Лечебное дело.""",
        'experience': """Toplam iş deneyimi 20 yıldır.""",
        'achievements': """"Larenks Hastalıkları" döngüsünde "Kulak Burun Boğaz" uzmanlık sertifikası, yayın tarihi: 25.01.2013.

"Yetişkin Kulak Burun Boğaz" uzmanlık sertifikası, veriliş tarihi: 06.02.2013.

"Mesleki patolojinin güncel sorunları" döngüsünde "Kulak Burun Boğaz" uzmanlık sertifikası, veriliş tarihi: 05.11.2016.

Uzmanlık sertifikası "Kulak Burun Boğaz (ana uzmanlık profiline göre odyoloji, endoskopi) (yetişkin, pediatrik), yayın tarihi: 09.04.2018."""
    },
    {
        'id': '2',
        'name': 'Buzar Alexander',
        'surname': 'Petrovich',
        'description': 'Kulak burun boğaz uzmanı yetişkin, çocuklar',
        'image_path': '/static/images/doctors/doctor2.png',
        'profession': """Tıbbi uygulamada kullanılmasına izin verilen modern önleme, teşhis, tedavi ve rehabilitasyon yöntemlerini kullanarak uzmanlık alanında nitelikli tıbbi bakım sağlar.

Geniş bir profilin ayaktan hasta
kabulüne yol açar : - sinüzit tedavisi;
- pürülan rinit;
- kronik bademcik iltihabı, bademcik iltihabı;
- bronko-pulmoner hastalıklar;
- farenjit, rinit, adenoidler, orta kulak iltihabı;
- nazal septumdaki operasyonlar;
- SARS, akut solunum yolu enfeksiyonları ve çeşitli soğuk algınlığı;
- Tonsilor aparatı ile oldukça etkili tedavi;
- sinüs hastalıklarının donanım tedavisi ("guguk kuşu"),
- donanım "pnömasaj";
- İşitsel duyarlılığın belirlenmesi (Odyometri);
- KBB endoskopisi;
- "ses tonu" üzerine fizyoterapi;
- paratonsiller (peri-medial) apsenin açılması, kulak çınlaması;
- novokain ablukası;
- orta kulağın işlevi, kulak zarının hareketlilik derecesi ve işitsel kemikçiklerin iletimi hakkında nesnel bir çalışma yöntemi (Timpanometri);
- akut ve kronik laringotrakeit için ilaçların gırtlak içine infüzyonu.""",
        'education': """Daha yüksek, tıp eğitimi.

Aktobe Devlet Tıp Akademisi, 2000-2006.

Uzmanlık - Pediatri.""",
        'experience': """Genel iş deneyimi - 14 yıl.""",
        'achievements': """"Pediatri. Pediatrik Cerrahi" uzmanlık alanında staj bitirme belgesi, yayın tarihi: 22.06.2007.

"Çocuklar için Kulak Burun Boğaz" uzmanlık sertifikası, yayın tarihi: 18.12.2009.

"Kulak Burun Boğaz (çocuklar için). Odyoloji ve odyoloji" uzmanlık sertifikası, veriliş tarihi: 04/03/2015.

Uzmanlık sertifikası "Kulak Burun Boğaz (odyoloji, ana uzmanlık profiline göre endoskopi) (yetişkin)", yayın tarihi: 30.11.2018.

Uzmanlık sertifikası "Kulak Burun Boğaz (yetişkin, pediatrik). Endoskopi", yayın tarihi: 20.12.2018.

Uzmanlık sertifikası "Kulak burun boğaz (odyoloji, ana uzmanlık profiline göre endoskopi) (yetişkin, pediatrik)", yayın tarihi: 09.01.2019."""
    },
    {
        'id': '3',
        'name': 'Akhmetgaliev',
        'surname': 'Ernar Kokimzhanuly',
        'description': 'Kulak burun boğaz uzmanı (çocuklar ve yetişkinler)',
        'image_path': '/static/images/doctors/doctor3.png',
        'profession': """Tıbbi uygulamada kullanılmasına izin verilen modern önleme, teşhis, tedavi ve rehabilitasyon yöntemlerini kullanarak uzmanlık alanında nitelikli tıbbi bakım sağlar.

Geniş bir profilin ayaktan hasta
kabulüne yol açar : - sinüzit tedavisi;
- pürülan rinit;
- kronik bademcik iltihabı, bademcik iltihabı;
- bronko-pulmoner hastalıklar;
- farenjit, rinit, adenoidler, orta kulak iltihabı;
- nazal septumdaki operasyonlar;
- SARS, akut solunum yolu enfeksiyonları ve çeşitli soğuk algınlığı;
- Tonsilor aparatı ile oldukça etkili tedavi;
- sinüs hastalıklarının donanım tedavisi ("guguk kuşu"),
- donanım "pnömasaj";
- İşitsel duyarlılığın belirlenmesi (Odyometri);
- KBB endoskopisi;
- "ses tonu" üzerine fizyoterapi;
- paratonsiller (peri-medial) apsenin açılması, kulak çınlaması;
- novokain ablukası;
- orta kulağın işlevi, kulak zarının hareketlilik derecesi ve işitsel kemikçiklerin iletimi hakkında nesnel bir çalışma yöntemi (Timpanometri);
- akut ve kronik laringotrakeit için ilaçların gırtlak içine infüzyonu.""",
        'education': """Daha yüksek, tıp eğitimi.
Ospanov Batı Kazakistan Devlet Tıp Üniversitesi, 2007-2014.

Uzmanlık - Genel Tıp.   """,
        'experience': """Toplam iş deneyimi 7 yıldır.""",
        'achievements': """"Genel Tıp" uzmanlık alanında staj bitirme belgesi, uzman doktor niteliği, veriliş tarihi: 11.07.2014

"Çocuklar da dahil olmak üzere Kulak Burun Boğaz" uzmanlığında ikamet tamamlama sertifikası, yayın tarihi: 24.07.2017.

Uzmanlık sertifikası "Kulak Burun Boğaz (ana uzmanlık profilinde odyoloji, endoskopi) (yetişkin, pediatrik)", yayın tarihi: 09/11/2017."""
    },
    {
        'id': '4',
        'name': 'Isentaeva Gulmira',
        'surname': 'Sharafatdinovna',
        'description': 'Kulak Burun Boğaz uzmanı, odyolog (çocuklar ve yetişkinler)',
        'image_path': '/static/images/doctors/doctor4.png',
        'profession': """Tıbbi uygulamada kullanılmasına izin verilen modern önleme, teşhis, tedavi ve rehabilitasyon yöntemlerini kullanarak uzmanlık alanında nitelikli tıbbi bakım sağlar.

Geniş bir profilin ayaktan hasta
kabulüne yol açar : - sinüzit tedavisi;
- pürülan rinit;
- kronik bademcik iltihabı, bademcik iltihabı;
- bronko-pulmoner hastalıklar;
- farenjit, rinit, adenoidler, orta kulak iltihabı;
- nazal septumdaki operasyonlar;
- SARS, akut solunum yolu enfeksiyonları ve çeşitli soğuk algınlığı;
- Tonsilor aparatı ile oldukça etkili tedavi;
- sinüs hastalıklarının donanım tedavisi ("guguk kuşu"),
- donanım "pnömasaj";
- İşitsel duyarlılığın belirlenmesi (Odyometri);
- KBB endoskopisi;
- "ses tonu" üzerine fizyoterapi;
- paratonsiller (peri-medial) apsenin açılması, kulak çınlaması;
- novokain ablukası;
- orta kulağın işlevi, kulak zarının hareketlilik derecesi ve işitsel kemikçiklerin iletimi hakkında nesnel bir çalışma yöntemi (Timpanometri);
- akut ve kronik laringotrakeit için ilaçların gırtlak içine infüzyonu.""",
        'education': """Daha yüksek tıp eğitimi.

1996-2003 yılları arasında M. Ospanov'un adını taşıyan Batı Kazakistan Devlet Tıp Akademisi.

Uzmanlık - Pediatri.""",
        'experience': """Toplam iş tecrübesi 18 yıldır.""",
        'achievements': """"Kulak Burun Boğaz (çocuk)" uzmanlık sertifikası, veriliş tarihi: 24.01.2014.

Uzmanlık sertifikası "Kulak Burun Boğaz (odyoloji) (yetişkin, pediatrik)", yayın tarihi: 27.01.2017.

"Kulak Burun Boğaz (çocuklar)" uzmanlık sertifikası, veriliş tarihi: 06.02.2014.

24.02.2017 tarihli "Kulak Burun Boğaz (odyoloji) (yetişkin)" uzmanlık sertifikası."""
    },
    {
        'id': '5',
        'name': 'Smadiyarova',
        'surname': 'Nelly Sandybaevna',
        'description': 'Kulak burun boğaz uzmanı (çocuklar ve yetişkinler)',
        'image_path': '/static/images/doctors/doctor1.png',
        'profession': """Tıbbi uygulamada kullanılmasına izin verilen modern önleme, teşhis, tedavi ve rehabilitasyon yöntemlerini kullanarak uzmanlık alanında nitelikli tıbbi bakım sağlar.

Geniş bir profilin ayaktan hasta
kabulüne yol açar : - sinüzit tedavisi;
- pürülan rinit;
- kronik bademcik iltihabı, bademcik iltihabı;
- bronko-pulmoner hastalıklar;
- farenjit, rinit, adenoidler, orta kulak iltihabı;
- nazal septumdaki operasyonlar;
- SARS, akut solunum yolu enfeksiyonları ve çeşitli soğuk algınlığı;
- Tonsilor aparatı ile oldukça etkili tedavi;
- sinüs hastalıklarının donanım tedavisi ("guguk kuşu"),
- donanım "pnömasaj";
- İşitsel duyarlılığın belirlenmesi (Odyometri);
- KBB endoskopisi;
- "ses tonu" üzerine fizyoterapi;
- paratonsiller (peri-medial) apsenin açılması, kulak çınlaması;
- novokain ablukası;
- orta kulağın işlevi, kulak zarının hareketlilik derecesi ve işitsel kemikçiklerin iletimi hakkında nesnel bir çalışma yöntemi (Timpanometri);
- akut ve kronik laringotrakeit için ilaçların gırtlak içine infüzyonu.""",
        'education': """Высшее медицинское образование.

Актюбинская государственная медицинская академия, 1994-2000.

Специальность - Лечебное дело.""",
        'experience': """Toplam iş deneyimi 20 yıldır.""",
        'achievements': """"Larenks Hastalıkları" döngüsünde "Kulak Burun Boğaz" uzmanlık sertifikası, yayın tarihi: 25.01.2013.

"Yetişkin Kulak Burun Boğaz" uzmanlık sertifikası, veriliş tarihi: 06.02.2013.

"Mesleki patolojinin güncel sorunları" döngüsünde "Kulak Burun Boğaz" uzmanlık sertifikası, veriliş tarihi: 05.11.2016.

Uzmanlık sertifikası "Kulak Burun Boğaz (ana uzmanlık profiline göre odyoloji, endoskopi) (yetişkin, pediatrik), yayın tarihi: 09.04.2018."""
    },
    {
        'id': '6',
        'name': 'Buzar Alexander',
        'surname': 'Petrovich',
        'description': 'Kulak burun boğaz uzmanı yetişkin, çocuklar',
        'image_path': '/static/images/doctors/doctor2.png',
        'profession': """Tıbbi uygulamada kullanılmasına izin verilen modern önleme, teşhis, tedavi ve rehabilitasyon yöntemlerini kullanarak uzmanlık alanında nitelikli tıbbi bakım sağlar.

Geniş bir profilin ayaktan hasta
kabulüne yol açar : - sinüzit tedavisi;
- pürülan rinit;
- kronik bademcik iltihabı, bademcik iltihabı;
- bronko-pulmoner hastalıklar;
- farenjit, rinit, adenoidler, orta kulak iltihabı;
- nazal septumdaki operasyonlar;
- SARS, akut solunum yolu enfeksiyonları ve çeşitli soğuk algınlığı;
- Tonsilor aparatı ile oldukça etkili tedavi;
- sinüs hastalıklarının donanım tedavisi ("guguk kuşu"),
- donanım "pnömasaj";
- İşitsel duyarlılığın belirlenmesi (Odyometri);
- KBB endoskopisi;
- "ses tonu" üzerine fizyoterapi;
- paratonsiller (peri-medial) apsenin açılması, kulak çınlaması;
- novokain ablukası;
- orta kulağın işlevi, kulak zarının hareketlilik derecesi ve işitsel kemikçiklerin iletimi hakkında nesnel bir çalışma yöntemi (Timpanometri);
- akut ve kronik laringotrakeit için ilaçların gırtlak içine infüzyonu.""",
        'education': """Daha yüksek, tıp eğitimi.

Aktobe Devlet Tıp Akademisi, 2000-2006.

Uzmanlık - Pediatri.""",
        'experience': """Genel iş deneyimi - 14 yıl.""",
        'achievements': """"Pediatri. Pediatrik Cerrahi" uzmanlık alanında staj bitirme belgesi, yayın tarihi: 22.06.2007.

"Çocuklar için Kulak Burun Boğaz" uzmanlık sertifikası, yayın tarihi: 18.12.2009.

"Kulak Burun Boğaz (çocuklar için). Odyoloji ve odyoloji" uzmanlık sertifikası, veriliş tarihi: 04/03/2015.

Uzmanlık sertifikası "Kulak Burun Boğaz (odyoloji, ana uzmanlık profiline göre endoskopi) (yetişkin)", yayın tarihi: 30.11.2018.

Uzmanlık sertifikası "Kulak Burun Boğaz (yetişkin, pediatrik). Endoskopi", yayın tarihi: 20.12.2018.

Uzmanlık sertifikası "Kulak burun boğaz (odyoloji, ana uzmanlık profiline göre endoskopi) (yetişkin, pediatrik)", yayın tarihi: 09.01.2019."""
    },
    {
        'id': '7',
        'name': 'Akhmetgaliev',
        'surname': 'Ernar Kokimzhanuly',
        'description': 'Kulak burun boğaz uzmanı (çocuklar ve yetişkinler)',
        'image_path': '/static/images/doctors/doctor3.png',
        'profession': """Tıbbi uygulamada kullanılmasına izin verilen modern önleme, teşhis, tedavi ve rehabilitasyon yöntemlerini kullanarak uzmanlık alanında nitelikli tıbbi bakım sağlar.

Geniş bir profilin ayaktan hasta
kabulüne yol açar : - sinüzit tedavisi;
- pürülan rinit;
- kronik bademcik iltihabı, bademcik iltihabı;
- bronko-pulmoner hastalıklar;
- farenjit, rinit, adenoidler, orta kulak iltihabı;
- nazal septumdaki operasyonlar;
- SARS, akut solunum yolu enfeksiyonları ve çeşitli soğuk algınlığı;
- Tonsilor aparatı ile oldukça etkili tedavi;
- sinüs hastalıklarının donanım tedavisi ("guguk kuşu"),
- donanım "pnömasaj";
- İşitsel duyarlılığın belirlenmesi (Odyometri);
- KBB endoskopisi;
- "ses tonu" üzerine fizyoterapi;
- paratonsiller (peri-medial) apsenin açılması, kulak çınlaması;
- novokain ablukası;
- orta kulağın işlevi, kulak zarının hareketlilik derecesi ve işitsel kemikçiklerin iletimi hakkında nesnel bir çalışma yöntemi (Timpanometri);
- akut ve kronik laringotrakeit için ilaçların gırtlak içine infüzyonu.""",
        'education': """Daha yüksek, tıp eğitimi.
Ospanov Batı Kazakistan Devlet Tıp Üniversitesi, 2007-2014.

Uzmanlık - Genel Tıp.   """,
        'experience': """Toplam iş deneyimi 7 yıldır.""",
        'achievements': """"Genel Tıp" uzmanlık alanında staj bitirme belgesi, uzman doktor niteliği, veriliş tarihi: 11.07.2014

"Çocuklar da dahil olmak üzere Kulak Burun Boğaz" uzmanlığında ikamet tamamlama sertifikası, yayın tarihi: 24.07.2017.

Uzmanlık sertifikası "Kulak Burun Boğaz (ana uzmanlık profilinde odyoloji, endoskopi) (yetişkin, pediatrik)", yayın tarihi: 09/11/2017."""
    },
    {
        'id': '8',
        'name': 'Isentaeva Gulmira',
        'surname': 'Sharafatdinovna',
        'description': 'Kulak Burun Boğaz uzmanı, odyolog (çocuklar ve yetişkinler)',
        'image_path': '/static/images/doctors/doctor4.png',
        'profession': """Tıbbi uygulamada kullanılmasına izin verilen modern önleme, teşhis, tedavi ve rehabilitasyon yöntemlerini kullanarak uzmanlık alanında nitelikli tıbbi bakım sağlar.

Geniş bir profilin ayaktan hasta
kabulüne yol açar : - sinüzit tedavisi;
- pürülan rinit;
- kronik bademcik iltihabı, bademcik iltihabı;
- bronko-pulmoner hastalıklar;
- farenjit, rinit, adenoidler, orta kulak iltihabı;
- nazal septumdaki operasyonlar;
- SARS, akut solunum yolu enfeksiyonları ve çeşitli soğuk algınlığı;
- Tonsilor aparatı ile oldukça etkili tedavi;
- sinüs hastalıklarının donanım tedavisi ("guguk kuşu"),
- donanım "pnömasaj";
- İşitsel duyarlılığın belirlenmesi (Odyometri);
- KBB endoskopisi;
- "ses tonu" üzerine fizyoterapi;
- paratonsiller (peri-medial) apsenin açılması, kulak çınlaması;
- novokain ablukası;
- orta kulağın işlevi, kulak zarının hareketlilik derecesi ve işitsel kemikçiklerin iletimi hakkında nesnel bir çalışma yöntemi (Timpanometri);
- akut ve kronik laringotrakeit için ilaçların gırtlak içine infüzyonu.""",
        'education': """Daha yüksek tıp eğitimi.

1996-2003 yılları arasında M. Ospanov'un adını taşıyan Batı Kazakistan Devlet Tıp Akademisi.

Uzmanlık - Pediatri.""",
        'experience': """Toplam iş tecrübesi 18 yıldır.""",
        'achievements': """"Kulak Burun Boğaz (çocuk)" uzmanlık sertifikası, veriliş tarihi: 24.01.2014.

Uzmanlık sertifikası "Kulak Burun Boğaz (odyoloji) (yetişkin, pediatrik)", yayın tarihi: 27.01.2017.

"Kulak Burun Boğaz (çocuklar)" uzmanlık sertifikası, veriliş tarihi: 06.02.2014.

24.02.2017 tarihli "Kulak Burun Boğaz (odyoloji) (yetişkin)" uzmanlık sertifikası."""
    },


    {
        'id': '9',
        'name': 'Smadiyarova',
        'surname': 'Nelly Sandybaevna',
        'description': 'Kulak burun boğaz uzmanı (çocuklar ve yetişkinler)',
        'image_path': '/static/images/doctors/doctor1.png',
        'profession': """Tıbbi uygulamada kullanılmasına izin verilen modern önleme, teşhis, tedavi ve rehabilitasyon yöntemlerini kullanarak uzmanlık alanında nitelikli tıbbi bakım sağlar.

Geniş bir profilin ayaktan hasta
kabulüne yol açar : - sinüzit tedavisi;
- pürülan rinit;
- kronik bademcik iltihabı, bademcik iltihabı;
- bronko-pulmoner hastalıklar;
- farenjit, rinit, adenoidler, orta kulak iltihabı;
- nazal septumdaki operasyonlar;
- SARS, akut solunum yolu enfeksiyonları ve çeşitli soğuk algınlığı;
- Tonsilor aparatı ile oldukça etkili tedavi;
- sinüs hastalıklarının donanım tedavisi ("guguk kuşu"),
- donanım "pnömasaj";
- İşitsel duyarlılığın belirlenmesi (Odyometri);
- KBB endoskopisi;
- "ses tonu" üzerine fizyoterapi;
- paratonsiller (peri-medial) apsenin açılması, kulak çınlaması;
- novokain ablukası;
- orta kulağın işlevi, kulak zarının hareketlilik derecesi ve işitsel kemikçiklerin iletimi hakkında nesnel bir çalışma yöntemi (Timpanometri);
- akut ve kronik laringotrakeit için ilaçların gırtlak içine infüzyonu.""",
        'education': """Высшее медицинское образование.

Актюбинская государственная медицинская академия, 1994-2000.

Специальность - Лечебное дело.""",
        'experience': """Toplam iş deneyimi 20 yıldır.""",
        'achievements': """"Larenks Hastalıkları" döngüsünde "Kulak Burun Boğaz" uzmanlık sertifikası, yayın tarihi: 25.01.2013.

"Yetişkin Kulak Burun Boğaz" uzmanlık sertifikası, veriliş tarihi: 06.02.2013.

"Mesleki patolojinin güncel sorunları" döngüsünde "Kulak Burun Boğaz" uzmanlık sertifikası, veriliş tarihi: 05.11.2016.

Uzmanlık sertifikası "Kulak Burun Boğaz (ana uzmanlık profiline göre odyoloji, endoskopi) (yetişkin, pediatrik), yayın tarihi: 09.04.2018."""
    },
    {
        'id': '10',
        'name': 'Buzar Alexander',
        'surname': 'Petrovich',
        'description': 'Kulak burun boğaz uzmanı yetişkin, çocuklar',
        'image_path': '/static/images/doctors/doctor2.png',
        'profession': """Tıbbi uygulamada kullanılmasına izin verilen modern önleme, teşhis, tedavi ve rehabilitasyon yöntemlerini kullanarak uzmanlık alanında nitelikli tıbbi bakım sağlar.

Geniş bir profilin ayaktan hasta
kabulüne yol açar : - sinüzit tedavisi;
- pürülan rinit;
- kronik bademcik iltihabı, bademcik iltihabı;
- bronko-pulmoner hastalıklar;
- farenjit, rinit, adenoidler, orta kulak iltihabı;
- nazal septumdaki operasyonlar;
- SARS, akut solunum yolu enfeksiyonları ve çeşitli soğuk algınlığı;
- Tonsilor aparatı ile oldukça etkili tedavi;
- sinüs hastalıklarının donanım tedavisi ("guguk kuşu"),
- donanım "pnömasaj";
- İşitsel duyarlılığın belirlenmesi (Odyometri);
- KBB endoskopisi;
- "ses tonu" üzerine fizyoterapi;
- paratonsiller (peri-medial) apsenin açılması, kulak çınlaması;
- novokain ablukası;
- orta kulağın işlevi, kulak zarının hareketlilik derecesi ve işitsel kemikçiklerin iletimi hakkında nesnel bir çalışma yöntemi (Timpanometri);
- akut ve kronik laringotrakeit için ilaçların gırtlak içine infüzyonu.""",
        'education': """Daha yüksek, tıp eğitimi.

Aktobe Devlet Tıp Akademisi, 2000-2006.

Uzmanlık - Pediatri.""",
        'experience': """Genel iş deneyimi - 14 yıl.""",
        'achievements': """"Pediatri. Pediatrik Cerrahi" uzmanlık alanında staj bitirme belgesi, yayın tarihi: 22.06.2007.

"Çocuklar için Kulak Burun Boğaz" uzmanlık sertifikası, yayın tarihi: 18.12.2009.

"Kulak Burun Boğaz (çocuklar için). Odyoloji ve odyoloji" uzmanlık sertifikası, veriliş tarihi: 04/03/2015.

Uzmanlık sertifikası "Kulak Burun Boğaz (odyoloji, ana uzmanlık profiline göre endoskopi) (yetişkin)", yayın tarihi: 30.11.2018.

Uzmanlık sertifikası "Kulak Burun Boğaz (yetişkin, pediatrik). Endoskopi", yayın tarihi: 20.12.2018.

Uzmanlık sertifikası "Kulak burun boğaz (odyoloji, ana uzmanlık profiline göre endoskopi) (yetişkin, pediatrik)", yayın tarihi: 09.01.2019."""
    },
    {
        'id': '11',
        'name': 'Akhmetgaliev',
        'surname': 'Ernar Kokimzhanuly',
        'description': 'Kulak burun boğaz uzmanı (çocuklar ve yetişkinler)',
        'image_path': '/static/images/doctors/doctor3.png',
        'profession': """Tıbbi uygulamada kullanılmasına izin verilen modern önleme, teşhis, tedavi ve rehabilitasyon yöntemlerini kullanarak uzmanlık alanında nitelikli tıbbi bakım sağlar.

Geniş bir profilin ayaktan hasta
kabulüne yol açar : - sinüzit tedavisi;
- pürülan rinit;
- kronik bademcik iltihabı, bademcik iltihabı;
- bronko-pulmoner hastalıklar;
- farenjit, rinit, adenoidler, orta kulak iltihabı;
- nazal septumdaki operasyonlar;
- SARS, akut solunum yolu enfeksiyonları ve çeşitli soğuk algınlığı;
- Tonsilor aparatı ile oldukça etkili tedavi;
- sinüs hastalıklarının donanım tedavisi ("guguk kuşu"),
- donanım "pnömasaj";
- İşitsel duyarlılığın belirlenmesi (Odyometri);
- KBB endoskopisi;
- "ses tonu" üzerine fizyoterapi;
- paratonsiller (peri-medial) apsenin açılması, kulak çınlaması;
- novokain ablukası;
- orta kulağın işlevi, kulak zarının hareketlilik derecesi ve işitsel kemikçiklerin iletimi hakkında nesnel bir çalışma yöntemi (Timpanometri);
- akut ve kronik laringotrakeit için ilaçların gırtlak içine infüzyonu.""",
        'education': """Daha yüksek, tıp eğitimi.
Ospanov Batı Kazakistan Devlet Tıp Üniversitesi, 2007-2014.

Uzmanlık - Genel Tıp.   """,
        'experience': """Toplam iş deneyimi 7 yıldır.""",
        'achievements': """"Genel Tıp" uzmanlık alanında staj bitirme belgesi, uzman doktor niteliği, veriliş tarihi: 11.07.2014

"Çocuklar da dahil olmak üzere Kulak Burun Boğaz" uzmanlığında ikamet tamamlama sertifikası, yayın tarihi: 24.07.2017.

Uzmanlık sertifikası "Kulak Burun Boğaz (ana uzmanlık profilinde odyoloji, endoskopi) (yetişkin, pediatrik)", yayın tarihi: 09/11/2017."""
    },
    {
        'id': '12',
        'name': 'Isentaeva Gulmira',
        'surname': 'Sharafatdinovna',
        'description': 'Kulak Burun Boğaz uzmanı, odyolog (çocuklar ve yetişkinler)',
        'image_path': '/static/images/doctors/doctor4.png',
        'profession': """Tıbbi uygulamada kullanılmasına izin verilen modern önleme, teşhis, tedavi ve rehabilitasyon yöntemlerini kullanarak uzmanlık alanında nitelikli tıbbi bakım sağlar.

Geniş bir profilin ayaktan hasta
kabulüne yol açar : - sinüzit tedavisi;
- pürülan rinit;
- kronik bademcik iltihabı, bademcik iltihabı;
- bronko-pulmoner hastalıklar;
- farenjit, rinit, adenoidler, orta kulak iltihabı;
- nazal septumdaki operasyonlar;
- SARS, akut solunum yolu enfeksiyonları ve çeşitli soğuk algınlığı;
- Tonsilor aparatı ile oldukça etkili tedavi;
- sinüs hastalıklarının donanım tedavisi ("guguk kuşu"),
- donanım "pnömasaj";
- İşitsel duyarlılığın belirlenmesi (Odyometri);
- KBB endoskopisi;
- "ses tonu" üzerine fizyoterapi;
- paratonsiller (peri-medial) apsenin açılması, kulak çınlaması;
- novokain ablukası;
- orta kulağın işlevi, kulak zarının hareketlilik derecesi ve işitsel kemikçiklerin iletimi hakkında nesnel bir çalışma yöntemi (Timpanometri);
- akut ve kronik laringotrakeit için ilaçların gırtlak içine infüzyonu.""",
        'education': """Daha yüksek tıp eğitimi.

1996-2003 yılları arasında M. Ospanov'un adını taşıyan Batı Kazakistan Devlet Tıp Akademisi.

Uzmanlık - Pediatri.""",
        'experience': """Toplam iş tecrübesi 18 yıldır.""",
        'achievements': """"Kulak Burun Boğaz (çocuk)" uzmanlık sertifikası, veriliş tarihi: 24.01.2014.

Uzmanlık sertifikası "Kulak Burun Boğaz (odyoloji) (yetişkin, pediatrik)", yayın tarihi: 27.01.2017.

"Kulak Burun Boğaz (çocuklar)" uzmanlık sertifikası, veriliş tarihi: 06.02.2014.

24.02.2017 tarihli "Kulak Burun Boğaz (odyoloji) (yetişkin)" uzmanlık sertifikası."""
    }, {
        'id': '13',
        'name': 'Smadiyarova',
        'surname': 'Nelly Sandybaevna',
        'description': 'Kulak burun boğaz uzmanı (çocuklar ve yetişkinler)',
        'image_path': '/static/images/doctors/doctor1.png',
        'profession': """Tıbbi uygulamada kullanılmasına izin verilen modern önleme, teşhis, tedavi ve rehabilitasyon yöntemlerini kullanarak uzmanlık alanında nitelikli tıbbi bakım sağlar.

Geniş bir profilin ayaktan hasta
kabulüne yol açar : - sinüzit tedavisi;
- pürülan rinit;
- kronik bademcik iltihabı, bademcik iltihabı;
- bronko-pulmoner hastalıklar;
- farenjit, rinit, adenoidler, orta kulak iltihabı;
- nazal septumdaki operasyonlar;
- SARS, akut solunum yolu enfeksiyonları ve çeşitli soğuk algınlığı;
- Tonsilor aparatı ile oldukça etkili tedavi;
- sinüs hastalıklarının donanım tedavisi ("guguk kuşu"),
- donanım "pnömasaj";
- İşitsel duyarlılığın belirlenmesi (Odyometri);
- KBB endoskopisi;
- "ses tonu" üzerine fizyoterapi;
- paratonsiller (peri-medial) apsenin açılması, kulak çınlaması;
- novokain ablukası;
- orta kulağın işlevi, kulak zarının hareketlilik derecesi ve işitsel kemikçiklerin iletimi hakkında nesnel bir çalışma yöntemi (Timpanometri);
- akut ve kronik laringotrakeit için ilaçların gırtlak içine infüzyonu.""",
        'education': """Высшее медицинское образование.

Актюбинская государственная медицинская академия, 1994-2000.

Специальность - Лечебное дело.""",
        'experience': """Toplam iş deneyimi 20 yıldır.""",
        'achievements': """"Larenks Hastalıkları" döngüsünde "Kulak Burun Boğaz" uzmanlık sertifikası, yayın tarihi: 25.01.2013.

"Yetişkin Kulak Burun Boğaz" uzmanlık sertifikası, veriliş tarihi: 06.02.2013.

"Mesleki patolojinin güncel sorunları" döngüsünde "Kulak Burun Boğaz" uzmanlık sertifikası, veriliş tarihi: 05.11.2016.

Uzmanlık sertifikası "Kulak Burun Boğaz (ana uzmanlık profiline göre odyoloji, endoskopi) (yetişkin, pediatrik), yayın tarihi: 09.04.2018."""
    },
    {
        'id': '15',
        'name': 'Buzar Alexander',
        'surname': 'Petrovich',
        'description': 'Kulak burun boğaz uzmanı yetişkin, çocuklar',
        'image_path': '/static/images/doctors/doctor2.png',
        'profession': """Tıbbi uygulamada kullanılmasına izin verilen modern önleme, teşhis, tedavi ve rehabilitasyon yöntemlerini kullanarak uzmanlık alanında nitelikli tıbbi bakım sağlar.

Geniş bir profilin ayaktan hasta
kabulüne yol açar : - sinüzit tedavisi;
- pürülan rinit;
- kronik bademcik iltihabı, bademcik iltihabı;
- bronko-pulmoner hastalıklar;
- farenjit, rinit, adenoidler, orta kulak iltihabı;
- nazal septumdaki operasyonlar;
- SARS, akut solunum yolu enfeksiyonları ve çeşitli soğuk algınlığı;
- Tonsilor aparatı ile oldukça etkili tedavi;
- sinüs hastalıklarının donanım tedavisi ("guguk kuşu"),
- donanım "pnömasaj";
- İşitsel duyarlılığın belirlenmesi (Odyometri);
- KBB endoskopisi;
- "ses tonu" üzerine fizyoterapi;
- paratonsiller (peri-medial) apsenin açılması, kulak çınlaması;
- novokain ablukası;
- orta kulağın işlevi, kulak zarının hareketlilik derecesi ve işitsel kemikçiklerin iletimi hakkında nesnel bir çalışma yöntemi (Timpanometri);
- akut ve kronik laringotrakeit için ilaçların gırtlak içine infüzyonu.""",
        'education': """Daha yüksek, tıp eğitimi.

Aktobe Devlet Tıp Akademisi, 2000-2006.

Uzmanlık - Pediatri.""",
        'experience': """Genel iş deneyimi - 14 yıl.""",
        'achievements': """"Pediatri. Pediatrik Cerrahi" uzmanlık alanında staj bitirme belgesi, yayın tarihi: 22.06.2007.

"Çocuklar için Kulak Burun Boğaz" uzmanlık sertifikası, yayın tarihi: 18.12.2009.

"Kulak Burun Boğaz (çocuklar için). Odyoloji ve odyoloji" uzmanlık sertifikası, veriliş tarihi: 04/03/2015.

Uzmanlık sertifikası "Kulak Burun Boğaz (odyoloji, ana uzmanlık profiline göre endoskopi) (yetişkin)", yayın tarihi: 30.11.2018.

Uzmanlık sertifikası "Kulak Burun Boğaz (yetişkin, pediatrik). Endoskopi", yayın tarihi: 20.12.2018.

Uzmanlık sertifikası "Kulak burun boğaz (odyoloji, ana uzmanlık profiline göre endoskopi) (yetişkin, pediatrik)", yayın tarihi: 09.01.2019."""
    },
    {
        'id': '16',
        'name': 'Akhmetgaliev',
        'surname': 'Ernar Kokimzhanuly',
        'description': 'Kulak burun boğaz uzmanı (çocuklar ve yetişkinler)',
        'image_path': '/static/images/doctors/doctor3.png',
        'profession': """Tıbbi uygulamada kullanılmasına izin verilen modern önleme, teşhis, tedavi ve rehabilitasyon yöntemlerini kullanarak uzmanlık alanında nitelikli tıbbi bakım sağlar.

Geniş bir profilin ayaktan hasta
kabulüne yol açar : - sinüzit tedavisi;
- pürülan rinit;
- kronik bademcik iltihabı, bademcik iltihabı;
- bronko-pulmoner hastalıklar;
- farenjit, rinit, adenoidler, orta kulak iltihabı;
- nazal septumdaki operasyonlar;
- SARS, akut solunum yolu enfeksiyonları ve çeşitli soğuk algınlığı;
- Tonsilor aparatı ile oldukça etkili tedavi;
- sinüs hastalıklarının donanım tedavisi ("guguk kuşu"),
- donanım "pnömasaj";
- İşitsel duyarlılığın belirlenmesi (Odyometri);
- KBB endoskopisi;
- "ses tonu" üzerine fizyoterapi;
- paratonsiller (peri-medial) apsenin açılması, kulak çınlaması;
- novokain ablukası;
- orta kulağın işlevi, kulak zarının hareketlilik derecesi ve işitsel kemikçiklerin iletimi hakkında nesnel bir çalışma yöntemi (Timpanometri);
- akut ve kronik laringotrakeit için ilaçların gırtlak içine infüzyonu.""",
        'education': """Daha yüksek, tıp eğitimi.
Ospanov Batı Kazakistan Devlet Tıp Üniversitesi, 2007-2014.

Uzmanlık - Genel Tıp.   """,
        'experience': """Toplam iş deneyimi 7 yıldır.""",
        'achievements': """"Genel Tıp" uzmanlık alanında staj bitirme belgesi, uzman doktor niteliği, veriliş tarihi: 11.07.2014

"Çocuklar da dahil olmak üzere Kulak Burun Boğaz" uzmanlığında ikamet tamamlama sertifikası, yayın tarihi: 24.07.2017.

Uzmanlık sertifikası "Kulak Burun Boğaz (ana uzmanlık profilinde odyoloji, endoskopi) (yetişkin, pediatrik)", yayın tarihi: 09/11/2017."""
    },
    {
        'id': '17',
        'name': 'Isentaeva Gulmira',
        'surname': 'Sharafatdinovna',
        'description': 'Kulak Burun Boğaz uzmanı, odyolog (çocuklar ve yetişkinler)',
        'image_path': '/static/images/doctors/doctor4.png',
        'profession': """Tıbbi uygulamada kullanılmasına izin verilen modern önleme, teşhis, tedavi ve rehabilitasyon yöntemlerini kullanarak uzmanlık alanında nitelikli tıbbi bakım sağlar.

Geniş bir profilin ayaktan hasta
kabulüne yol açar : - sinüzit tedavisi;
- pürülan rinit;
- kronik bademcik iltihabı, bademcik iltihabı;
- bronko-pulmoner hastalıklar;
- farenjit, rinit, adenoidler, orta kulak iltihabı;
- nazal septumdaki operasyonlar;
- SARS, akut solunum yolu enfeksiyonları ve çeşitli soğuk algınlığı;
- Tonsilor aparatı ile oldukça etkili tedavi;
- sinüs hastalıklarının donanım tedavisi ("guguk kuşu"),
- donanım "pnömasaj";
- İşitsel duyarlılığın belirlenmesi (Odyometri);
- KBB endoskopisi;
- "ses tonu" üzerine fizyoterapi;
- paratonsiller (peri-medial) apsenin açılması, kulak çınlaması;
- novokain ablukası;
- orta kulağın işlevi, kulak zarının hareketlilik derecesi ve işitsel kemikçiklerin iletimi hakkında nesnel bir çalışma yöntemi (Timpanometri);
- akut ve kronik laringotrakeit için ilaçların gırtlak içine infüzyonu.""",
        'education': """Daha yüksek tıp eğitimi.

1996-2003 yılları arasında M. Ospanov'un adını taşıyan Batı Kazakistan Devlet Tıp Akademisi.

Uzmanlık - Pediatri.""",
        'experience': """Toplam iş tecrübesi 18 yıldır.""",
        'achievements': """"Kulak Burun Boğaz (çocuk)" uzmanlık sertifikası, veriliş tarihi: 24.01.2014.

Uzmanlık sertifikası "Kulak Burun Boğaz (odyoloji) (yetişkin, pediatrik)", yayın tarihi: 27.01.2017.

"Kulak Burun Boğaz (çocuklar)" uzmanlık sertifikası, veriliş tarihi: 06.02.2014.

24.02.2017 tarihli "Kulak Burun Boğaz (odyoloji) (yetişkin)" uzmanlık sertifikası."""
    }, {
        'id': '18',
        'name': 'Smadiyarova',
        'surname': 'Nelly Sandybaevna',
        'description': 'Kulak burun boğaz uzmanı (çocuklar ve yetişkinler)',
        'image_path': '/static/images/doctors/doctor1.png',
        'profession': """Tıbbi uygulamada kullanılmasına izin verilen modern önleme, teşhis, tedavi ve rehabilitasyon yöntemlerini kullanarak uzmanlık alanında nitelikli tıbbi bakım sağlar.

Geniş bir profilin ayaktan hasta
kabulüne yol açar : - sinüzit tedavisi;
- pürülan rinit;
- kronik bademcik iltihabı, bademcik iltihabı;
- bronko-pulmoner hastalıklar;
- farenjit, rinit, adenoidler, orta kulak iltihabı;
- nazal septumdaki operasyonlar;
- SARS, akut solunum yolu enfeksiyonları ve çeşitli soğuk algınlığı;
- Tonsilor aparatı ile oldukça etkili tedavi;
- sinüs hastalıklarının donanım tedavisi ("guguk kuşu"),
- donanım "pnömasaj";
- İşitsel duyarlılığın belirlenmesi (Odyometri);
- KBB endoskopisi;
- "ses tonu" üzerine fizyoterapi;
- paratonsiller (peri-medial) apsenin açılması, kulak çınlaması;
- novokain ablukası;
- orta kulağın işlevi, kulak zarının hareketlilik derecesi ve işitsel kemikçiklerin iletimi hakkında nesnel bir çalışma yöntemi (Timpanometri);
- akut ve kronik laringotrakeit için ilaçların gırtlak içine infüzyonu.""",
        'education': """Высшее медицинское образование.

Актюбинская государственная медицинская академия, 1994-2000.

Специальность - Лечебное дело.""",
        'experience': """Toplam iş deneyimi 20 yıldır.""",
        'achievements': """"Larenks Hastalıkları" döngüsünde "Kulak Burun Boğaz" uzmanlık sertifikası, yayın tarihi: 25.01.2013.

"Yetişkin Kulak Burun Boğaz" uzmanlık sertifikası, veriliş tarihi: 06.02.2013.

"Mesleki patolojinin güncel sorunları" döngüsünde "Kulak Burun Boğaz" uzmanlık sertifikası, veriliş tarihi: 05.11.2016.

Uzmanlık sertifikası "Kulak Burun Boğaz (ana uzmanlık profiline göre odyoloji, endoskopi) (yetişkin, pediatrik), yayın tarihi: 09.04.2018."""
    },
    {
        'id': '19',
        'name': 'Buzar Alexander',
        'surname': 'Petrovich',
        'description': 'Kulak burun boğaz uzmanı yetişkin, çocuklar',
        'image_path': '/static/images/doctors/doctor2.png',
        'profession': """Tıbbi uygulamada kullanılmasına izin verilen modern önleme, teşhis, tedavi ve rehabilitasyon yöntemlerini kullanarak uzmanlık alanında nitelikli tıbbi bakım sağlar.

Geniş bir profilin ayaktan hasta
kabulüne yol açar : - sinüzit tedavisi;
- pürülan rinit;
- kronik bademcik iltihabı, bademcik iltihabı;
- bronko-pulmoner hastalıklar;
- farenjit, rinit, adenoidler, orta kulak iltihabı;
- nazal septumdaki operasyonlar;
- SARS, akut solunum yolu enfeksiyonları ve çeşitli soğuk algınlığı;
- Tonsilor aparatı ile oldukça etkili tedavi;
- sinüs hastalıklarının donanım tedavisi ("guguk kuşu"),
- donanım "pnömasaj";
- İşitsel duyarlılığın belirlenmesi (Odyometri);
- KBB endoskopisi;
- "ses tonu" üzerine fizyoterapi;
- paratonsiller (peri-medial) apsenin açılması, kulak çınlaması;
- novokain ablukası;
- orta kulağın işlevi, kulak zarının hareketlilik derecesi ve işitsel kemikçiklerin iletimi hakkında nesnel bir çalışma yöntemi (Timpanometri);
- akut ve kronik laringotrakeit için ilaçların gırtlak içine infüzyonu.""",
        'education': """Daha yüksek, tıp eğitimi.

Aktobe Devlet Tıp Akademisi, 2000-2006.

Uzmanlık - Pediatri.""",
        'experience': """Genel iş deneyimi - 14 yıl.""",
        'achievements': """"Pediatri. Pediatrik Cerrahi" uzmanlık alanında staj bitirme belgesi, yayın tarihi: 22.06.2007.

"Çocuklar için Kulak Burun Boğaz" uzmanlık sertifikası, yayın tarihi: 18.12.2009.

"Kulak Burun Boğaz (çocuklar için). Odyoloji ve odyoloji" uzmanlık sertifikası, veriliş tarihi: 04/03/2015.

Uzmanlık sertifikası "Kulak Burun Boğaz (odyoloji, ana uzmanlık profiline göre endoskopi) (yetişkin)", yayın tarihi: 30.11.2018.

Uzmanlık sertifikası "Kulak Burun Boğaz (yetişkin, pediatrik). Endoskopi", yayın tarihi: 20.12.2018.

Uzmanlık sertifikası "Kulak burun boğaz (odyoloji, ana uzmanlık profiline göre endoskopi) (yetişkin, pediatrik)", yayın tarihi: 09.01.2019."""
    },
    {
        'id': '20',
        'name': 'Akhmetgaliev',
        'surname': 'Ernar Kokimzhanuly',
        'description': 'Kulak burun boğaz uzmanı (çocuklar ve yetişkinler)',
        'image_path': '/static/images/doctors/doctor3.png',
        'profession': """Tıbbi uygulamada kullanılmasına izin verilen modern önleme, teşhis, tedavi ve rehabilitasyon yöntemlerini kullanarak uzmanlık alanında nitelikli tıbbi bakım sağlar.

Geniş bir profilin ayaktan hasta
kabulüne yol açar : - sinüzit tedavisi;
- pürülan rinit;
- kronik bademcik iltihabı, bademcik iltihabı;
- bronko-pulmoner hastalıklar;
- farenjit, rinit, adenoidler, orta kulak iltihabı;
- nazal septumdaki operasyonlar;
- SARS, akut solunum yolu enfeksiyonları ve çeşitli soğuk algınlığı;
- Tonsilor aparatı ile oldukça etkili tedavi;
- sinüs hastalıklarının donanım tedavisi ("guguk kuşu"),
- donanım "pnömasaj";
- İşitsel duyarlılığın belirlenmesi (Odyometri);
- KBB endoskopisi;
- "ses tonu" üzerine fizyoterapi;
- paratonsiller (peri-medial) apsenin açılması, kulak çınlaması;
- novokain ablukası;
- orta kulağın işlevi, kulak zarının hareketlilik derecesi ve işitsel kemikçiklerin iletimi hakkında nesnel bir çalışma yöntemi (Timpanometri);
- akut ve kronik laringotrakeit için ilaçların gırtlak içine infüzyonu.""",
        'education': """Daha yüksek, tıp eğitimi.
Ospanov Batı Kazakistan Devlet Tıp Üniversitesi, 2007-2014.

Uzmanlık - Genel Tıp.   """,
        'experience': """Toplam iş deneyimi 7 yıldır.""",
        'achievements': """"Genel Tıp" uzmanlık alanında staj bitirme belgesi, uzman doktor niteliği, veriliş tarihi: 11.07.2014

"Çocuklar da dahil olmak üzere Kulak Burun Boğaz" uzmanlığında ikamet tamamlama sertifikası, yayın tarihi: 24.07.2017.

Uzmanlık sertifikası "Kulak Burun Boğaz (ana uzmanlık profilinde odyoloji, endoskopi) (yetişkin, pediatrik)", yayın tarihi: 09/11/2017."""

    },
]
