# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image suki_sleepy = im.Scale("../images/suki/suki sleepy.png", 800,800)
image suki_smile = im.Scale("../images/suki/suki smile.png", 500, 500)
image suki_normal = im.Scale("../images/suki/suki normal.png", 800, 800)
image suki_shock = im.Scale("../images/suki/suki shock.png", 800, 800)
image suki_mandi = im.Scale("../images/suki/suki mandi.png", 800, 800)
image suki_TN = im.Scale("../images/suki/suki towel normal.png", 800, 800)
image suki_WS = im.Scale("../images/suki/suki_WS.png", 800, 800)
image suki_WS = im.Scale("../images/suki/suki_WS.png", 500, 500)
image suki_D = im.Scale("../images/suki/suki delighted.png", 500, 500)
image huda_N = im.Scale("../images/huda/huda normal.png", 500, 500)
image huda_N2 = im.Scale("../images/huda/huda normal2.png", 500, 500)
image hudasmink = im.Scale("../images/huda/hudasmink.png", 500, 500)
image huda_M = im.Scale("../images/huda/hudamringis.png", 500, 500)


#deklarasi background
image bg_awal = "../images/bg/viewatas.jpeg"
image bathroom = "../images/bg/small_bathroom.jpeg"
image kamar = "../images/bg/room.jpeg"
image street = "../images/bg/StreetDay.png"
image taman = im.Scale("../images/bg/taman_day.jpeg", 1280, 790)
image sdgs = im.Scale("../images/bg/sdgs.jpeg", 1280,850)
image Ex = im.Scale("../images/bg/pameran_outdoor.jpeg", 1280,850)
image depankelas = im.Scale("../images/bg/depankelas.jpeg", 1280,790)

define alarm = "../audio/alarm.wav"

# Deklarasikan karakter yang digunakan di game.
define s = Character('suki', color="#c8ffc8")
define n = Character('', color="#e6f14b")
define h = Character('rapip', color="#2d16de")

# Game dimulai disini.
label start:

    scene black with dissolve
    show bg_awal with fade
    "Di pagi yang cerah, Suki berangkat ke sekolah di Tokyo dengan penuh semangat. Hari itu, sekolahnya mengadakan pameran Global Goals yang diadakan oleh PBB" 
    scene black
    show taman with dissolve
    show suki_WS with dissolve
    "Suki sangat antusias untuk belajar lebih banyak tentang bagaimana dia bisa berkontribusi dalam mencapai tujuan tersebut."
    hide suki_WS with fade
    show suki_smile with dissolve
    s "Oh, pameran Global Goals! Aku penasaran apa yang bisa kulakukan untuk membantu."

    scene black with fade
    "Sesampainya di sekolah, Suki langsung menuju aula tempat pameran diadakan. Dia melihat berbagai stan yang menjelaskan berbagai tujuan global. Stan yang paling menarik perhatiannya adalah tentang tujuan “Aksi Iklim”."
    
    show Ex with Dissolve(4.0)
    "Saat berjalan dari satu stan ke stan lainnya, Suki melihat Haruto, teman sekelasnya."
    show suki_D at left with moveinbottom
    s "eh hai rapip, kamu juga disini"
    show huda_M at right with moveinbottom
    show Ex with vpunch
    h "ehehe iya, ini sangat menarik perhatianku"
    show suki_smile at left with dissolve
    s "rapip, ini sangat menarik. menurutmu apa kita bisa melakukan sesuatu di sekolah untuk membantu?"
    show huda_N2 at right with dissolve
    h "emm mungkin kita bisa mulai dari hal-hal kecil, seperti mengurangi penggunaan plastik, menanam pohon, dan mendaur ulang sampah."
    show suki_WS at left with dissolve
    s "ide yang bagus upip" 
    show hudasmink at right with dissolve
    h "yoshhh"
    # hide suki_D huda_N2 with fade
    
    show depankelas with dissolve
    "Setelah pameran, Suki dan Rapip sepakat untuk memulai proyek lingkungan di sekolah mereka. Mereka mengumpulkan teman-teman sekelas dan membentuk sebuah kelompok yang mereka sebut “Green Guardians”."    
    
return
