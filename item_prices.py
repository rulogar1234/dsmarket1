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
precios.to_sql(name='item_prices2', con=connection, if_exists='replace', index=False)

#cursor = connection.cursor()
cursor.execute("CREATE TABLE item_prices (item TEXT , category TEXT, store_code TEXT, yearweek TEXT, sell_price REAL);")
cursor.execute("INSERT INTO item_prices (item,category,store_code,yearweek,sell_price) SELECT item, category, store_code, SUBSTR(CAST (yearweek AS TEXT),0,7), sell_price FROM item_prices2")

connection.commit()


connection.close()
print('Desconexión')