from flask import Flask, jsonify, request

app = Flask(__name__)
tarefas = []
@app.route('/')
def home():
    return 'Bem-vindo à API de tarefas!'
@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)
@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    descricao = request.json.get('descricao')
    nova_tarefa = {'id': len(tarefas) + 1, 'descricao': descricao}
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201
# Implemente as rotas para atualizar e excluir tarefas aqui
if __name__ == '__main__':
    app.run(debug=True)