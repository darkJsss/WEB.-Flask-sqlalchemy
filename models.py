from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

Base = declarative_base()

class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    def set_password(self, password):
        self.password = generate_password_hash(password)
        # имба в чистом виде

    def check_password(self, password):
        return check_password_hash(self.password, password)
        # имба в чистом виде

    def __repr__(self):
        return f"<User '{self.email}'>"