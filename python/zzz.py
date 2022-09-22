import mysql.connector as mysql

db = mysql.connect(
    host = "Localhost",
    user = "root",
    passwd = "",
    Database = "DBPython"
)

conexion = db.cursor()

consulta = "INSERT INFO usuarios (USU_USER, USU_CLAV) VALUES (%s,%s)"
# valores a ser insertadis en la tabla de usuarios 
valores = (
    ("Peter", "peter"),
    ("Any", "any"),
    ("Julio","dj"),
    ("Cristel","cris")
)
# ejecutando un comando insert
conexion.execute(consulta, valores)

# confirmando la transaccion realizada
db.commit()




print(conexion.rowcount, "registros insertados.......")
