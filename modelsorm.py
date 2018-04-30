import sqlite3
from peewee import Model, SqliteDatabase, AutoField, CharField, ForeignKeyField
from datetime import datetime


DB = SqliteDatabase('finance-manager.db')
DB.connect()


class User(Model):
    username = CharField(primary_key=True)


    class Meta:
        database = DB


class Amount(Model):
    user_id = ForeignKeyField(User, backref='amount')
    amount = AutoField()
    date_time = CharField()


    class Meta:
        database = DB

DB.create_tables([User, Amount])
DB.close()
