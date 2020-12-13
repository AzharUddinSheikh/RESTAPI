from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userdetails = request.form
        name = userdetails['name']
        email = userdetails['email']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO USERS(name, email) values(%s,%s)",
                    (name, email))
        mysql.connection.commit()
        cur.close()
        return {'status': 'successful'}
    return render_template('index.html')
# render templates allow our .html file to run in this server


if __name__ == "__main__":
    app.run(debug=True)

# debug = True for every changes our code run automatically
# if __name__ == "__main__" method ll allow our code to run in this file only
 # app = Flask(__name__) __name__ is the name of the current python module (app need to know where it located )
 # or we can say it we  are initializing Flask class and set it into app variable

# mysql = MySQL(app) here we initialize MySQL class and set it into mysql variable
#
# fetching form data

# request.form by this method and setting it into variable

# lets connect our application into database so import mysql module

# we have to set some parameter to connect specific database

'''
app.config['MYSQL_HOST'] = 'localhost' default
app.config['MYSQL_USER'] = 'root' user name
app.config['MYSQL_PASSWORD'] = 'admin' password when created in mysql
app.config['MYSQL_DB'] = 'flaskapp' its a database name 

and many more configuration 
'''

# mysql.connection.cursor() = not only it ll connect our data but also can pull data form db/ or we able to execute our query
# .execute('query').fetchall() = what ever query given it ll execute and by fetcha command it pull out that data

# .commit() for saving the changes
# .close it ll close our db
