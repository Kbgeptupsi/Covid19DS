#Importamos librerias 

import sqlite3
import csv

#conexion a la base de datos 
conexion = sqlite3.connect("/home/devkbgeptupsi/Documentos/DataScience/Covid-19DS/Covid-19 datasets/2021Case_Diarie-19.db")
#metodo cursor
cursor = conexion.cursor()


#Creamos la tabla 
cursor.execute("CREATE TABLE case_diaries2020 (FIPS INTEGER,Admin2 VARCHAR(20),Province_State VARCHAR(30),Country_Region VARCHAR(30),Last_Update VARCHAR(30),Lat VARCHAR(15),Long_ VARCHAR(15),Confirmed VARCHAR(10),Deaths VARCHAR(10),Recovered VARCHAR(15),Active VARCHAR(10),Combined_Key VARCHAR(30))")


#abrimos el archivo


# Hacer que busque por año para abrir y adjuntar lo de ese año
#con un for que abra los casos de ese dia y ese año ejemplo 2020
ds1 = open("/home/devkbgeptupsi/Documentos/DataScience/Covid-19DS/Covid-19 datasets/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/01-01-2021.csv")

row = csv.reader(ds1)

cursor.executemany("INSERT INTO  case_diaries2020 VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", row)



cursor.execute("SELECT * FROM case_diaries2020")

print(cursor.fetchall())

conexion.commit()
conexion.close()