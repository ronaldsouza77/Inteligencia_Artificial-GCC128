## Alunos

Gustavo Gabriel Martins

Ronald De Souza Galdino

# K-Means Clustering

Este é um exemplo de implementação do algoritmo K-Means para clusterização de dados. Existem duas classes neste código: k_means_sklearn e k_means.

A primeira classe, k_means_sklearn, utiliza a biblioteca scikit-learn para executar o K-Means. Ele carrega o conjunto de dados Iris, que é um conjunto de dados popular usado em tarefas de classificação. Aqui está um resumo do que a classe faz e como executá-la:

## k_means_sklearn:

- Inicializa o número de clusters (K).
- Carrega o conjunto de dados Iris.
- Armazena as características (X) e os rótulos verdadeiros (Y) do conjunto de dados.
- Cria e ajusta um modelo K-Means com o número de clusters especificado.
- Faz uma plotagem de dispersão dos dados, colorindo os pontos com base nos clusters gerados.

## k_means:

- Inicializa o número de clusters (K).
- Inicializa as listas para centroides, clusters e distâncias.
- Inicializa os centroides de acordo com o algoritmo K-Means++.
- Calcula a distância euclidiana entre os pontos e os centroides.
- Encontra o cluster para cada ponto com base nas distâncias.
- Atualiza os centroides com base nos pontos atribuídos a cada cluster.
- Repete o processo até que os centroides convirjam.
- Calcula o índice Davies-Bouldin e escolhe o melhor resultado com base nele.
- Faz uma plotagem de dispersão dos dados, colorindo os pontos com base nos clusters gerados.


Ambas as classes fazem a clusterização dos dados, mas k_means é uma implementação manual do K-Means, enquanto k_means_sklearn utiliza a biblioteca scikit-learn para realizar a tarefa. Você pode escolher qual implementação deseja usar com base em seus requisitos específicos. Certifique-se de ter as bibliotecas necessárias instaladas antes de executar o código.

## Para executar o código 

1. Instale as bibliotecas necessárias:

Certifique-se de que você tenha as bibliotecas necessárias instaladas em seu ambiente Python. Você pode instalá-las usando o pip. Abra um terminal ou prompt de comando e execute os seguintes comandos:

```
pip install ucimlrepo scikit-learn pandas numpy matplotlib
```
Isso instalará as bibliotecas ucimlrepo, scikit-learn, pandas, numpy e matplotlib.

2. Execute o código
 
Você pode executar o código Python usando seu terminal ou prompt de comando. Navegue até o diretório onde você salvou o arquivo Python e execute-o usando o seguinte comando:

```
python k-means.py
```

Dependendo do número de clusters (K) escolhido e dos dados de entrada, o código executará o K-Means e exibirá um gráfico de dispersão dos clusters.

Caso prefira, instale um editor de código ou ambiente de desenvolvimento integrado (IDE) como o vs code, instale as extensões necessárias, abra o arquivo k-means.py e execute.