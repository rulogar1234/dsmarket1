#conexion base de datos SQL Server
#import pyodbc
#from sqlalchemy import create_engine
#server = 'PREVF-SQL03\\MINERVA'
#database = 'DSMarket'
#username = 'raul'
#password = '4321'
#conn_str = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=SQL+Server'
#try:
#  engine = create_engine(conn_str, use_setinputsizes=False)
#  connection = engine.connect()
#  print('Conexión establecida')
#except:
#  print('Error al intentar la conexión')


#conexión base de datos SQL Lite
import sqlite3

try:
  connection = sqlite3.connect("C:/Users/rsalcedo/OneDrive/Documentos/projects_ds/dsmarket/data/dsmarket.db")
  print('Conexión establecida')
except:
  print('Error al intentar la conexión')
try:
    cursor = connection.cursor()
    cursor.execute("DROP TABLE daily_calendar;")
except:
   print("Tabla no existe")

import pandas as pd
#importación ficheros
calendario = pd.read_csv("C:/Users/rsalcedo/OneDrive/Documentos/projects_ds/dsmarket/data/daily_calendar_with_events.csv")

#creación de df
calendario.to_sql(name='daily_calendar', con=connection, if_exists='replace', index=False)

cursor = connection.cursor()
cursor.execute("ALTER TABLE daily_calendar ADD COLUMN yearweek TEXT;")
cursor.execute("UPDATE daily_calendar SET yearweek=strftime('%Y%m', date)")
cursor.execute("ALTER TABLE daily_calendar ADD COLUMN fecha DATE;")
cursor.execute("UPDATE daily_calendar SET fecha = DATE(date);")
cursor.execute("ALTER TABLE daily_calendar DROP COLUMN date;")
connection.commit()

connection.close()
print('Desconexión')