## Alunos:

Gustavo Gabriel Martins

Ronald De Souza Galdino

# Classificação com k-NN

Este projeto demonstra um exemplo de classificação de dados utilizando o algoritmo k-NN (k-Nearest Neighbors) com Python e a biblioteca scikit-learn. O código é um classificador k-NN personalizado que classifica pontos de teste com base em distâncias euclidianas e calcula a matriz de confusão para diferentes valores de k, além de plotar um gráfico de score em função de k.

## Lógica do código:

O código consiste em uma classe Knn que realiza o seguinte processo:

1. Carregamento do Conjunto de Dados Iris:

O código carrega o conjunto de dados Iris, um conjunto de dados de classificação de flores em três classes (Setosa, Versicolor e Virginica). O conjunto de dados é dividido em atributos (features) e rótulos (labels).

2. Divisão dos Dados em Treinamento e Teste:

Os dados são divididos em conjuntos de treinamento e teste usando a função train_test_split da biblioteca scikit-learn. Neste exemplo, 70% dos dados são usados para treinamento e 30% para teste.

3. Cálculo da Distância Euclidiana:

A classe Knn define um método distancia_euclidiana para calcular a distância euclidiana entre dois vetores.

4. Classificação k-NN:

A classe Knn contém um método classifica que executa o algoritmo k-NN. Para cada ponto de teste, ele calcula as distâncias euclidianas em relação aos pontos de treinamento, classifica os pontos com base em k, onde k é o número de vizinhos considerados. O código realiza uma classificação baseada na contagem e soma das distâncias dos vizinhos mais próximos.

5. Cálculo do Score:

O método score calcula o score do modelo para diferentes valores de k e, em seguida, cria um gráfico de score em função de k.

6. Matriz de Confusão:

Para cada valor de k, o código calcula e imprime a matriz de confusão. A matriz de confusão mostra o desempenho da classificação, incluindo verdadeiros positivos, falsos positivos, verdadeiros negativos e falsos negativos.

7. Plotagem da Matriz de Confusão:

A matriz de confusão é plotada usando a biblioteca seaborn e matplotlib. O último valor de k é usado para criar o gráfico.

## Execução do Código

Para executar o código, siga estas etapas:

1. Instale as bibliotecas necessárias:

Certifique-se de que você tenha as seguintes bibliotecas Python instaladas:

- scikit-learn
- seaborn
- matplotlib
- numpy

Você pode instalar essas bibliotecas usando o pip. Exemplo:
```
pip install scikit-learn seaborn matplotlib numpy
```

2. Execute o código:

Execute o arquivo Python que contém o código do projeto.

Por exemplo, se o código estiver no arquivo knn.py, você pode executá-lo da seguinte forma:
```
python knn.py
```

3. Visualize os resultados:

O código imprimirá a matriz de confusão para diferentes valores de k e plotará um gráfico de score em função de k. Você poderá analisar os resultados diretamente no terminal e os gráficos gerados. 

**(Obs: Primeiramente será exibido a matriz de confusão, e, quando fechar ela será exibido o grafico do score em função de k.)**