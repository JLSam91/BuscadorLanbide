from flask import Flask, render_template, request
from buscador import Macrofuncion
app = Flask(__name__)

filtros = ['provincia', 'ciudad', 'localgsdvgjhgdidad']

@app.route('/', methods = ['POST', 'GET'])
def hello_world2():
    if request.method == 'POST': 
        argumentos = {}
        argumentos['titulo'] = request.values['nombre']
        #ciudad = request.values['ciudad']
        lista = Macrofuncion(**argumentos)
        return render_template('index.html', lista = lista, criterio = request.values['nombre'], filtros=filtros, filtro_selec=request.values['filtro_selec'])
    else:
        return render_template('index.html', filtros = filtros)

if __name__ == '__main__':

	app.run(debug=True, threaded=True)

