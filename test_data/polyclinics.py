from test_data.doctors import test_doctors_data

test_polyclinics_data = [
    {
        'id': '1',
        'title': 'Kulak Burun Boğaz',
        'description': """"Aigerim" kliniğinin mikroendoskopik kulak burun boğaz bölümü, yetişkinlerin ve en küçük hastaların tedavisinde uzmanlaşmış, kulak, boğaz ve burun hastalıkları için yüksek kaliteli tıbbi bakım sağlar.
Resepsiyon kulak burun boğaz uzmanları, uzun yıllara dayanan deneyime sahip doktorlar, birinci sınıf profesyoneller tarafından gerçekleştirilir. Burada sadece danışma ve teşhis hizmetleri sağlanmaz (endoskopik teknikler, işitme inceleme yöntemleri, burun solunum fonksiyonları), aynı zamanda gerekirse cerrahi müdahale de yapılır.

Kliniğimizin KBB servisi iki ana görevi çözmektedir. Yüksek kaliteli teşhis ve tedavi. Klinik, ortak konsültasyonlara aktif olarak katılır, yurtdışından davet edilen önde gelen uzmanlarla "zor" hastalarla ilgili istişarelere, gerekirse cerrahi tedavi de uygulanır. Ve klinikte daha fazla gözlem ve rehabilitasyon devam ediyor.

Kliniğimiz, doktorun hastasına karşı özenli, ilgili, samimi tutumuna, sorunu anlamasına ve başarılı çözümüne olan inancına dayanmaktadır.""",
        'image_path': '/static/images/polyclinics/kbb.png',
        'doctors': test_doctors_data[0:4],
    },
    {
        'id': '2',
        'title': 'Dermatoloji',
        'description': """Dermatoloji, cilt ve eklerinin incelenmesine ve ayrıca hastalıklarının tedavisi ve önlenmesine adanmış bir klinik tıp dalıdır.

Aşağıdaki belirtiler bulunursa bir dermatolog ile konsültasyon gereklidir:""",
        'image_path': '/static/images/polyclinics/dermatoloji.png',
        'doctors': test_doctors_data[0:4],
    },
    {
        'id': '3',
        'title': 'Üroloji',
        'description': """Üroloji "Klinikler Agerim", üriner ve erkek üreme sistemlerinin hastalıklarını ve fonksiyonel bozukluklarını tedavi eder. Bir üroloğun mesleki yeterlilik yelpazesi, hem erkek hem de kadınlarda, hangi terapötik konservatif (ilaç) tedavi yöntemlerinin kullanıldığını ortadan kaldırmak için geniş bir patolojik durum listesi içerir.""",
        'image_path': '/static/images/polyclinics/uroloji.png',
        'doctors': test_doctors_data[0:4],
    },
    {
        'id': '4',
        'title': 'Endoskopi',
        'description': """Endoskopi, içi boş organların durumunu değerlendirmenin mümkün olduğu bir prosedürdür. Jinekoloji, gastroenteroloji ve cerrahide en büyük prevalansı aldı. Endoskopi sırasında doktorun koordineli eylemleri sayesinde, mide ülseri ve ülseratif kolitten kansere kadar birçok hastalığı tespit etmek mümkündür. Endoskopi yardımı ile iltihaplanma, kanama odaklarını tespit etmek mümkündür. Patolojik sürecin tam yerini belirlemek, doktorun hasta için daha etkili tedavi önermesine yardımcı olur.""",
        'image_path': '/static/images/polyclinics/endoskopi.png',
        'doctors': test_doctors_data[0:4],
    },
    {
        'id': '5',
        'title': 'Psikoloji',
        'description': """Bir psikoloğa başvurmak, herhangi bir kişinin yaşadığı kriz yaşam durumlarında bir çıkış yolu bulmanın en medeni yoludur.

Krizler kendini şu şekilde gösterir:

sağlığın sistemik olarak bozulması (çeşitli ağrılar, yorgunluk, uyku bozukluğu vb.)
duygusal rahatsızlık (artan sinirlilik, kızgınlık, endişeli kaygı, ilgisizlik, sürekli düşük ruh hali arka planı, çeşitli korkular ve "kötü" önseziler)
hayata ilgi kaybı ve anlam duygusu
artan bağımlılık davranışı.""",
        'image_path': '/static/images/polyclinics/psikoloji.png',
        'doctors': test_doctors_data[0:4],
    },
    {
        'id': '6',
        'title': 'Fizyoterapi',
        'description': """Hastalıkların alevlenmesini önlemek, vücudu güçlendirmek, tonu, çalışma kapasitesini ve iyi bir ruh halini korumak için rehabilitasyon, çeşitli hastalıklardan iyileşme döneminde fizyoterapi vazgeçilmezdir.

"Aigerim" kliniğinin fizyoterapi bölümü modern ekipmanlarla donatılmıştır.

Kliniğimizde aşağıdaki fizyoterapi türleri kullanılmaktadır:""",
        'image_path': '/static/images/polyclinics/fizyoterapi.png',
        'doctors': test_doctors_data[0:4],
    },
    {
        'id': '7',
        'title': 'Kardiyoloji',
        'description': """Kalp hastalığı günümüzde en sık görülen hastalıklardan biridir.

Kardiyovasküler hastalıklar genellikle asemptomatiktir. Kişi kendisini tehdit eden tehlikenin farkında bile olmayabilir. Kalp hastalığı dikkatsizliği ve kendi kendine ilaç tedavisini affetmez.

Bir kardiyolog tarafından yıllık muayene, sağlık durumunuza güvenmenizi ve hastalığın erken evresinde olası sapmaları belirlemenizi sağlayacaktır.""",
        'image_path': '/static/images/polyclinics/kardiyoloji.png',
        'doctors': test_doctors_data[0:4],
    },

]
