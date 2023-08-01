#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

SQLALCHEMY_DATABASE_URL = 'sqlite://./sql_app.db'

engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

class Base(DeclarativeBase):
    pass
