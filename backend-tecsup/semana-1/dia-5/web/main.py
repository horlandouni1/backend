from flask import Flask,render_template
from flask_mysqldb import MySQL


app = Flask(__name__)

#CONFIGURAR CONEXIÓN CON BASE DE DATOS
app.config['MYSQL_HOST'] = 'bf99jkhcooetq54sjwta-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'ubxzpeezw9z8fcdw'
app.config['MYSQL_PASSWORD'] = 'IbPCKpHJpxHs7gaFl8zF'
app.config['MYSQL_DB'] = 'bf99jkhcooetq54sjwta'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute('select id,sistema,procesador,memoria from computadoras')
    data = cursor.fetchall()
    cursor.close()
    
    print(data)
    
    context = {
        'data':data
    }
    
    return render_template('index.html',**context)

app.run(debug=True,port=4000)