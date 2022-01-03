from flask import Flask,render_template
from flask_mysqldb import MySQL


app = Flask(__name__)

#CONFIGURAR CONEXIÓN CON BASE DE DATOS
app.config['MYSQL_HOST'] = 'b8jbbodxdpfnz8shn5hf-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'uxokmefkdrcvisu2'
app.config['MYSQL_PASSWORD'] = 't4FSTmb1DcZEv71EvsId'
app.config['MYSQL_DB'] = 'b8jbbodxdpfnz8shn5hf'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute('select id,Nombre,Cargo,fecha_hora from asistencias')
    data = cursor.fetchall()
    cursor.close()
    
    print(data)
    
    context = {
        'data':data
    }
    
    return render_template('index.html',**context)

app.run(debug=True,port=4000)