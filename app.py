from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/carta')
def carta():
    return render_template('carta.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')

# La ruta '/delivery' ahora carga la página del formulario de datos
@app.route('/delivery')
def delivery():
    return render_template('delivery.html')

@app.route('/reserva')
def reserva():
    return render_template('reserva.html')

@app.route('/agradecimiento')
def agradecimiento():
    return render_template('agradecimiento.html')

if __name__ == '__main__':
    app.run(debug=True)