#Importamos librerias 

import sqlite3
import csv

#conexion a la base de datos 
conexion = sqlite3.connect("/home/devkbgeptupsi/Documentos/DataScience/Covid-19DS/Covid-19 datasets/2020_complete_covid-19.db")
#metodo cursor
cursor = conexion.cursor()


#Creamos la tabla 
cursor.execute("CREATE TABLE archived_daily_case_updates (Province_State VARCHAR(30),Country_Region VARCHAR(30),LastUpdate VARCHAR(16), Confirmed INTEGER, Death INTEGER, Recovered INTEGER,Suspected INTEGER,ConfnSusp INTEGER)")


#abrimos el archivo
ds1 = open("/home/devkbgeptupsi/Documentos/DataScience/Covid-19DS/Covid-19 datasets/COVID-19-master/archived_data/archived_daily_case_updates/01-22-2020_1200.csv")
ds2 = open("/home/devkbgeptupsi/Documentos/DataScience/Covid-19DS/Covid-19 datasets/COVID-19-master/archived_data/archived_daily_case_updates/01-23-2020_1200.csv")



row = csv.reader(ds1)
row2 = csv.reader(ds2)

cursor.executemany("INSERT INTO  archived_daily_case_updates VALUES (?,?,?,?,?,?,?,?)", row)
cursor.executemany("INSERT INTO  archived_daily_case_updates VALUES (?,?,?,?,?,?,?,?)", row2)


cursor.execute("SELECT * FROM archived_daily_case_updates")

print(cursor.fetchall())

conexion.commit()
conexion.close()