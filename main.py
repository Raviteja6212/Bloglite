import csv
import os
from flask import Flask, Request, flash
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
            sqlite_select_Query = "select * from users_data;"
            cursor.execute(sqlite_select_Query)
            record = cursor.fetchall()
            cursor.close()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        
        for i in record:
            if i[1]==username and i[2]==password:
                return render_template("homepage.html")
        return render_template("errorpage.html")

@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method=="GET":
        return render_template("singupPage.html")
    else:
        username = request.form.getlist('username')[0]
        password = request.form.getlist('password')[0]

        try:
            sqliteConnection = sqlite3.connect('database.db')
            cursor = sqliteConnection.cursor()
            sqlite_select_Query = "select * from users_data;"
            cursor.execute(sqlite_select_Query)
            record = cursor.fetchall()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        
        for i in record:
            if i[1]==username:
                return render_template("singupPage.html",message="Username already exists !!")
        
        Insert_Query = "INSERT INTO users_data (username,password) VALUES (?,?)"
        cursor.execute(Insert_Query,(username,password))
        sqliteConnection.commit()
        cursor.close()
        
        return render_template("index.html", message="User successfully created. You can log in:)")



if __name__=="__main__":
    app.run()
    