Documentação

Projeto de Cálculo Básico

O projeto consiste em um jogo simples de cálculo matemático onde o jogador deve resolver operações básicas (soma,
subtração, multiplicação e divisão) de acordo com o nível de dificuldade escolhido.
Estrutura de Arquivos

    projeto_calculo_basico/
    │
    ├── game.py
    └── models/
        └── calculator.py


- game.py: Contém a lógica principal do jogo, incluindo a interação com o usuário e a recursão para continuar jogando.

- models/calculator.py: Define a classe Calculator, responsável por gerar operações matemáticas aleatórias com base no
nível de dificuldade escolhido.

Funcionalidades

game.py:

- main(): Função principal que inicia o jogo chamando a função jogar() com zero pontos.
- jogar(pontos): Função recursiva que permite ao jogador jogar repetidamente, acumulando pontos conforme responde corretamente às operações matemáticas.

models/calculator.py:

Calculator Class:

- init(self, dificuldade): Construtor da classe que inicializa valores aleatórios para as operações com base no nível de dificuldade escolhido.
- str(self): Retorna uma representação em string dos valores e da operação atual.
- checar_resultado(self, resposta): Verifica se a resposta fornecida pelo jogador está correta para a operação atual.
- mostrar_operacao(self): Mostra a operação matemática atual para que o jogador resolva.

Para executar o jogo:

- Certifique-se de ter o Python instalado em sua máquina.
- Execute python game.py no terminal dentro do diretório do projeto.
- Siga as instruções para escolher o nível de dificuldade e responder às operações matemáticas apresentadas.# Desafios-Matematicos
