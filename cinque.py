from flask import Flask, render_template
app = Flask(__name__)

import random 
prova = 0

@app.route('/', methods=['GET'])
def home():
    return render_template('cinque.html')

@app.route('/paginarisultato/<scelta>', methods=['GET'])
def paginarisultato(scelta):
    global prova
    numero = random.randint(1, 9)
    if numero == int(scelta):
        testo = "HAI VINTO!"
        prova += 1
    else:
        testo = "HAI PERSO!"
        prova += 1
    return render_template('risultato.html', esito = testo, tentativi = prova)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)