import sys, pymysql, config
sys.path.append('..')

from config import db 
from datetime import *
from sqlalchemy.dialects.mysql import MEDIUMBLOB

class User(db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(100), unique=True, nullable=False)
    jabatan = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telp = db.Column(db.String(100), unique=True, nullable=False)
    alamat = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Forum(db.Model):

    __tablename__ = "forum"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    judul_forum = db.Column(db.String(100), unique=True, nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Mengirim_Pesan(db.Model):

    __tablename__ = "mengirim_pesan"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isi_pesan = db.Column(db.String(100), unique=True, nullable=False)
    id_forum= db.Column(db.Integer, db.ForeignKey('forum.id'), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Modul(db.Model):

    __tablename__ = "modul"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    judul = db.Column(db.String(100), unique=True, nullable=False)
    file = db.Column(MEDIUMBLOB, nullable=False)
    id_forum = db.Column(db.Integer, db.ForeignKey('forum.id'), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)




    

