# Instruções para Executar o Código


Este código é uma implementação de um algoritmo genético que otimiza a função f(c) = c^2 - 3c + 4 com base em cromossomos representados como números binários. A otimização visa encontrar o valor de c que maximiza a função.

Para executar o código, siga estas etapas:

Certifique-se de ter o Python instalado no seu sistema. Caso contrário, você pode baixá-lo em python.org.

Garanta que a biblioteca NumPy esteja instalada. Se não estiver, você pode instalá-la usando o seguinte comando:


pip install numpy


Copie e cole o código fornecido em um arquivo Python (por exemplo, genetic_algorithm.py).

Abra um terminal e navegue até o diretório onde o arquivo Python está localizado.

Execute o código Python com o seguinte comando:

python genetic_algorithm.py

O código executará o algoritmo genético, exibindo informações sobre cada geração e, no final, imprimirá o resultado que representa o valor de c que maximiza a função.

# Breve Explicação
Este código implementa um algoritmo genético simples para otimizar a função f(c) = c^2 - 3c + 4, onde c é um número real no intervalo de -10 a 10. Aqui está uma breve explicação das principais etapas do algoritmo:

Inicialização da População: Uma população inicial de cromossomos é gerada aleatoriamente no intervalo de -10 a 10.

Codificação dos Cromossomos: Os números reais são convertidos em representações binárias, onde o primeiro bit indica o sinal.

Seleção de Pais: A seleção dos pais é realizada usando um torneio, onde os dois cromossomos mais aptos são escolhidos.

Crossover: Um ponto de cruzamento é escolhido e os bits dos pais são trocados para criar filhos. O código lida com casos em que os filhos podem ultrapassar os limites do intervalo.

Mutação: Existe uma pequena chance de mutação em que um bit de um cromossomo pode ser invertido. A mutação é tratada para garantir que os limites do intervalo não sejam violados.

Avaliação da Aptidão: A função f(c) é avaliada para cada cromossomo.

Seleção de Sobreviventes: Os filhos substituem os cromossomos menos aptos na população.

Iteração: O processo de seleção, crossover, mutação e substituição é repetido por várias gerações.

Resultado: O código imprime o resultado, ou seja, o valor de c que maximiza a função.


ALUNOS: 
 
**Gustavo Gabriel Martins  Matrícula: 202110838**

**Ronald De Souza Galdino  Matrícula: 202110679**