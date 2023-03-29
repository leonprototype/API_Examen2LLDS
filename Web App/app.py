from flask import render_template, Flask
import requests

app = Flask(__name__)

# Se asigna a la variable url el link en donde se encuentra el servidor en donde esta nuestro codigo backend
url = 'https://api-examen2llds.onrender.com/api/games'


@app.route('/')
def home():
    # Se extraen los objetos del url a traves del metodo request y se usa un try en caso de no recibir nada del servidor
    try:
        response = requests.get(url).json()['games']
        print(response)
    except Exception:
        print('Error...')
        response = []
    # Se llama al codigo front end
    return render_template('index.html', games=response)


if __name__ == '__main__':
    app.run(debug=True)
