from ucimlrepo import fetch_ucirepo
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import pairwise_distances
from sklearn.cluster import KMeans
import warnings
import pandas as pd

# Classe k_means_sklearn - Implementação do K-Means usando scikit-learn
class k_means_sklearn:
  
  def __init__(self, k):
     # Suprimir avisos do scikit-learn
    warnings.filterwarnings("ignore", category=FutureWarning)
    self.k = k
     # Carregar o conjunto de dados Iris
    iris = fetch_ucirepo(id=53)
    
    # Armazenar os recursos (X) e rótulos verdadeiros (Y) do conjunto de dados
    self.X = pd.DataFrame(iris.data.features)
    self.Y = iris.data.targets
    # Criar e ajustar um modelo KMeans com o número de clusters especificado
    self.model=KMeans(n_clusters=self.k)
    self.model.fit(self.X)

    
  def getClusters(self):
     # Gerar um gráfico de dispersão dos dados
    color=np.array(['Red','green','blue'])
    plt.scatter(self.X["petal length"],self.X["petal width"],c=color[self.model.labels_],s=40)
    plt.title('Classification K-means ')
    plt.show()

# Classe k_means - Implementação personalizada do K-Means
class k_means:

  def __init__(self, k):
    
    self.k = k
    
    # Inicializar listas para centroides, clusters e distâncias
    self.centroides = []    
    self.clusters = []
    self.clusters_v = []

    for i in range(self.k):
      self.clusters.append([])
      self.clusters_v.append(True)

    
    # Carregar o conjunto de dados Iris
    iris = fetch_ucirepo(id=53)
    self.X = iris.data.features
    self.Y = iris.data.targets

    # Inicializar as distancias como sendo -1
    self.distancias = []

    for i in range(len(self.X)):
      self.distancias.append([])
      for j in range(self.k):
        self.distancias[i].append([-1])
    # Inicializar centroides
    self.inicializa_centroides()

  def distancia_euclidiana(self, vetor1, vetor2):

    if len(vetor1) != len(vetor2):
      raise ValueError("Os vetores devem ter o mesmo número de elementos")
    # Calcular a distância euclidiana entre dois vetores
    soma_quadrados = sum((x - y)**2 for x, y in zip(vetor1, vetor2))
    return math.sqrt(soma_quadrados)

  def inicializa_centroides(self):
    
    self.centroides = []

    # Escolhe o primeiro centróide aleatoriamente
    primeiro_centroide = self.X.sample(n=1).iloc[0]
    self.centroides.append(primeiro_centroide)

    # Inicialização dos centróides restantes com K-Means++
    for _ in range(1, self.k):
        distancias = []
        for _, ponto in self.X.iterrows():
            # Calcula a distância mínima quadrada para os centróides atuais
            dist_min = min([np.linalg.norm(np.array(ponto) - np.array(centroide))**2 for centroide in self.centroides])
            distancias.append(dist_min)

        # Normaliza as distâncias para obter probabilidades
        probabilidades = distancias / sum(distancias)

        # Escolhe o próximo centróide com base nas probabilidades
        novo_centroide_idx = random.choices(self.X.index, weights=probabilidades)[0]
        novo_centroide = self.X.iloc[novo_centroide_idx]
        self.centroides.append(novo_centroide)
    
      
  def calcula_distancia_centroides(self):

    for i in range(len(self.X)):

      for j in range(self.k):
        # Calcula a distância euclidiana entre o ponto X.iloc[i] e o centróide self.centroides[j]
        self.distancias[i][j] = self.distancia_euclidiana(
            self.X.iloc[i], self.centroides[j])

  def menor_distancia(self):
     # Calcula a menor distância entre os pontos e os centróides para um cluster específico (j)
    self.calcula_distancia_centroides()

    menor_distancia = []

    for i in range(len(self.distancias)):
      menor_distancia.append(-1)

    for i in range(len(self.distancias)):
      # Encontra o índice do centróide mais próximo para cada ponto
      menor_distancia[i] = self.distancias[i].index(min(self.distancias[i]))

    return menor_distancia

  def soma(self, vetor1, vetor2):

    vetor_medio = []

    for i in range(len(vetor1)):
      # Soma os elementos correspondentes de dois vetores
      vetor_medio.append((vetor1[i] + vetor2[i]))

    return vetor_medio

  def calcula_media(self, vetor1, vetor2):

    vetor_medio = []

    for i in range(len(vetor1)):
      # Calcula a média dos elementos correspondentes de dois vetores
      vetor_medio.append(vetor1[i] / vetor2)

    return vetor_medio

  def atualiza_centroides(self):

    # Os índices dos centroides são armazeandos
    centroides_index = []

    for i in range(self.k):

      centroides_index.append(int(self.centroides[i].name))

    # O centroide_aux vai servir para armazenar os centroides já calculados anteriormente
    centroides_aux = []

    for i in range(self.k):
      centroides_aux.append([])

      for j in range(4):
        centroides_aux[i].append(-1)


    resul = []
    menor_distancia_resul = []
    execucoes = 5

  
    for i in range(execucoes):
      
      teste = True
      execute = False
      self.inicializa_centroides()
      tam = []
      menor_distancia = []
      
      #Enquanto houver algum centroide diferente do centroide calculado anteriormente, executa o código novamente, até que haja a convergencia dos resultados
      while (teste):

        # Aqui faz a atualização do teste para saber se o algoritmo convergiu
        for i in range(self.k):
          for j in range(4):
  
            teste = centroides_aux[i][j] != self.centroides[i][j]
  
            if (teste):
              break
              
        # Atualiza os centroides calculados anteriormente
        centroides_aux = []
        centroides_aux = self.centroides[:]

        # A menor distancia indica o indice(rótulo) do centroide mais próximo em relação a cada elemento da população
        menor_distancia = self.menor_distancia()

        # soma e tam serão utlizados para calcular o novo centroide
        soma = []
        tam = []

        #inicializa o vetor soma e tam
        for j in range(self.k):
          soma.append([])
          tam.append(0)
          for h in range(4):
            soma[j].append(0)
  
        for j in range(len(menor_distancia)):

          #Verifica se o j faz parte do indice de algum dos centroides escolhidos da 
          #primeira inicialização dos centroides
          
          #Se ele não for da primeira leva, o execute vai ser true então irá executar
          if j not in centroides_index or execute:

            #calcula a soma de todos os valores de um determinado cluster
            soma[menor_distancia[j]] = self.soma(self.X.iloc[j], soma[menor_distancia[j]])

            #calcula acreescenta o tamanho de um determinado cluster
            tam[menor_distancia[j]] += 1

    
        for j in range(len(self.centroides)):
          
          # Calcula o ponto médio dos valores de um determinado cluster
          if (tam[j] != 0):
            self.centroides[j] = self.calcula_media(soma[j], tam[j])
          else:
            self.centroides[j] = self.X.sample(n=1).iloc[0]
            
        # altera o execute para não considerar para as próximas execuções
        execute = True

      # guarda o resultado do indice de davi
      resul.append(self.calcula_davis_bouldin(menor_distancia))
      menor_distancia_resul.append(menor_distancia)

    
    # Encontrar o índice do resultado com o menor índice Davies-Bouldin    
    indice = resul.index(min(resul))
    self.getClusters(menor_distancia_resul[indice])
   

  def calcula_davis_bouldin(self, menor_distancia):
    
    # Calcula as distâncias entre os centróides de cada cluster
    distances = pairwise_distances(self.centroides)

    # Inicializa uma lista para armazenar os índices Davies-Bouldin
    davies_bouldin_indices = []

    # Calcula o índice Davies-Bouldin para cada cluster
    for i in range(self.k):
      
        # Calcula s_i, a maior distância entre o centróide do cluster i e os outros centróides
        s_i = np.max([distances[i, j] for j in range(self.k) if j != i])
        R_i = []
        for j in range(self.k):
            if j != i:
                # Encontra os índices dos elementos pertencentes aos clusters i e j
                indices_i = [idx for idx, label in enumerate(menor_distancia) if label == i]
                indices_j = [idx for idx, label in enumerate(menor_distancia) if label == j]

                # Cria subconjuntos de dados com base nos índices encontrados
                X_i = self.X.iloc[indices_i]
                X_j = self.X.iloc[indices_j]

                # Calcula a distância média entre os elementos de X_i e X_j
                mean_distance_i_to_j = np.mean(pairwise_distances(X_i, X_j))
                mean_distance_j_to_i = np.mean(pairwise_distances(X_j, X_i))

                # Calcula R_j, uma métrica que reflete a relação entre os clusters i e j
                R_j = (mean_distance_i_to_j + mean_distance_j_to_i) / s_i
                R_i.append(R_j)
        davies_bouldin_indices.append(np.max(R_i))

    # Calcula o Índice Davies-Bouldin médio, que é a média dos índices Davies-Bouldin para todos os clusters
    db_index = np.mean(davies_bouldin_indices)

    # Retorna o Índice Davies-Bouldin médio
    return db_index

  
  def getClusters(self, v):

      color=np.array(['Red','green','blue'])
      plt.scatter(self.X["petal length"],self.X["petal width"],c=color[v],s=40)
      plt.title('Classification réelle')
      plt.show()

      
 
# Número de clusters
k = 3
k_means = k_means(k)
k_means.atualiza_centroides()
# Criar uma instância da classe k_means_sklearn
k_means_sklearn = k_means_sklearn(k)
# Chamar o método para obter clusters e calcular o F1-Score
k_means_sklearn.getClusters()
