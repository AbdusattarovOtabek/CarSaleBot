from sqlalchemy import BigInteger, create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.asyncio import async_sessionmaker
from typing import List
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase

from config import DATABASE_URL



# SQLAlchemy sozlamalari
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass



# Foydalanuvchi va mahsulotlar uchun SQLAlchemy modellari

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    username = Column(String, index=True)
    phone_number = Column(String, index=True)
    language = Column(String)
    role = Column(String)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String)
    mark = Column(String)
    color = Column(String)
    mileage = Column(Integer)
    price = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    status = Column(String)
    user = relationship("User")
    product = relationship("Product")

class Favorite(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    user = relationship("User")
    product = relationship("Product")

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
