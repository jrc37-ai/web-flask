from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/otros")
def otros():
    return render_template('otros.html')

@app.route("/outliers")
def outliers():
    return render_template('outliers.html')

@app.route("/boton", methods=['POST'])
def boton():
    cuartos = int(request.form['cuartos'])
    distancia = int(request.form['distancia'])
    output = cuartos * distancia
    return render_template('index.html', pred_text=f'{cuartos} cuartos por {distancia} distancia es igual a {output}')

if __name__=="__main__":
    app.run(debug=True) 
