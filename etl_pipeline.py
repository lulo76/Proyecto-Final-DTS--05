# Variables para la conexión
############################
HOST = 'localhost'
PORT = 3306
USER = 'root'
PASSWORD = '1234567890'
DATABASE = 'olist'
############################

import pandas as pd 
import mysql.connector
from sqlalchemy import create_engine


def create_db():
    con = mysql.connector.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD
    )
    cur = con.cursor()
    cur.execute("DROP DATABASE IF EXISTS "+DATABASE)
    cur.execute("CREATE DATABASE "+DATABASE)
    con.close()

def extract():
    df_customers= pd.read_csv('https://raw.githubusercontent.com/lulo76/Proyecto-Final-DTS--05/main/Week%201/Datasets/olist_customers_dataset.csv')
    df_geolocation= pd.read_csv('https://raw.githubusercontent.com/lulo76/Proyecto-Final-DTS--05/main/Week%201/Datasets/olist_geolocation_dataset.csv')
    df_order_items= pd.read_csv('https://raw.githubusercontent.com/lulo76/Proyecto-Final-DTS--05/main/Week%201/Datasets/olist_order_items_dataset.csv')
    df_reviews = pd.read_csv('https://raw.githubusercontent.com/lulo76/Proyecto-Final-DTS--05/main/Week%201/Datasets/olist_order_reviews_dataset.csv')
    df_orders = pd.read_csv('https://raw.githubusercontent.com/lulo76/Proyecto-Final-DTS--05/main/Week%201/Datasets/olist_orders_dataset.csv')
    df_sellers=pd.read_csv('https://raw.githubusercontent.com/lulo76/Proyecto-Final-DTS--05/main/Week%201/Datasets/olist_sellers_dataset.csv')
  
    data = {
        'df_customers': df_customers, 
        'df_geolocation': df_geolocation, 
        'df_order_items': df_order_items,
        'df_reviews': df_reviews,
        'df_orders': df_orders,
        'df_sellers': df_sellers
    }

    return data


