Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1.Langkah pertama yang saya lakukan adalah membuat repository baru di GitHub dengan nama “snitchfootball”. Repository ini saya gunakan untuk menyimpan seluruh kode project Django yang saya kerjakan, sekaligus menjadi sarana version control agar setiap perubahan dapat dicatat dengan rapi. Setelah repository berhasil dibuat, saya melakukan clone repository tersebut ke komputer lokal sehingga saya bisa langsung memulai pengerjaan project.
2. Setelah repository siap, saya menyiapkan lingkungan pengembangan Python dengan membuat sebuah virtual environment. Tujuannya adalah agar dependency project tidak bercampur dengan dependency lain di sistem. Saya kemudian menginstall Django beserta library tambahan seperti python-decouple, gunicorn, dan whitenoise. Semua dependency yang terpasang saya simpan ke dalam file requirements.txt agar lebih mudah ketika project nanti dideploy ke server.
3. Langkah selanjutnya adalah membuat project Django baru dengan nama config. Untuk menjaga keamanan, saya menambahkan sebuah file .env yang berisi informasi sensitif seperti SECRET_KEY, DEBUG, dan ALLOWED_HOSTS. File .envini kemudian saya hubungkan dengan settings.py menggunakan library decouple, sehingga konfigurasi project menjadi lebih aman, fleksibel, dan mudah dikelola.
4. Setelah project utama selesai dibuat, saya membuat sebuah app baru bernama main menggunakan perintah startapp. App ini lalu saya tambahkan ke dalam daftar INSTALLED_APPS di file settings.py agar Django mengenalinya sebagai bagian dari project.
5. Di dalam app main, saya membuat sebuah model bernama Product yang memiliki beberapa atribut, yaitu name, description, price, stock, dan created_at. Model ini berfungsi sebagai representasi data produk yang akan disimpan di dalam database. Setelah model selesai dibuat, saya menjalankan perintah migrasi agar Django membuat tabel yang sesuai di database.
6. Supaya data produk bisa ditampilkan kepada pengguna, saya membuat sebuah fungsi view di file views.py untuk mengambil data dari model Product dan merendernya ke template main.html. Untuk mengatur akses URL, saya menambahkan file urls.py di dalam app main, dan membuat routing sederhana yang menghubungkan view tersebut dengan template. Template main.html sendiri saya letakkan di dalam folder templates/main/ berisi kode HTML untuk menampilkan daftar produk.
7. Selanjutnya, saya menghubungkan project utama dengan app main dengan cara menambahkan include('main.urls') pada file config/urls.py. Dengan cara ini, setiap kali pengguna mengakses URL utama project, Django akan langsung diarahkan ke routing yang ada di app main.
8. Setelah semua berjalan baik di lokal, saya melakukan deployment project ke PWS. Pertama, saya melakukan push seluruh kode project ke repository GitHub. Kemudian di PWS, saya membuat project baru, melakukan clone repository, menginstall seluruh dependency dari requirements.txt, serta menjalankan migrasi database. Setelah itu, saya menjalankan collectstatic untuk mengatur static files, menambahkan konfigurasi environment sesuai isi .env, dan mengatur file WSGI agar mengarah ke project Django. Terakhir, saya melakukan restart web app, dan project “snitchfootball” berhasil berjalan di server PWS.

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan 
antara urls.py, views.py, models.py, dan berkas html.
https://www.canva.com/design/DAGygS6WKXY/qlOy5lZ1ltgvN5wtyG3xdg/view?utm_content=DAGygS6WKXY&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h38237d2240

Jelaskan peran settings.py dalam proyek Django!
peran settings.py dalam proyek Django adalah sebagai pusat kongfigurasi aplikasi Django. terdapat pengaturan keamanan seperti SECRET_KEY, DEBUG, dan ALLLOWED_HOST, daftar aplikasi pada INSTALLED_APPS, serta middleware. file ini juga mengatur URL utama yang digunakan. selain itu, menhatur password, zona waktu, bahasa, serta key default model yang tersusun dengan rapi dan aman saat dijalankan.

