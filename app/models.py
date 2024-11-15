from sqlalchemy import Column, Integer, String, Boolean, Float, Text
from sqlalchemy.orm import relationship
from app.database import Base


class SpyCats(Base):
    __tablename__ = "spy_cats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    years_of_experience = Column(Integer, nullable=False)
    breed = Column(String, nullable=False)
    salary = Column(Float, nullable=False)

    mission = relationship("Mission", back_populates="cat")


class Mission(Base):
    __tablename__ = "missions"

    id = Column(Integer, primary_key=True, index=True)
    cat_id = Column(Integer, ForeignKey="spy_cats.id")
    complete = Column(Boolean, default=False)
    cat = relationship("SpyCats", back_populates="missions")
    targets = relationship("Target", back_populates="mission")


class Target(Base):
    __tablename__ = "targets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    complete = Column(Boolean, default=True)
    mission_id = Column(Integer, ForeignKey="mission.id")
    notes = Column(Text, nullable=True)
    mission = relationship("Mission", back_populates="targets")
