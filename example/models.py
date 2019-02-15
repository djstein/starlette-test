from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    complete = Column(Boolean)

    def __repr__(self):
        return f"<Task(id={self.id}, title={self.title}, complete={self.complete}"
