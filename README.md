Nama : Ardelia Yasmin Yolandaya
NPM	 : 57419295

## Pengenalan

_Django_ merupakan salah satu _framework_ yang menggunakan bahasa pemrograman _python_.
_Framework_ sangat berguna dalam pengembangan web karena sudah menyediakan komponen-komponen 
yang dibutuhkan untuk membuat dan menjalankan suatu web, tanpa harus mulai dari nol. 
Sebelum memulai pengembangan web menggunakan Django, penting untuk memahami apa itu virtual environemnt (virtualenv).
Virtual environment (lingkungan virtual) berfungsi untuk memisahkan pengaturan dan _package_ yang di _install_  
pada setiap _Django project_ sehingga perubahan yang dilakukan pada satu _project_ tidak mempengaruhi _project_ lainnya. 
Dengan kata lain, setiap _Django project_ sebaiknya memiliki _virtualenv_ nya sendiri. 


## Cara menjalankan Project ini


1. Buatlah sebuah virtual environment pada root directory $ virtualenv env.

2. Aktifkan virtual environment $ source env/bin/activate (Linux dan OSX) atau C:\Desktop\[NamaFolder]>env\Scripts\activate (Windows)

3. Install seluruh dependency  pip install -r requirements.txt

4. Migrasikan aplikasi (env) $ [NamaFolder] cobaweb/py manage.py migrate (Linux dan OSX) atau (env) C:\Desktop\[NamaFolder]>cobaweb\py manage.py migrate (Windows)

5. Jalankan aplikasi (env) $ [NamaFolder] cobaweb/py manage.py runserver (Linux dan OSX) atau (env) C:\Desktop\[NamaFolder]>cobaweb\py manage.py runserver (Windows)

6. Lalu buka Browser dan ketikkan localhost:8000 kemudian tekan enter, maka browser akan menampilan isi project ini.