#conexión base de datos SQL Lite
import sqlite3

try:
  connection = sqlite3.connect("C:/Users/rsalcedo/OneDrive/Documentos/projects_ds/dsmarket/dsmarket1/data/dsmarket.db")
  print('Conexión establecida')
except:
  print('Error al intentar la conexión')
try:
    cursor = connection.cursor()
    cursor.execute("DROP TABLE item_prices;")
except:
   print("la tabla no existe")

import pandas as pd
#importación ficheros
precios = pd.read_csv("C:/Users/rsalcedo/OneDrive/Documentos/projects_ds/dsmarket/dsmarket1/data/item_prices.csv")

#creación de df
precios.to_sql(name='item_prices', con=connection, if_exists='replace', index=False)

#cursor = connection.cursor()
#cursor.execute("ALTER TABLE daily_calendar ADD COLUMN yearweek TEXT;")
#cursor.execute("UPDATE daily_calendar SET yearweek=strftime('%Y%m', date)")
#cursor.execute("ALTER TABLE daily_calendar ADD COLUMN fecha DATE;")
#cursor.execute("UPDATE daily_calendar SET fecha = DATE(date);")
#cursor.execute("ALTER TABLE daily_calendar DROP COLUMN date;")
#connection.commit()

connection.close()
print('Desconexión')