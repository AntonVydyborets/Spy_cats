from sqlalchemy import Column, Integer, String, Boolean, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class SpyCats(Base):
    __tablename__ = "spy_cats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    years_of_experience = Column(Integer, nullable=False)
    breed = Column(String, nullable=False)
    salary = Column(Float, nullable=False)

    missions = relationship("Mission", back_populates="cat")


class Mission(Base):
    __tablename__ = "missions"

    id = Column(Integer, primary_key=True, index=True)
    cat_id = Column(Integer, ForeignKey("spy_cats.id"))
    complete = Column(Integer, default=0) 
    cat = relationship("SpyCats", back_populates="missions")
    targets = relationship("Target", back_populates="mission", primaryjoin="Mission.id == Target.mission_id")


class Target(Base):
    __tablename__ = "targets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    complete = Column(Integer, default=0) 
    mission_id = Column(Integer, ForeignKey("missions.id"))
    notes = Column(Text, nullable=True)
    mission = relationship("Mission", back_populates="targets")