Bagaimana cara kerja migrasi database di Django?
cara kerja migrasi database di Django adalah dengan mencatat perubahan model ke file menggunakan makemigrations. selain itu juga menggunakan migrate untuk mengeksekusi perintah ke database. intinya untuk menjaga struktur database agar selalu sesuai dengan kode.

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
menurut saya, framework Django dijadikan permulaan dalam pembelajaran perangkat lunak karena Django memiliki kebutuhan umum yang sudah tersedia sehingga mudah digunakan oleh pemula. dengan menggunakan model template view yang tersusun dengan rapi dan jelas sehingga mahasiswa dapat memahami cara kerja aplikasi dengan terstruktur.

Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Secara umum, penjelasan materi sudah cukup membantu, tetapi akan lebih baik jika tujuan pembelajaran dijelaskan dengan lebih jelas di awal sehingga mahasiswa paham arah dan tujuan dari praktikum yang sedang dijalani. Selain itu, contoh kode yang diberikan sebaiknya ditampilkan secara utuh, bukan hanya potongan, karena bagi pemula seringkali sulit menyambungkan potongan kode


======== TUGAS 3 ========
Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery kita perlukan agar data pada server bisa digunakan oleh berbagai macam perangkat misalnya web, mobile, atau aplikasi lainnya dengan format standar. dengan data delivery, sistem akan lebih fleksibel, mudah diintegrasikan, dan dapat berkembang tanpa mengubah struktur utama atau inti dari aplikasi.

Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
diantara XML dan JSON, keduanya memiliki kelebihannya masing-masing, namun JSON merupakan turunan langsung dari JavaScript Object yang dapat digunakan dengan mudah di aplikasi web modern tanpa proses yang panjang. selain itu, JSON lebih efesien karena lebih ringan, ringkas, mudah dipahami dan diproses.

Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
is_valid adalah method dari Django yang akan mengakibatkan Django mengikat data ke form dan ketika dipanggil, Django akan mengecek apakah data sesuai dengan tipenya dan apakah semua field sudah terisi, yang akan mengembalikan True atau False.


Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
CSRF (Cross-Site Request Forgery) adalah salah satu serangan yang paling umum pada aplikasi web. serangan ini bekerja dengan menipu browser user dengan mengirimkan request berbahaya ke server, misalnya seorang user melakukan login ke suatu situs online, lalu penyerang mengirimkan link berbahaya ke situs korban, yang jika ditekan akan mengakibatkan akun dari user (korban) dibajak. oleh karena itu kita dapat mencegah hal tersebut dengan cara menambahkan csrf_token yang merupakan salah satu mekanisme pertahanan di Django. setiap kali form ditampilkan, Django akan menyediakan token unik yang bisa digunakan dalam waktu tertentu sampai sesinya berakhir. apabila kita tidak menambahkan csrf_token di form, maka Django akan menganggap form tersebut tidak aman dan menjadi celah bagi penyerang untuk menyerang seperti mengganti password, hapus data, dan transaksi illegal. 


Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. langkah pertama yang saya lakukan adalah membuat direktori baru yaitu templates dan membuat html bernama base.html, dan mengisi html tersebut dengan potongan kode yang telah disediakan di tutorial2 sebelumnya.
2. selanjutnya saya membuka settings.py dan menambahkan BASE_DIR pada 'DIRS' menjadi [BASE_DIR / 'templates'].
3. setelah itu, pada direktori templates pada main, saya merubah menggunakan main.html menjadi base.html sebagai template utama yang akan digunakan.
4. saya membuat folder baru pada direktori main, yaitu forms.py yang berisi class ProductForm(ModelForm) yang didalamnya terdapat fields yang saya sesuaikan dengan kategori yang ada pada models.py yang telah saya buat pada tugas2, yaitu "name", "price", "description", "thumbnail","category", "is_featured".
5.  selanjutnya saya membuka views.py dan menambahkan import dan method baru seperti create_product dan show_product, selain itu saya juga mengedit beberapa potongan kode pada main.html dan urls.py menyesuaikan dari kebutuhan yang diminta pada tugas3.
6. setelah menyesuaikan kode dengan perintah pada tugas3, saya mengecek dengan memerintah python manage.py runserver dan membuka localhost untuk memastikan apakah tampilan sudah sesuai dengan ekpektasi tugas.
7. pada langkah selanjutnya adalah mengembalikan data dalam bentuk xml , json, xml id, dan json id. pada pengerjaan ini saya hanya mengikuti instruksi dari tutorial2, karena sama saja dan kode tetap berjalan dengan baik. dan selanjutnya saya menguji keempat link pada postman hingga output atau tampilannnya sesuai ekspektasi ketika dirun menggunakan xml, json, xml id, dan json id, lalu hasilnya saya screenshot dan cantumkan link nya pada readme bagian paling akhir di penjelasan ini. (pada line 55)

Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Secara umum, penjelasan materi sudah cukup membantu, tetapi akan lebih baik jika tujuan pembelajaran dijelaskan dengan lebih jelas di awal sehingga mahasiswa paham arah dan tujuan dari praktikum yang sedang dijalani. Selain itu, contoh kode yang diberikan sebaiknya ditampilkan secara utuh, bukan hanya potongan, karena bagi pemula seringkali sulit menyambungkan potongan kode.

