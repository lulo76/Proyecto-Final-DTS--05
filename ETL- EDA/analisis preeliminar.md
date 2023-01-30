El dataset de closed deals posee 14 columnas y 842 filas. 

contiene gran cantidad de nulos en las columnas has_company, has_gtin, average_stock, declared_product_catalog_size 

mql_id = tipo de dato  object, representa el id de marketing qualified leads
seller_id = tipo de dato  object, contiene el id del vendedor 
sdr_id= tipo de dato object, contiene el id COMPLETAR 
sr_id= tipo de dato object,  
won_date=tipo de dato object, fecha de trato/venta, CAMBIAR A DATETIME
business_segment=tipo de dato object, rubro al que se dedica 
lead_type= tipo de dato object, estado de su tienda online?  
lead_behaviour_profile=tipo de object, estatus de tienda online?
has_company= tipo de dato object, estado de compañia
has_gtin=tipo de dato object, ?? 
average_stock=tipo de dato object, promedio de stock  
business_type=tipo de dato object, tipo de negocio 
declared_product_catalog_size=tipo de dato float64, tamaño del catalago declarado
declared_monthly_revenue= tipo de dato float64, declarado mensual(de ventas?)


El dataset de customers posee 5 columnas y 99441 filas. 
este dataset no posee valores nulos 

customer_id= tipo de dato object, representa el id de cliente
customer_unique_id= tipo de dato object, contiene el id unico de cliente
customer_zip_code_prefix= tipo de dato int64, (puede ser el codigo postal?)
customer_city= tipo de dato object, contiene la ciudad del cliente
customer_state= tipo de dato object, contiene el estado del cliente

El dataset geolocation posee 5 columnas y 1000163 filas 
este dataset no presenta valores nulos
geolocation_zip_code_prefix= tipo de dato int64 , podria contener el codigo postal
geolocation_lat = tipo de dato float64, contiene la latitud
geolocation_lng= tipo de dato float64, contiene la longitud
geolocation_city= tipo de dato object, contiene el nombre de la ciudad
geolocation_state= tipo de dato object, contiene las iniciales del estado


El dataset marketing qualified leads posee  4 columnas y 8000 filas 
este dataset presenta pocos valores vacios
mql_id= tipo de dato  object, contiene el id del lider de marketing
first_contact_date= tipo de dato object, contiene la fecha del primer contacto(podria cambiarse a datetime)
landing_page_id= tipo de dato  object, contiene el id de la pagina
origin= tipo de dato object, contiene el origen de la informacion

El dataset order items posee 7 columnas y 112650 filas 
este dataset no contiene valores nulos
order_id= tipo de dato object, contiene el id de la orden
order_item_id= tipo de dato int64, contiene el id del item
product_id= tipo de datoobject, contiene el id del producto
seller_id= tipo de dato object, contiene el id del vendedor
shipping_limit_date = tipo de dato object, contiene la fecha limite de envio
price= tipo de dato float64, contiene el precio
freight_value= tipo de dato float64, contiene el valor del flete

El dataset order payments contiene 5 colummas y 103886 filas
este dataset no posee valores nulos
order_id= tipo de dato object, contiene el id de la orden
payment_sequential= tipo de dato int64, contiene la secuencia de pagos
payment_type= tipo de dato object, posee el tipo de pago
payment_installments= tipo de dato  int64,  contiene la cuota de pago
payment_value= tipo de dato float64, contiene el valor de pago

El dataset order reviews contiene 7 columnas y 99224 filas
este dataset contiene gran cantidad de valores nulos en las columnas review_comment_title y review_comment_message
review_id= tipo de dato object, contiene el id de review
order_id= tipo de dato object, contiene el id de order
review_score= tipo de dato int64, contiene el puntaje de review
review_comment_title= tipo de dato object, contiene el titulo del comentario
review_comment_message= tipo de dato object, contiene el comentario
review_creation_date= tipo de dato object, contiene la fecha de creacion del comentario
review_answer_timestamp= tipo de dato object, contiene el tiempo de respuesta

El dataset orders contiene 8 columnas y 99441 filas
este dataset posee pocos valores nulos
order_id= tipo de dato object, contiene el id de orden
customer_id= tipo de dato object, contiene el id de cliente
order_status= tipo de dato object, contiene el estado de la orden
order_purchase_timestamp= tipo de dato object, contiene el tiempo desde la compra
order_approved_at= tipo de dato object, contiene el tiempo de aprobacion de orden
order_delivered_carrier_date= tipo de dato  object, contiene la fecha de entrega al transportista
order_delivered_customer_date= tipo de dato  object, contiene la fecha en que fue entregada la orden al cliente
order_estimated_delivery_date= tipo de dato  object, contiene la fecha estimada de entrega al cliente

El dataset products contiene 9 columnas y 32951 filas
este dataset contiene pocos valores faltantes
product_id= tipo de dato  object, contiene el id de producto
product_category_name= tipo de dato  object, contiene el nombre de la categoria de producto
product_name_lenght= tipo de dato  float64, contiene la longitud del nombre del producto
product_description_lenght= tipo de dato  float64, contiene la longitud de la descripcion del producto
product_photos_qty= tipo de dato float64, contiene la cantidad de fotos del producto
product_weight_g= tipo de dato float64, contiene el peso del producto
product_length_cm= tipo de dato float64, contiene el largo del producto
product_height_cm= tipo de dato  float64, contiene la altura del producto
product_width_cm= tipo de dato float64, contiene el ancho del producto

El dataset sellers contiene 4 columnas y 3095 filas
este dataset no contiene valores nulos 
seller_id= tipo de dato object, contiene la identificacion del vendedor
seller_zip_code_prefix= tipo de dato int64, contiene el codigo postal del vendedor
seller_city= tipo de dato object, contiene la ciudad del vendedor
seller_state= tipo de dato object, contiene el estado del vendedor

El dataset product category name trasnlation contiene
este dataset no posee valores nulos
product_category_name= tipo de dato object, contiene el nombre de la categoria del producto
product_category_name_english= tipo de dato object, contiene el nombre de la categoria del producto en ingles