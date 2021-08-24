import pyodbc 

def conexion(driver,server,db)
	conn = pyodbc.connect('Driver=+str(driver)+;'
	                      'Server=+str(server)+;'
	                      'Database=+str(db)+;'
	                      'Trusted_Connection=yes;')
	return conn
def query(conexion,query)

	cursor = conexion.cursor()
	cursor.execute(query)
	return cursor

def get_string(cursor)
	text_sql=""
	for row in cursor:
	    #print(row)
	    print(row[3])
	    text_sql=text_sql+str(row[3])+"\n"


	return text sql