screenshot hasil postman :
https://drive.google.com/drive/folders/1fr3H8o_B6l1rBhPQ_pLHSHl5DUbasl3d?usp=sharing

========================TUGAS 4========================
Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
Django AuthenticationForm adalah fungsi bawaan dari Django yang berfungsi untuk melakukan autentikasi dan login saat autentikasi berhasil, mencocokkan input username dan password dengan data. kelebihannya adalah tidak memerlukan form validasi manual dan ketika username atau password salah, secara otomatis akan menampilkan pesan error. kekurangannya adalah keamanan sangat sederhana hanya meminta username dan password tanpa pengamanan tambahan seperti OTP atau captcha dan penggunaannya masih terbatas saat melakukan login.

Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
perbedaan autentikasi dan otorisasi yaitu autentikasi merupakan proses verifikasi identitas dari pengguna yaitu mengisi username dan password, sedangkan otorisasi merupakan proses yang memberikan akses apa saja yang bisa dilakukan olher pengguna saat pengguna telah berhasil login. implementasi pada Django yaitu meng-import 'from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login' dan '@login_required(login_url='/login')' 

Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
kelebihan session yaitu penyimpanan data menjadi lebih aman dan data yang disimpan besar dan kompleks, sedangkan kekurangannya adalah server menjadi terbebani oleh user. kelebihan cookies adalah tidak membebani server, penggunaan yang sederhana, dan bisa diakses terus-menerus meskipun browser ditutup, sedangkan kekurangannya adalah bisa disalahgunakan misalnya lewat XSS dan mudah dimanipulasi.

Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
ada beberapa ancaman keamanan dalam penggunaan cookies, diantaranya sebagai berikut :
-ancaman XSS, cross site scripting menjadi salah satu risiko penggunaan cookies karena penyerang dapat menyisipkan script untuk mencuri cookie dari browser.
-jika sessionID ada di cookie yang berhasil diambil oleh penyerang, penyerang tersebut bisa berpura-pura menjadi user dan mengambil semua data pribadi pengguna
-data user dapat dimanipulasi oleh penyerang karena cookie disimpan di sisi client
-kapasitas cookie terbatas
cara Django mengatasi hal tersebut adalah dengan cara menyediakan beberapa mekanisme keamanan untuk meminimalisir risiko tersebut, diantaranya adalah data user tidak disimpan di cookie melainkan di session id saja, Django menambahkan token CSRF untuk melindungi data.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
1. langkah pertama yang saya lakukan adalah menggunakan berkas tugas3 untuk ditambahkan fitur terbaru intuk Snitch football.
2. saya menambahkan import UserCreationForm untuk mengimplementasikan fitur pendaftaran dari user dalam web yang memungkinkan pengguna baru dapat mendaftar dengan mudah di situs web.
3. selanjutnya meng-import messages, dan register untuk fitur registrasi pada web.
4. selanjutnya saya membuat fungsi login dan logout. saya membuat fungsi login dengan mengimport authentication login, agar jika autentikasi berhasil, user bisa login. saya membuat fungsi logout dengan mengimport logout bersamaan dengan autentikasi dan login. logout akan menghapus sesi pengguna yang masuk dan kembali ke halaman login user.
5. selanjutnya saya melakukan registrasi beberapa akun dan membuat password yang berbeda untuk login, dan dari setiap akun tersebut saya menambahkan macam-macam product yang nantinya bisa ditampilkan di all product maupun di product yang dibuat sendiri oleh user yang mengimplementasikan menghubungkan product dengan user.
7. yang terakhir untuk fitur last login saya menggunakan potongan kode 'if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response' yang berfungsi untuk mendaftarkab cookie di response dengan timestamp 


