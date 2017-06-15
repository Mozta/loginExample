#This script charge excel in tables and put into db
import petl as etl
import psycopg2
from time import time

def llevar_bd_to_excel():
    table = etl.io.xls.fromxls('lista.xls')
    connection = psycopg2.connect('dbname=usuarios user=postgres password=admin')
    etl.todb(table, connection, 'login_lista')

start_time = time()
llevar_bd_to_excel()
elapsed_time = time() - start_time
print("Datos cargados exitosamente!")
print("Elapsed time: %.10f seconds" % elapsed_time)