def transform(data):
                 
    """ 
    Esta función realiza todas las tareas de ETL necesarias para un grupo de datos.
    Parametro: data (diccionario)

    Retorna: un diccionario con todas las transformaciones realizadas
    """         
    
    df_customers= data['df_customers']
    df_geolocation=data['df_geolocation']
    df_order_items= data['df_order_items']
    df_reviews= data['df_reviews']
    df_orders= data['df_orders']
    df_sellers= data['df_sellers']

    #Transformaciones para cada DF
    
    #Customers
    # Renombramos la columna de codigo postal.
    df_customers.rename(columns = {'customer_zip_code_prefix':'cus_zip_code'}, inplace=True)
    #modifico el nombre de las ciudades con la primer letra mayuscula
    #df_customers = df_customers['customer_city'].str.capitalize()
    df_customers['customer_city'] = df_customers['customer_city'].str.capitalize()

    #Geolocation
    #Dropear duplicados de zip code
    df_geolocation.drop_duplicates(['geolocation_zip_code_prefix'], inplace=True)
    # Renombramos las columnas.
    df_geolocation.rename(columns = {'geolocation_zip_code_prefix':'geo_zip_code'}, inplace=True)
    df_geolocation.rename(columns = {'geolocation_lat':'geo_lat'}, inplace=True)
    df_geolocation.rename(columns = {'geolocation_lng':'geo_lng'}, inplace=True)
    df_geolocation.rename(columns = {'geolocation_city':'geo_city'}, inplace=True)
    df_geolocation.rename(columns = {'geolocation_state':'geo_state'}, inplace=True)
    
    #Order Items
    #quitar espacio izquierdo
    df_order_items['shipping_limit_date']= df_order_items['shipping_limit_date'].str.lstrip()
    #quitar espacio derecho
    df_order_items['shipping_limit_date']= df_order_items['shipping_limit_date'].str.rstrip()
    #reemplazar el espacio vacio por coma
    df_order_items['shipping_limit_date']=df_order_items['shipping_limit_date'].str.replace(' ', ',')
    #separar la listta en columna por , 
    df_order_items['shipping_limit_date']= df_order_items['shipping_limit_date'].str.split(',')
    #asignar nuevos valores6
    df_order_items[['fecha_limite', 'hora_limite']] = pd.DataFrame(df_order_items.shipping_limit_date.values.tolist(), 
                                                            columns=['fecha_limite', 'hora_limite'])
    #dropear shipping date
    df_order_items.drop(['shipping_limit_date'], axis=1, inplace=True)
    #cambiar formato a datetime
    df_order_items['fecha_limite']= pd.to_datetime(df_order_items['fecha_limite'])
    #cambiar formato a datetime
    df_order_items['hora_limite']= pd.to_datetime(df_order_items['hora_limite'])

    #Reviews
    # Eliminar id's duplicados
    df_reviews.drop_duplicates(['review_id'], inplace=True)
    # Eliminar columna de titulos de comentarios
    df_reviews.drop(['review_comment_title'], axis=1, inplace=True)
    # Borrar espacio vacio izquierdo y derecho.
    df_reviews['review_comment_message'] = df_reviews['review_comment_message'].str.lstrip() 
    df_reviews['review_comment_message'] = df_reviews['review_comment_message'].str.rstrip()
    # Rellenarmos NaN con "sin datos"
    df_reviews['review_comment_message'].fillna('Sin Dato', inplace = True)
       

    #Orders
    # Crear las columnas con diferencia de dias
    df_orders ['dif_buy_cust'] = (pd.to_datetime(df_orders['order_delivered_customer_date']) - pd.to_datetime(df_orders['order_purchase_timestamp'])).dt.days
    df_orders ['dif_buy_est'] = (pd.to_datetime(df_orders['order_estimated_delivery_date']) - pd.to_datetime(df_orders['order_purchase_timestamp'])).dt.days
    df_orders ['dif_cust_est'] = (pd.to_datetime(df_orders['order_estimated_delivery_date']) - pd.to_datetime(df_orders['order_delivered_customer_date'])).dt.days
    # Llenar los NaN vacios
    df_orders['order_approved_at'].fillna('Sin Dato', inplace = True)
    df_orders['order_delivered_carrier_date'].fillna('Sin Dato', inplace = True)
    df_orders['order_delivered_customer_date'].fillna('Sin Dato', inplace = True)
    df_orders['dif_buy_cust'].fillna('Sin Dato', inplace = True)
    df_orders['dif_cust_est'].fillna('Sin Dato', inplace = True)
    # Eliminamos la columna order_status
    df_orders.drop(['order_status'], axis = 1, inplace=True)
    

    #Sellers
    # Renombramos las columnas.
    df_sellers.rename(columns = {'seller_zip_code_prefix':'sel_zip_code'}, inplace=True)

    data = {
        'df_customers': df_customers, 
        'df_geolocation': df_geolocation, 
        'df_order_items': df_order_items,
        'df_reviews': df_reviews,
        'df_orders': df_orders,
        'df_sellers': df_sellers
    }

    return data
    

def load(data):
    con = create_engine('mysql+pymysql://'+USER+':'+PASSWORD+'@'+HOST+':'+str(PORT)+'/'+DATABASE)

    for table in data:
        df = data[table]
        df.to_sql(table[3:], con=con, index=False)


