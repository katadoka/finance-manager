import sqlite3
from peewee import Model, SqliteDatabase, DateTimeField, ForeignKeyField, FloatField, CharField
from datetime import datetime


DB = SqliteDatabase('finance-manager.db')
DB.connect()


class User(Model):
    username = CharField(primary_key=True)


    class Meta:
        database = DB


class Amount(Model):
    user = ForeignKeyField(User, backref='amount')
    amount = FloatField()
    date_time = DateTimeField()


    class Meta:
        database = DB

DB.create_tables([User, Amount])
DB.close()
