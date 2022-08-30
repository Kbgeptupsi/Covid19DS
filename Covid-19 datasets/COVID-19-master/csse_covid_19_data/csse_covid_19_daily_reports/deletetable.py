from curses import curs_set
import sqlite3
conexion = sqlite3.connect("/home/devkbgeptupsi/Documentos/DataScience/Covid-19DS/Covid-19 datasets/2021Case_Diarie-19.db")
cursor=conexion.cursor()
cursor.executemany("DROP TABLE Case_Diarie-19 where case_diaries2020")