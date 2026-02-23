class Pessoa:
    """
    CLASSE MÃE: Define o molde para qualquer pessoa no sistema.
    """
    def __init__(self, nome, idade, altura):
        # MÉTODO CONSTRUTOR: Primeira ação do Python ao criar o objeto.
        # Ele dá 'materialidade' à classe, atribuindo os parâmetros aos atributos.
        
        # ENCAPSULAMENTO: O prefixo '__' torna os atributos privados.
        # Isso protege os dados contra alterações indevidas fora da classe.
        self.__nome = nome
        self.__idade = idade
        self.altura = altura 

    def apresentar(self):
        # MÉTODO: Uma ação que utiliza os atributos da própria classe (self).
        print(f"Olá, meu nome é {self.__nome}, tenho {self.__idade} anos e minha altura é {self.altura} metros.")

    def get_nome(self):
        # MÉTODO GET (PEGAR): Permite acessar um atributo privado de forma segura.
        # Como o nome está encapsulado, criamos este método para poder lê-lo fora da classe.
        return self.__nome

    def set_idade(self, novaIdade):
        # MÉTODO SET (DEFINIR): Permite alterar um atributo privado sob certas condições.
        # Aqui usamos um 'if' como filtro de segurança para validar a nova idade.
        if int(novaIdade) < 120:
            self.__idade = novaIdade

# --- INSTANCIAÇÃO DE OBJETOS ---

# Criando objetos reais (p1 e p2) a partir do molde (Classe Pessoa)
p1 = Pessoa("Sérgio", "42" , "1.83")
p2 = Pessoa("Ana", "41", "1.72")

# Execução das ações (Métodos)
p1.apresentar()
p2.apresentar()

# Testando o Set: Alterando a idade com segurança através do método
p1.set_idade(35)
p1.apresentar()

# Testando o Get: Acessando o nome protegido isoladamente
print(f"Nome extraído com Get: {p1.get_nome()}")


# --- CONCEITO DE HERANÇA ---

# HERANÇA: Criamos a classe Aluno que 'herda' tudo da classe Pessoa (mãe).
# Isso evita a repetição de código, aproveitando atributos e métodos já existentes.
class Aluno(Pessoa):
    def __init__(self, nome, idade, altura, matricula):
        # super(): Comando para acessar a classe mãe e instanciar os dados que queremos herdar.
        super().__init__(nome, idade, altura)
        self.matricula = matricula # Atributo exclusivo da classe Aluno

    def estudante(self):
        # Método exclusivo da classe Aluno para imprimir a matrícula.
        print("A matricula do aluno e: ", self.matricula)

    # --- CONCEITO DE POLIMORFISMO ---
    
    # POLIMORFISMO (Muitas Formas): Sobrescrita do método apresentar.
    # Recriamos o método com o MESMO NOME da classe mãe, mas com um comportamento DIFERENTE.
    # Enquanto a Pessoa fala idade/altura, o Aluno fala o nome e a matrícula.
    def apresentar(self):
        # Usamos super().get_nome() para acessar o nome que está privado na classe mãe.
        print("Olá, meu nome é", super().get_nome(), "e minha matricula é", self.matricula)

# --- INSTANCIAÇÃO DO OBJETO FILHO ---

aluno1 = Aluno("Lana", 8, "1,51", "123456")

aluno1.estudante()  # Ação exclusiva de Aluno
aluno1.apresentar() # Ação Polimórfica (versão do Aluno)