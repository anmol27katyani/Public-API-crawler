import time
import requests
import random
import os
import mysql.connector
from datetime import datetime
from mysql.connector import Error
import urllib.parse
from math import ceil

file1 = open("deb.txt", "r+")
for i in range(11):
    line = file1.readline() 
    if i==4:
        print (line)
        break

passwd=line[len(line)-17:len(line)-1]
class Database:
    def __init__(self):
        self.cursor = None
        os.system("mysql.server start")
        self.connection = None
        self.create_connection("localhost", "debian-sys-maint", passwd)  # This is used for Docker only

        query1 = "CREATE DATABASE apilatest2"
        self.create_database(query1)

        mycursor = self.connection.cursor()
        mycursor.execute("USE apilatest2")
        #For creating 2 tables
        query2 = "CREATE TABLE categories_table (category VARCHAR(255), count VARCHAR(40) , PRIMARY KEY (category))"
        self.create_table(query2)
        query3 = "CREATE TABLE newapidb (api VARCHAR(255), description VARCHAR(255) , auth VARCHAR(200), https VARCHAR(200), cors VARCHAR(200), link VARCHAR(200) ,category VARCHAR(255))"
        self.create_table(query3)

    def create_connection(self,host_name, user_name, user_password):
        self.connection = None
        self.connection = mysql.connector.connect(host = host_name,user=user_name,passwd=user_password)
        print("Connection to MySQL DB successful")
        

    def create_database(self, query):
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(query)
            print("Database created successfully")
        except Error as e:
            print("The error HAS occurred")

    def create_table(self,query):
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(query)
            print("Table created successfully")
        except Error as e:
            print("The error occurred")

    def insert_category_db(self , category, counting ):
        mycursor = self.connection.cursor()
        count=str(counting)
        mycursor.execute("INSERT INTO categories_table (category,count) VALUES(%s,%s)", (category,count))
        self.connection.commit()

    def insert_apidb_db(self , api,description, auth, https, cors, link,category):
        mycursor = self.connection.cursor()
        mycursor.execute("INSERT INTO newapidb (api,description,auth,https,cors,link,category) VALUES(%s,%s,%s,%s,%s,%s,%s)", (api,description,auth,https,cors,link,category))
        self.connection.commit()
        mycursor.close()
