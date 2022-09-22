# importar modulos de la biblioteca Flask.
from flask import Flask , render_template

# crear objetos de la clase Flask, dando __name__ como argumento.
app = Flask(__name__)

# escribir las rutas usando las funciones "decorator".
# ruta o 'URL' predefinida.
@app.route("/")
def home():

    name = "Zuri" # escribe tu nombre
    age = "14 años" # escribe tu edad

    return render_template('index.html' , name = name , age = age)
    

# define la ruta a la página web de tu padre.
@app.route("/padre")
def father():
    name='Alex'
    age='53'
    return render_template('father.html',nombre=name,edad=age)

# define la ruta a la página web de tu madre.
@app.route("/madre")
def mother():
    name='Xochitl'
    age='47'
    return render_template('mother.html',nombre=name,edad=age)

# define la ruta a la página web de tus amigos.
@app.route("/amigos")
def friends():
    name='Isabela'
    age='15'
    return render_template('friend.html',nombre=name,edad=age)

# agrega otras rutas, si tú quieres.




# ejecuta el archivo
if __name__  ==  '__main__':
    app.run(debug=True)
