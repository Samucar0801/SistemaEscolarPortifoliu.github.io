# Importando Flask para criar uma aplicação web
# O Flask é um microframework em Python que permite criar aplicações web de forma fácil.
from flask import Flask, render_template, request, redirect, url_for

# Inicializando a aplicação Flask
# Aqui estamos criando uma instância da classe Flask que vai nos permitir criar rotas e gerenciar a aplicação.
app = Flask(__name__)

print('Hello World')

# Classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

# Classe Funcionario herdando de Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade)  # Chamando o construtor da classe base (Pessoa)
        self.cargo = cargo  # Armazenando o cargo do funcionário
        self.salario = salario  # Armazenando o salário do funcionário

# Classe Aluno herdando de Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, idade, numero_matricula):
        super().__init__(nome, idade)  # Chamando o construtor da classe base (Pessoa)
        self.numero_matricula = numero_matricula  # Armazenando o número de matrícula do aluno

# Classe Escola para gerenciar os Funcionários e Alunos
class Escola:
    def __init__(self, nome, endereco, diretor):
        self.nome = nome  # Armazenando o nome da escola
        self.endereco = endereco  # Armazenando o endereço da escola
        self.diretor = diretor  # Armazenando o nome do diretor da escola
        self.funcionarios = []  # Lista de funcionários, inicialmente vazia
        self.alunos = []  # Lista de alunos, inicialmente vazia

    # Método para adicionar um funcionário à lista de funcionários
    def contratar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)  # Adiciona um funcionário à lista de funcionários
        
    # Método para adicionar um aluno à lista de alunos
    def admitir_aluno(self, aluno):
        self.alunos.append(aluno)  # Adiciona um aluno à lista de alunos

# Criando uma instância da Escola
escola = Escola("Escola XYZ", "Rua das Flores", "Diretor Fulano")  # Criando a escola com um nome, endereço e diretor

# Rota principal que renderiza o template HTML
@app.route('/')  # Define a rota principal (raiz) da aplicação
def index():
    # Renderiza o template HTML 'index.html', passando as listas de funcionários e alunos
    return render_template('index.html', funcionarios=escola.funcionarios, alunos=escola.alunos)

# Rota para adicionar um funcionário via formulário
@app.route('/adicionar_funcionario', methods=['POST'])  # Define a rota para adicionar funcionário, aceitando apenas POST
def adicionar_funcionario():
    # Pegando os dados do formulário
    nome = request.form['nomeFuncionario']  # Captura o nome do funcionário do formulário
    idade = request.form['idadeFuncionario']  # Captura a idade do funcionário do formulário
    cargo = request.form['cargoFuncionario']  # Captura o cargo do funcionário do formulário
    salario = request.form['salarioFuncionario']  # Captura o salário do funcionário do formulário
    
    # Criando uma instância de Funcionario
    funcionario = Funcionario(nome, idade, cargo, salario)  # Cria um novo objeto Funcionario com os dados capturados
    escola.contratar_funcionario(funcionario)  # Adiciona o funcionário à escola
    
    return redirect(url_for('index'))  # Redireciona o usuário para a página inicial após adicionar o funcionário

# Rota para adicionar um aluno via formulário
@app.route('/adicionar_aluno', methods=['POST'])  # Define a rota para adicionar aluno, aceitando apenas POST
def adicionar_aluno():
    # Pegando os dados do formulário
    nome = request.form['nomeAluno']  # Captura o nome do aluno do formulário
    idade = request.form['idadeAluno']  # Captura a idade do aluno do formulário
    matricula = request.form['matriculaAluno']  # Captura o número de matrícula do aluno do formulário
    
    # Criando uma instância de Aluno
    aluno = Aluno(nome, idade, matricula)  # Cria um novo objeto Aluno com os dados capturados
    escola.admitir_aluno(aluno)  # Adiciona o aluno à escola
    
    return redirect(url_for('index'))  # Redireciona o usuário para a página inicial após adicionar o aluno

# Iniciando o servidor da aplicação
if __name__ == '__main__':
    app.run(debug=True)  # Inicia o servidor Flask em modo de depuração
