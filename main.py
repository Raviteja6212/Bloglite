import csv
import os
from flask import Flask, Request
from flask import render_template
from flask import request
import matplotlib.pyplot as plt
from jinja2 import Template
import sqlite3

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def mainfunction():

    if request.method=="GET":
        return render_template("index.html")
    elif request.method=="POST":
        return render_template("index.html")

@app.route("/home",methods=["GET","POST"])
def homepage():
    if request.method=="POST":
        username = request.form.getlist('username')[0]
        password = request.form.getlist('password')[0]

        try:
            sqliteConnection = sqlite3.connect('database.db')
            cursor = sqliteConnection.cursor()
            print("\n\n\nDatabase created and Successfully Connected to SQLite")

            sqlite_select_Query = "select * from users_data;"
            cursor.execute(sqlite_select_Query)
            record = cursor.fetchall()
            print("\n\nSQLite Database Version is: ", record)
            cursor.close()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        
        for i in record:
            print("\n\n\n\n\n")
            print(i[1],username)
            print(i[2],password)
            if i[1]==username and i[2]==password:
                return render_template("homepage.html")
        return render_template("errorpage.html")

if __name__=="__main__":
    app.run()