def normalize_data():
    con = mysql.connector.connect(
        host=HOST,
        user=USER,
        passwd=PASSWORD,
        db=DATABASE
    )
    cur = con.cursor()
    cur.execute("ALTER TABLE customers MODIFY customer_id VARCHAR(50);")
    cur.execute("ALTER TABLE customers MODIFY cus_zip_code INT;")
    cur.execute("ALTER TABLE geolocation MODIFY geo_zip_code INT;")
    cur.execute("ALTER TABLE order_items MODIFY order_id VARCHAR (50);")
    cur.execute("ALTER TABLE order_items MODIFY product_id VARCHAR (50);")
    cur.execute("ALTER TABLE order_items MODIFY seller_id VARCHAR (50);")
    cur.execute("ALTER TABLE order_items MODIFY order_item_id INT;")
    cur.execute("ALTER TABLE orders MODIFY order_id VARCHAR(50);")
    cur.execute("ALTER TABLE orders MODIFY customer_id VARCHAR(50);")
    cur.execute("ALTER TABLE reviews MODIFY review_id VARCHAR(50);")
    cur.execute("ALTER TABLE reviews MODIFY order_id VARCHAR(50);")
    cur.execute("ALTER TABLE sellers MODIFY seller_id VARCHAR(50);")
    cur.execute("ALTER TABLE sellers MODIFY sel_zip_code INT;")
    con.close()
    return "tablas modificadas"


def set_primary_key():
    con = mysql.connector.connect(
        host=HOST,
        user=USER,
        passwd=PASSWORD, 
        db=DATABASE
    )
    cur = con.cursor()
    cur.execute("ALTER TABLE customers ADD PRIMARY KEY (customer_id);")
    cur.execute("ALTER TABLE customers ADD INDEX (cus_zip_code);")
    cur.execute("ALTER TABLE geolocation ADD PRIMARY KEY (geo_zip_code);")
    cur.execute("ALTER TABLE geolocation ADD INDEX (geo_zip_code);")
    cur.execute("ALTER TABLE order_items ADD COLUMN id_item INT AUTO_INCREMENT PRIMARY KEY;")
    cur.execute("ALTER TABLE order_items ADD INDEX (order_id);")
    cur.execute("ALTER TABLE order_items ADD INDEX (seller_id);")
    cur.execute("ALTER TABLE orders ADD PRIMARY KEY (order_id);")
    cur.execute("ALTER TABLE orders ADD INDEX (customer_id);")
    cur.execute("ALTER TABLE reviews ADD PRIMARY KEY (review_id);")
    cur.execute("ALTER TABLE reviews ADD INDEX (order_id);")
    cur.execute("ALTER TABLE sellers ADD PRIMARY KEY (seller_id);")
    cur.execute("ALTER TABLE sellers ADD INDEX (sel_zip_code);")
    con.close()
    return "Claves primarias creadas"


def set_foreign_key():
    con = mysql.connector.connect(
        host=HOST,
        user=USER,
        passwd=PASSWORD,
        db=DATABASE
    )
    cur = con.cursor() 
    cur.execute("SET foreign_key_checks=0;")
    cur.execute("ALTER TABLE customers ADD FOREIGN KEY (cus_zip_code) REFERENCES geolocation(geo_zip_code);")
    cur.execute("ALTER TABLE order_items ADD FOREIGN KEY (order_id) REFERENCES orders(order_id);")
    cur.execute("ALTER TABLE order_items ADD FOREIGN KEY (seller_id) REFERENCES sellers(seller_id);")
    cur.execute("ALTER TABLE orders ADD FOREIGN KEY (customer_id) REFERENCES customers(customer_id);")
    cur.execute("ALTER TABLE reviews ADD FOREIGN KEY (order_id) REFERENCES orders(order_id);")
    cur.execute("ALTER TABLE sellers ADD FOREIGN KEY (sel_zip_code) REFERENCES geolocation(geo_zip_code);")
    con.close()
    return "Claves primarias creadas"


# Crear pipeline
###################################################
print('creating database...')
create_db()
print('extracting data...')
data = extract()
print('transforming data...')
data = transform(data)
print('loading data...')
load(data)
print('normalizing data...')
normalize_data()
print('set primary keys...')
set_primary_key()
print('set foreign key')
set_foreign_key()
print('\nTASK COMPLETED SUCCESSFULLY!')
###################################################