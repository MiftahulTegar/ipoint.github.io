from operator import pos
import sys
import mysql.connector as mysql
sys.path.append('...')
from config import app 
from app.models import db, User, Forum, Mengirim_Pesan, Modul
from passlib.hash import sha256_crypt
from flask import Flask, render_template, request, redirect, flash, url_for, session
from flask_mysqldb import MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'kpl'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    return render_template('dashboard/dashboard.html')

#logout ds and mhs
@app.route('/logout')
def logout():
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

# pendaftaran User
@app.route('/registrasi', methods=['GET', 'POST'])
def registrasi():
    if request.method == 'POST':
        nama = request.form['nama']
        jabatan = request.form['jabatan']
        email = request.form['email']
        telp = request.form['telp']
        alamat = request.form['alamat']
        username = request.form['username']
        password = request.form['password']

        password_hash = sha256_crypt.hash(password)

        check_data = User.query.filter_by(nama=nama).first()
        if check_data is not None:
            flash(f'Akun {nama} telah terdaftar', 'info')
            return render_template('register.html')
        
        try:
            input = User(nama=nama, jabatan=jabatan, email=email, telp=telp, alamat=alamat, username=username, password=password_hash)
            db.session.add(input)
            db.session.commit()
            flash('Akun anda berhasil didaftarkan', 'success')
            return redirect(url_for('login'))

        except:
            flash(f'akun yang dibuat sudah ada', 'warning')
            return render_template('register.html')
    return render_template('register.html')

# login User
@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM user WHERE username = %s", [username])
        cek = User.query.filter_by(username=username).first()
        if result > 0:
            data = cur.fetchone()
            password = data['password']
            if sha256_crypt.verify(password_candidate, password):
                session['id'] = cek.id
                session['username'] = username
                session['password'] = password_candidate
                return redirect(url_for('dashboard'))
            else:
                flash('Kata sandi salah!', 'info')
                return render_template('login.html')
        else:
            flash('Akun tidak terdaftar!', 'warning')
    return render_template('login.html')

# masuk Profile
@app.route('/profile', methods = ['GET', 'POST'])
def profile():
    idd = session['id']
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user WHERE id AND id = %s", [idd])
    rv = cur.fetchall()
    cur.close()

    return render_template('dashboard/profile.html', data=rv)

# daftar pengguna
@app.route('/pengguna', methods = ['GET', 'POST'])
def pengguna():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user WHERE jabatan='dosen'")
    rv = cur.fetchall()
    cur.close()
    cus = mysql.connection.cursor()
    cus.execute("SELECT * FROM user WHERE jabatan='mahasiswa'")
    rz = cus.fetchall()
    cus.close()
    return render_template('dashboard/user.html', data=rv, data1=rz)

# lihat FORUM SAYA
@app.route('/forumsaya', methods = ['GET', 'POST'])
def forumsaya():
    idd = session['id']
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM forum f, user u WHERE f.id_user=u.id AND f.id_user = %s", [idd])
    rv = cur.fetchall()
    cur.close()
    return render_template('dashboard/forumsaya.html', data=rv)

# lihat FORUM SEMUA
@app.route('/forum', methods = ['GET', 'POST'])
def forum():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM forum f, user u WHERE f.id_user=u.id")
    rv = cur.fetchall()
    return render_template('dashboard/forum.html', data=rv)

# input FORUM MHS & DS
@app.route('/daftarforum', methods = ['GET', 'POST'])
def daftarforum():
    idd = session['id']
    if request.method == 'POST':
        judul_forum = request.form['judul_forum']
        cek_forum = Forum.query.filter_by(judul_forum=judul_forum).filter_by(id_user=idd).first()
        if cek_forum is not None:
            flash('Forum sudah ada')
            return render_template('dashboard/daftar_forum.html')
        
        input = Forum(judul_forum=judul_forum, id_user=idd)
        db.session.add(input)
        db.session.commit()
        return redirect(url_for('forumsaya'))
    return render_template('dashboard/daftar_forum.html')

# lihat isi FORUM, PESAN, MODUL
@app.route('/pesan/<int:id>', methods = ['GET', 'POST'])
def pesan(id):

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM forum WHERE id = %s", [id])
    b = cur.fetchall()

    bis = mysql.connection.cursor()
    bis.execute("SELECT m.judul, m.file, u.nama ,u.jabatan FROM user u, modul m WHERE m.id_user = u.id AND id_forum = %s", [id])

    bas = mysql.connection.cursor()
    bas.execute("SELECT p.isi_pesan, u.nama ,u.jabatan FROM user u, mengirim_pesan p WHERE p.id_user = u.id AND id_forum = %s", [id])

    cus = mysql.connection.cursor()
    cus.execute("SELECT * FROM mengirim_pesan WHERE id_forum = %s", [id])
    abc = cus.fetchall()

    cas = mysql.connection.cursor()
    cas.execute("SELECT * FROM modul WHERE id_forum = %s", [id])
    ab = cas.fetchall()

    yz = mysql.connection.cursor()
    yz.execute("SELECT * FROM forum f, user u WHERE f.id_user=u.id AND u.jabatan='dosen' AND f.id = %s", [id])

    cus.close()
    return render_template('dashboard/pesan.html', a=b, b=abc, c=ab, d=bas, e=yz, f=bis)

# input PESAN DOSEN & MAHASISWA
@app.route('/pesan/<int:id>/komentar', methods = ['GET', 'POST'])
def mengirimpesan(id):
    idd = session['id']
    cus = mysql.connection.cursor()
    cus.execute("SELECT * FROM forum WHERE id = %s", [id])
    data = cus.fetchall()
    cus.close()
    if request.method == 'POST':
        isi_pesan = request.form['isi_pesan']
        cek_pesan = Mengirim_Pesan.query.filter_by(isi_pesan=isi_pesan).filter_by(id_forum=id).filter_by(id_user=idd).first()
        if cek_pesan is not None:
            flash('Pesan harus bervariasi', 'info')
            return render_template('dashboard/mengirimpesan.html')
        
        input = Mengirim_Pesan(isi_pesan=isi_pesan, id_forum=id, id_user=idd)
        db.session.add(input)
        db.session.commit()
        return redirect(url_for('pesan', id=id))
    return render_template('dashboard/mengirimpesan.html', y=data)

# input MODUL
@app.route('/pesan/<int:id>/modul', methods = ['GET', 'POST'])
def modul(id):
    idd = session['id']
    cus = mysql.connection.cursor()
    cus.execute("SELECT * FROM forum WHERE id = %s", [id])
    data = cus.fetchall()
    cus.close()
    
    if request.method == 'POST':
        judul = request.form['judul']
        file = request.form['file'].encode()
        cek_modul = Modul.query.filter_by(judul=judul).filter_by(file=file).filter_by(id_forum=id).filter_by(id_user=idd).first()
        if cek_modul is not None:
            flash('Modul sudah ada')
            return render_template('dashboard/modul.html')
        
        input = Modul(judul=judul, file=file, id_forum=id, id_user=idd)
        db.session.add(input)
        db.session.commit()
        return redirect(url_for('pesan', id=id))
    return render_template('dashboard/modul.html', z=data)