from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics
import math
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class Knn:
  
  def __init__(self):
    # Carrega o conjunto de dados Iris
    iris = datasets.load_iris()
    X = iris.data  
    y = iris.target  
    # Divide o conjunto de dados em treinamento e teste
    self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.7, random_state=3)
    self.y_test_class = []  # Lista para armazenar as classes previstas
    self.scores = []  # Lista para armazenar os resultados de score
    self.k = 20   # Valor de k para o algoritmo k-NN

    self.classifica()  # Chama o método para classificar os pontos de teste


  def distancia_euclidiana(self, vetor1, vetor2):
    # Calcula a distância euclidiana entre dois vetores
    if len(vetor1) != len(vetor2):
      raise ValueError("Os vetores devem ter o mesmo número de elementos")
    # Calcular a distância euclidiana entre dois vetores
    soma_quadrados = sum((x - y)**2 for x, y in zip(vetor1, vetor2))
    return math.sqrt(soma_quadrados)

  def classifica(self):

    # Calcular a distância euclidiana entre cada ponto de teste e cada ponto de treinamento
    for i in range(len(self.X_test)):
      
      distancias = []
      self.y_test_class.append([]) # Inicializa a lista para as classes previstas
      
      for j in range(len(self.X_train)):
        distancias.append((self.distancia_euclidiana(self.X_test[i], self.X_train[j]), j))

      distancias_ordenadas = sorted(distancias, key=lambda x: x[0])

      for j in range(self.k):

        cont0 = 0
        soma0 = 0
        
        cont1 = 0
        soma1 = 0
        
        cont2 = 0
        soma2 = 0
        
        for k in range(j+1):
          
          if self.y_train[distancias_ordenadas[k][1]] == 0:
            cont0 += 1
            soma0 += distancias_ordenadas[k][0]
            
          elif self.y_train[distancias_ordenadas[k][1]] == 1:
            cont1 += 1
            soma1 += distancias_ordenadas[k][0]
            
          elif self.y_train[distancias_ordenadas[k][1]] == 2:
            cont2 += 1
            soma0 += distancias_ordenadas[k][0]
            
        # Classificação com base em contagem e soma de distâncias
        if cont0 > cont1 and cont0 > cont2:
          self.y_test_class[i].append(0)
            
        elif cont1 >cont0 and cont1 > cont2:
          self.y_test_class[i].append(1)
        
        elif cont2 > cont0 and cont2 > cont1:
          self.y_test_class[i].append(2)
          
        elif cont0 == cont1:
          if soma0 > soma1:
            self.y_test_class[i].append(1)
          else:
            self.y_test_class[i].append(0)

        elif cont1 == cont2:
          if soma1 > soma2:
            self.y_test_class[i].append(2)
          else:
            self.y_test_class[i].append(1)

        elif cont0 == cont2:
          if soma0 > soma2:
            self.y_test_class[i].append(2)
          else:
            self.y_test_class[i].append(0)
            
    self.score() # Calcula o score do modelo
    
  def score(self):
        
    score_list = []
    for i in range(self.k):
      aux = []

      for y in self.y_test_class:
        aux.append(y[i])
        
      score_list.append(metrics.accuracy_score(self.y_test,aux))
    
    numeros = []
    for i in range(1, len(score_list)+1):
      numeros.append(i)

    # Calcula a matriz de confusão
    confusion_matrices = []

    for i in range(self.k):
        aux = []
        for y in self.y_test_class:
            aux.append(y[i])

        confusion_matrices.append(confusion_matrix(self.y_test, aux))

        print(f"Matriz de Confusão para k = {i+1}:\n{confusion_matrices[i]}")

    numeros = list(range(1, len(confusion_matrices) + 1))

    # Plota a matriz de confusão para o último valor de k
    plt.figure(figsize=(8, 6))
    sns.heatmap(confusion_matrices[-1], annot=True, fmt="d", cmap="Blues", cbar=False)
    plt.title(f"Matriz de Confusão para k = {self.k}")
    plt.xlabel("Valores Previstos")
    plt.ylabel("Valores Reais")
    plt.show()
    
    # Plota o gráfico de score em função de k
    plt.plot(numeros, score_list)
    plt.xlabel("num K")
    plt.ylabel("Score %")
    plt.show()
        
knn = Knn() # Cria uma instância da classe Knn para executar o código