from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': "Pelé - o rei",
        'autor': "Santos FC"
    },
    {
        'id': 2,
        'titulo': "Sócrates - o doutor",
        'autor': "SCCP"
    },
    {
        'id': 3,
        'titulo': "Livro Exemplo",
        'autor': "Brasil"
    },
]

# CONSULTAR TODOS OS LIVROS
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# CONSULTAR LIVRO POR ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    return jsonify({'erro': 'Livro não encontrado'}), 404

# EDITAR LIVRO POR ID
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    return jsonify({'erro': 'Livro não encontrado'}), 404

# EXCLUIR LIVRO POR ID
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

        return jsonify(livros)
#CRIAR
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# EXECUTAR A API
if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
