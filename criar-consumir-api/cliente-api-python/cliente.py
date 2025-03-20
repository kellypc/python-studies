import requests

BASE_URL = 'http://127.0.0.1:5000/'

def obter_tarefas():
    response = requests.get(f'{BASE_URL}/tarefas')
    return response.json()

def criar_tarefa(descricao):
    response = requests.post(f'{BASE_URL}/tarefas', json={'descricao': descricao})
    return response.json()

def executar_exemplos():
    # Listar tarefas
    print('Listando tarefas:')
    print(obter_tarefas())
    # Criar uma nova tarefa
    print('Criando uma nova tarefa:')
    print(criar_tarefa('Estudar Python'))
    # Listar tarefas novamente
    print('Listando tarefas:')
    print(obter_tarefas())
if __name__ == '__main__':
    executar_exemplos()