==================================TUGAS 5=================================
Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
jika terdapat beberapa CSS selector, browser akan memilih berdasarkan tingkat kekhususan selector, selector dengan kekhususan tertinggi akan diprioritaskan. urutan prioritasnya berlaku: 
!important
Inline style (<div style="color:red">)
ID selector (#id-name)
Class, attribute, pseudo-class (.btn, :hover)
Tag HTML (p, h1)

Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
pada project django ini, semua halaman dimulai dari main.html, detail product, register, login, hingga register serta lainnya sudah dibuat responsive menggunakan tailwind. responsive design sangat penting untuk sebuah web karena user membuka web bisa jadi menggunakan handphone atau komputer, nah jika tidak responsive, bentuk web akan berantakan di layar kecil, seperti beberapa tombol tidak keluar di layar dan susunan yang tidak rapi. contoh aplikasi yang sudah menerapkan responsive design adalah Instagram, Facebook, X, dan Whatsapp.

Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Padding adalah ruang di dalam elemen, tepatnya jarak antara konten (misalnya teks nama produk atau harga) dengan batas dalam elemen. Dengan kata lain, padding membuat konten “bernapas” di dalam box. Border adalah garis tepi yang membungkus padding dan konten; border sering digunakan sebagai aksen visual seperti garis emas di sekitar kartu produk yang kita buat. Margin adalah ruang di luar border, yaitu jarak antara elemen tersebut dengan elemen lain di sekitarnya, misalnya jarak antar card produk di halaman utama.
Di proyek ini, kita mengimplementasikan ketiga hal tersebut menggunakan utilitas Tailwind. Misalnya, p-5 digunakan untuk memberi padding pada card agar teks produk tidak menempel ke tepi card. Kemudian border border-yellow-600 digunakan untuk menambahkan garis emas di sekitar card agar sesuai dengan tema Harry Potter. Sedangkan m-4 dipakai sebagai margin untuk memberi jarak antar card produk sehingga layout grid lebih rapi. Dengan kombinasi margin, border, dan padding, tampilan halaman jadi lebih terstruktur, mudah dibaca, dan nyaman dilihat, baik di layar besar maupun kecil.


Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox (Flexible Box) digunakan untuk mengatur elemen dalam satu dimensi, baik itu baris atau kolom. Flexbox memudahkan kita untuk meratakan elemen ke tengah, memberi jarak antar item, atau mendistribusikan ruang kosong secara otomatis. Misalnya pada navbar.html
Grid Layout digunakan untuk mengatur elemen dalam dua dimensi: baris dan kolom. Konsep grid sangat bermanfaat untuk menampilkan daftar produk dalam bentuk card.
Kedua konsep ini saling melengkapi: flexbox sangat berguna untuk menata bagian-bagian kecil seperti form input atau navbar, sedangkan grid lebih cocok untuk layout utama seperti daftar produk. Dengan memanfaatkan keduanya, aplikasi Django kita bisa tampil rapi, responsif, dan tetap konsisten di berbagai perangkat.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. Menambahkan Tailwind ke aplikasi
Saya mengintegrasikan Tailwind ke dalam project Django agar lebih mudah styling. File base.html
sudah dihubungkan dengan Tailwind, dan setiap halaman (login, register, main, detail, create, edit)
saya beri class-class Tailwind untuk konsistensi styling.
2. Menambahkan fitur Edit Product pada aplikasi
Saya membuat view edit_product di views.py, menambahkan path /product//edit di urls.py, serta
menambahkan tombol Edit di card produk. Halaman edit_product.html dibuat dengan form pre-filled
dari ProductForm.
3. Menambahkan fitur Hapus Product pada aplikasi
Saya membuat view delete_product yang menghapus object lalu redirect ke halaman utama.
Tombol Delete ditampilkan di card produk hanya jika user adalah pemilik produk.
4. Menambahkan Navigation Bar pada aplikasi
Saya membuat file navbar.html yang reusable, lalu include di semua template dengan {% include
'navbar.html' %}.
5. Konfigurasi static files pada aplikasi
Saya memastikan konfigurasi STATIC_URL dan STATICFILES_DIRS sudah benar di settings.py,
sehingga Tailwind CSS, custom CSS, dan gambar (misalnya no-product.png) bisa di-load dengan
{% static %}.
6. Styling pada aplikasi dengan Tailwind dan external CSS
Selain Tailwind, saya juga menambahkan sedikit custom CSS untuk form (form-style) supaya input
dan checkbox lebih menarik. Tema keseluruhan saya buat Harry Potter dengan kombinasi hijau
tua, emas, dan aksen kuning.
