## Alunos:

Gustavo Gabriel Martins

Ronald De Souza Galdino

# Agentes RandomVacuumAgent 4 places

Este é um código simples em Python que simula o funcionamento de um agente aspirador de pó em um ambiente com quatro locais. O agente é representado pela classe Agente, e o ambiente é modelado pela classe Ambiente. O agente toma decisões para se movimentar no ambiente e limpar locais sujos.

## Lógica do Agente

O agente possui uma lógica simples para decidir seu movimento e ação em cada posição do ambiente. A lógica inclui:

1.**Limpeza** : Se o agente encontra um local sujo, ele o limpa.

2.**Movimentação**: O agente decide para qual local se movimentar, seguindo uma lógica específica para cada posição no ambiente.

## Funcionamento do Código

O código é dividido em duas classes principais:

1. `Agente`

- __init__(self): Inicializa o agente com a posição (0,0), sem local anterior.

- setLocalization(self, localization): Define a posição do agente.

- getLocalization(self): Retorna a posição atual do agente.

- exec(self, status): Executa a lógica do agente, limpando se estiver sujo e decidindo o movimento.

2. `Ambiente`

- __init__(self): Inicializa o ambiente com quatro locais e um agente.

- ambienteMovimento(self): Simula o movimento do agente e a sujeira aleatória nos locais.

## Execução

- Certifique-se de ter o Python instalado em sua máquina.

- Abra um terminal na pasta onde o arquivo está localizado.

- Execute o seguinte comando:

```
python agente_aspirador.py
```

- **Observe a saída no terminal para ver a simulação em andamento.**