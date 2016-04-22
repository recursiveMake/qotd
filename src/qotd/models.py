from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Quote(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    author = Column(String(24))
    insight = Column(String(2048))

    def __repr__(self):
        return "<Quote(author='%s', insight='%s')>" % (self.author, self.insight)
