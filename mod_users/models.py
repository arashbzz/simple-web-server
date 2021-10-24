from sqlalchemy.sql.expression import false
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Integer, Column , String
from app import db


class Users(db.Model):
    __tablename__= 'users'
    id = Column(Integer(), primary_key=True)
    user_name =Column(String(128), nullable=False, unique=True)
    email = Column(String(256), nullable=True)
    password =Column(String(256), nullable=False)
    role = Column(Integer, default=0, nullable=False)

    def generat_passwoord (self,password):
        self.password = generate_password_hash(password)
        return  self.password

    def check_password (self , password, pas):
        return check_password_hash(password,pas)

    def is_admin (self):
        return self.role == 1
