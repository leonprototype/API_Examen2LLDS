from flask import Flask, render_template, jsonify, abort, request

app = Flask(__name__)


uri = '/api/games'

games = [
    {
        # 'id': 1,
        'titulo': 'Fortnite',
        'desarrollador': 'Epic Games',
        'img_url': 'https://image.api.playstation.com/vulcan/ap/rnd/202303/0621/d3c11818a78c6495e84a3d8e8dd6dc652721be36e0eb8c0a.png'
        # 'fecha_lanzamiento': '10/02/2020',
        # 'plataforma': 'Xbox, PC, PS4, PS5, Nintendo Switch',
        # 'clasificacion': 'E (for Everyone)',
    },
    # {
    #     'id': 2,
    #     'titulo': 'h',
    #     'desarrollador': 'j',
    #     'fecha_lanzamiento': 'a',
    #     'plataforma': 's',
    #     'clasificacion': 'd',
    # },
    # {
    #     'id': 3,
    #     'titulo': 'a',
    #     'desarrollador': 's',
    #     'fecha_lanzamiento': 'f',
    #     'plataforma': 'q',
    #     'clasificacion': 'w',
    # },
    # {
    #     'id': 4,
    #     'titulo': 'e',
    #     'desarrollador': 'r',
    #     'fecha_lanzamiento': 'q',
    #     'plataforma': 't',
    #     'clasificacion': 'f',
    # },
    # {
    #     'id': 5,
    #     'titulo': 'x',
    #     'desarrollador': 'c',
    #     'fecha_lanzamiento': 'z',
    #     'plataforma': 'v',
    #     'clasificacion': 'b',
    # }
]

# API


@app.route("/")
def home_API():
    return render_template('index.html')
    # return jsonify({'games': games, 'message': 'Bienvenido al servidor de la API'})


@app.route(uri, methods=['GET'])
def home_games():
    return jsonify({'games': games})


@app.route(uri+'/<int:game_id>', methods=['GET'])
def get_game(game_id):
    this_game = [game for game in games if game['id'] == game_id]
    if len(this_game) == 0:
        abort(404)
    return jsonify({'game': this_game[0]})


@app.route(uri, methods=['POST'])
def create_game():
    if not request.json:
        abort(404)
    game = {
        'id': len(games) + 1,
        'titulo': request.json['titulo'],
        'desarrollador': request.json['desarrollador'],
        'fecha_lanzamiento': request.json['fecha_lanzamiento'],
        'plataforma': request.json['plataforma'],
        'clasificacion': request.json['clasificacion']
    }

    games.append(game)
    return jsonify({'games': games}), 201


@app.route(uri + '<int:game_id>', methods=['PUT'])
def update_task(game_id):
    this_game = [game for game in games if game['id'] == game_id]
    if len(this_game) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'titulo' in request.json and type(request.json['titulo']) is not str:
        abort(400)
    if 'fecha_lanzamiento' in request.json and type(request.json['fecha_lanzamiento']) is not str:
        abort(400)
    if 'desarrollador' in request.json and type(request.json['desarrollador']) is not str:
        abort(400)
    if 'plataforma' in request.json and type(request.json['plataforma']) is not str:
        abort(400)
    if 'clasificacion' in request.json and type(request.json['clasificacion']) is not str:
        abort(400)
    this_game[0]['titulo'] = request.json.get('titulo', this_game[0]['titulo'])
    this_game[0]['desarrollador'] = request.json.get(
        'desarrollador', this_game[0]['desarrollador'])
    this_game[0]['fecha_lanzamiento'] = request.json.get(
        'fecha_lanzamiento', this_game[0]['fecha_lanzamiento'])
    this_game[0]['plataforma'] = request.json.get(
        'plataforma', this_game[0]['plataforma'])
    this_game[0]['clasificacion'] = request.json.get(
        'clasificacion', this_game[0]['clasificacion'])
    return jsonify({'game': this_game[0]})


@app.route(uri+'/<int:id>', methods=['DELETE'])
def delete_task(id):
    this_game = [task for task in games if task['id'] == id]
    if this_game:
        games.remove(this_game[0])
        return jsonify({'games': games})
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
