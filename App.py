from flask import Flask, render_template, jsonify, abort, request

app = Flask(__name__)


uri = '/api/games'

# Lista de objetos que seran los que serviran para mandar como API
games = [
    {
        'id': 1,
        'titulo': 'Fortnite',
        'descripcion': """Fortnite es un videojuego del año 2017 desarrollado 
        por la empresa Epic Games lanzado como diferentes paquetes de software que presentan diferentes 
        modos de juego, pero que comparten 
        el mismo motor de juego y mecánicas. Fue anunciado en los premios 
        Spike Video Game Awards en 2011.""",
        'img_url': 'https://image.api.playstation.com/vulcan/ap/rnd/202303/0621/d3c11818a78c6495e84a3d8e8dd6dc652721be36e0eb8c0a.png',
        'fecha_lanzamiento': '25 de junio de 2017',
        'plataforma': """Microsoft Windows,
        macOS,
        PlayStation, 
        Xbox One,
        Nintendo Switch,
        PlayStation, 
        Xbox Series X | S,
        Android, 
        iOS""",
        'clasificacion': 'PEGI: +12',
    },
    {
        'id': 2,
        'titulo': 'Halo',
        'descripcion': """Halo es una franquicia de videojuegos de ciencia ficción creada y 
        desarrollada por Bungie Studios hasta Halo Reach, y gestionada ahora por 343 Industries, propiedad de Xbox Game Studios. La serie se centra en una guerra interestelar 
        entre la humanidad y una alianza teocrática de alienígenas conocidos como Covenant.""",
        'img_url': 'https://i.blogs.es/4c03cc/halo-4/1366_2000.jpeg',
        'fecha_lanzamiento':  '25 de septiembre de 2007',
        'plataforma': 'Xbox, Windows, Xbox360',
        'clasificacion': 'PEGI: +16',
    },
    {
        'id': 3,
        'titulo': 'Spider-man Web of Shadows',
        'descripcion': """Una invasión de mortíferos simbiontes amenaza con la total devastación de las
        calles de Nueva York. En nuestras manos estará detener esta amenaza poniéndonos el
        traje y usando los poderes arácnidos de Spiderman.""",
        'img_url': 'data:image/jpeg;base64,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',
        'fecha_lanzamiento': '21 de octubre 2008',
        'plataforma': 'Xbox 360, PlayStation 3, Microsoft Windows y Wii',
        'clasificacion': 'PEGI: +12',
    },
    {
        'id': 4,
        'titulo': 'Conkers Bad Fur Day',
        'descripcion': """ Conker se encuentra borracho tratando de regresar a su casa, tomando un camino cualquiera. Al día siguiente despierta desconcertado al lado de una granja, 
        con una terrible resaca, y mientras busca el camino de vuelta a su hogar, 
        este deberá evitar a los siervos del Rey Pantera (o Panther King).""",
        'img_url': 'https://images.uncyclomedia.co/inciclopedia/es/thumb/d/d8/Conker_personajes.jpg/300px-Conker_personajes.jpg',
        'fecha_lanzamiento': '4 de marzo de 2001 ',
        'plataforma': 'Nintendo 64',
        'clasificacion': 'PEGI: +18',
    },
    {
        'id': 5,
        'titulo': 'The Chronicles of Riddick: Escape from Butcher Bay',
        'descripcion': 'The Chronicles of Riddick: Escape from Butcher Bay es un videojuego de disparos en primera persona y sigilo desarrollado por Starbreeze Studios y publicado por Vivendi Games.',
        'img_url': 'https://upload.wikimedia.org/wikipedia/en/3/38/RiddickButcherBay.jpg',
        'fecha_lanzamiento': '1 de junio de 2004',
        'plataforma': 'Xbox, Microsoft Windows',
        'clasificacion': 'PEGI: 18',
    }
]

# API

# muestra un mensaje de bienvenida.


@app.route("/")
def home_API():
    return jsonify({'message': 'Bienvenido al servidor de la API'})

# devuelve una lista de todos los juegos.


@app.route(uri, methods=['GET'])
def get_games():
    return jsonify({'games': games})

# Busca un juego en especifico a traves de su ID y regresa el mismmo con el metodo GET


@app.route(uri+'/<int:game_id>', methods=['GET'])
def get_game(game_id):
    this_game = [game for game in games if game['id'] == game_id]
    if len(this_game) == 0:
        abort(404)
    return jsonify({'game': this_game[0]})

# A traves del metodo POST se crea un nuevo objeto y se agrega al final de la lista con append


@app.route(uri + '/post', methods=['POST'])
def create_game():
    if not request.json:
        abort(404)
    else:
        game = {
            # Se incrementa en 1 el numero de id para llevar un orden en los id y mantener consistencia
            'id': len(games) + 1,
            'titulo': request.json.get('titulo'),
            'descripcion': request.json.get('descripcion'),
            'img_url': request.json.get('img_url'),
            'fecha_lanzamiento': request.json.get('fecha_lanzamiento'),
            'plataforma': request.json.get('plataforma'),
            'clasificacion': request.json.get('clasificacion')
        }
    print(game)
    games.append(game)
    return jsonify({'games': games}), 201

# Con el metodo PUT se modifica un objeto de la lista y verifica si los datos ingresados corresponden con el tipo de dato que se requiere


@app.route(uri + '<int:game_id>', methods=['PUT'])
def update_task(game_id):
    this_game = [game for game in games if game['id'] == game_id]
    # Verificacion de que EXISTA el objeto en la lista
    if len(this_game) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'titulo' in request.json and type(request.json['titulo']) is not str:
        abort(400)
    if 'fecha_lanzamiento' in request.json and type(request.json['fecha_lanzamiento']) is not str:
        abort(400)
    if 'descripcion' in request.json and type(request.json['descripcion']) is not str:
        abort(400)
    if 'plataforma' in request.json and type(request.json['plataforma']) is not str:
        abort(400)
    if 'img_url' in request.json and type(request.json['img_url']) is not str:
        abort(400)
    if 'clasificacion' in request.json and type(request.json['clasificacion']) is not str:
        abort(400)
    # Agrega los nuevos datos a la tabla y se muestra el objto modificado
    this_game[0]['titulo'] = request.json.get('titulo', this_game[0]['titulo'])
    this_game[0]['descripcion'] = request.json.get(
        'descripcion', this_game[0]['descripcion'])
    this_game[0]['img_url'] = request.json.get(
        'img_url', this_game[0]['img_url'])
    this_game[0]['fecha_lanzamiento'] = request.json.get(
        'fecha_lanzamiento', this_game[0]['fecha_lanzamiento'])
    this_game[0]['plataforma'] = request.json.get(
        'plataforma', this_game[0]['plataforma'])
    this_game[0]['clasificacion'] = request.json.get(
        'clasificacion', this_game[0]['clasificacion'])
    return jsonify({'game': this_game[0]})

# Elimina un objeto de la lista a traves del metodo DELETE utilizando .remove


@app.route(uri+'/<int:id>', methods=['DELETE'])
def delete_task(id):
    this_game = [task for task in games if task['id'] == id]
    if this_game:
        games.remove(this_game[0])
        return jsonify({'games': games})
    # Si no existe se cierra el programa a traves de abort
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
