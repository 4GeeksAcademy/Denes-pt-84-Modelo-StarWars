import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String)
    email = Column(String(100), nullable=False, unique=True)
    personaje = relationship('Characters', back_populates ='person')
    favourite_planets = relationship('Favourite_Planets', back_populates = 'person')
    favourite_characters = relationship('Favourite_Characters', back_populates = 'person')
    favourite_vehicles = relationship('Favourite_vehicle', back_populates = 'person')


class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    person_id = Column(Integer, ForeignKey('user.id'))
    person = relationship('User', back_populates='personaje')
    planetas = relationship('Planets', back_populates = 'personaje')
    vehicle = relationship('Vehicles', back_populates = 'character')

class Planets(Base): 
    __tablename__ = 'planets'
    id = Column(Integer, primary_key = True)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    name = Column(String, nullable=True, unique=True)
    color = Column(String)
    personaje = relationship('Characters', back_populates ='planetas')

class Favourite_Planets(Base):
    __tablename__ = 'favourites_planets'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    person = relationship('User', back_populates='favoreites_planets')

class Favourite_Characters(Base): 
    __tablename__ = 'favourite_characters'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    person = relationship('User', back_populates='favourites_characters')

class Favourite_Vehicles(Base): 
    __tablename__ = 'favourite_vehicles'
    id = Column(Integer, primary_key = True)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    person = relationship('User', back_populates='favourite_vehicles')


class Vehicles(Base): 
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    characterId = Column(Integer, ForeignKey('characters.id'))
    name = Column(String, nullable=True)
    height = Column(String)
    character = relationship('Characters', back_populates='vehicle')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
