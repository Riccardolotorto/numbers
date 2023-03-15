from flask import Flask, render_template
app = Flask(__name__)

import random 


@app.route('/', methods=['GET'])
def home():
    return render_template('quattro.html')

@app.route('/paginarisultato/<scelta>', methods=['GET'])
def paginarisultato(scelta):
    numero = random.randint(1, 9)
    if numero == int(scelta):
        testo = "HAI VINTO!"
    else:
        testo = "HAI PERSO!"
    return render_template('risultato.html', esito = testo)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)