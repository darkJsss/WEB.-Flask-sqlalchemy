from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..db_session import SqlAlchemyBase

class Work(SqlAlchemyBase):
    __tablename__ = 'works'

    id = Column(Integer, primary_key=True, autoincrement=True)
    job_title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_date = Column(DateTime, default=datetime.utcnow())
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="works")