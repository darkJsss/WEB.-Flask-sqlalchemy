from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from ..db_session import SqlAlchemyBase

class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)
        # имба в чистом виде

    def check_password(self, password):
        # имба в чистом виде
        return check_password_hash(self.hashed_password, password)

    def __repr__(self):
        return f"<User '{self.email}'>"