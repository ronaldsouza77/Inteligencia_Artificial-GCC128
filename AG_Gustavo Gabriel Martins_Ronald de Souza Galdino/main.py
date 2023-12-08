# Gustavo Gabriel Martins  Matrícula: 202110838
# Ronald De Souza Galdino  Matrícula: 202110679

import numpy as np

# função para calcular a chance (de 0 a 100) de algo ocorrer dado um c qualquer

def chance(c):
    if np.random.randint(0, 100) <= c:
        return True
    else:
        return False

genes = 5
chromosomes = 4
lb = -10
ub = 10
populationSize = (chromosomes, 1)
generations = 5

#Inicialização da população
population = np.random.uniform(lb, ub, populationSize)

# transformação da população para binário
population_bin_aux = [format(int(num), '05b') for num in population.flatten()]


# tratamento dos números binários relacionado ao sinal
population_bin = []
for i in range(4):
    binary_str = ""
  # na posição 0 indicasse o sinal
    if population_bin_aux[i][0] == '-':
        for j in range(1,5):
            binary_str += population_bin_aux[i][j]
        population_bin.append("1" + binary_str)
    else:
        for j in range(1,5):
            binary_str += population_bin_aux[i][j]
        population_bin.append("0" + binary_str)


for generation in range(generations):

    print(("Generation:", generation + 1))
    fitness = []

# Treinamento da população
    for c in population:
        cf = float(c[0])
        fitness.append(
            eval("cf**2 - 3*cf + 4"))  

  # A instrução a seguir criará um array bidimensional vazio para armazenar os pais
  
    parents = []

  # Um loop para extrair um pai em cada iteração
    ultimo = ""
    penultimo = ""
    for p in range(0,4):
      # Encontrando o índice do cromossomo mais apto na população
        fittestIndex = np.where(fitness == np.max(fitness))

        # Extraindo o ultimo e o penultimo para serem substituidos pelos filhos dos que venceram o torneio
        if p == 3:
            ultimo = population_bin[fittestIndex[0][0]]
        if p == 2:
            penultimo = population_bin[fittestIndex[0][0]]
          
      # Extraindo índice do cromossomo mais apto
        fittestIndex = fittestIndex[0][0]


      # Copiando o cromossomo mais apto para o array dos pais
        parents.append(population_bin[fittestIndex])

      # Alterar a aptidão do cromossomo mais apto para evitar a nova seleção desse cromossomo
        fitness[fittestIndex] = -1

    if chance(70):

        crossoverPoint = 3

      # Índice do primeiro pai.
        parent1Index = 0

      # Índice do segundo.
        parent2Index = 1

        offspring = ''

      # Extraindo a primeira metade da prole
        offspring += parents[parent1Index][0:crossoverPoint]

      # Extraindo a segunda metade da prole
        offspring += parents[parent2Index][crossoverPoint:]

      # Extrai os bits do número binário sem considerar o sinal
        binary_str = ""
        for i in range(1,5):
            binary_str += offspring[i]
# Verifica se o número binário está ultrapassando os limites do intervado da população
        if int(binary_str, 2) > 10 and offspring[0] == '1':
            offspring = '11010'
        elif int(binary_str, 2) > 10:
            offspring = '01010'

#Substitui o ultimo pelo primeiro filho dos que venceram o torneio
        for i in range(0, 4):

            if int(population_bin[i], 2) == int(ultimo, 2):
                population_bin[i] = offspring
                break
# Desenvolvimento dos egundo filho para substituir o penultimo
        offspring = ''
        offspring += parents[parent2Index][0:crossoverPoint]
        offspring += parents[parent1Index][crossoverPoint:]

        binary_str = ""
        for i in range(1,5):
            binary_str += offspring[i]

        if int(binary_str, 2) > 10 and offspring[0] == '1':
            offspring = '11010'
        elif int(binary_str, 2) > 10:
            offspring = '01010'

        for i in range(0,4):
            if int(population_bin[i], 2) == int(penultimo, 2):
                population_bin[i] = offspring
            break

 # Garantia de 1% de chance para cada elemento da população
    for i in range(0, 4):
    
      if chance(4):
  # Índice do gene que será mutado
          randomIndexG = 0
  # Índice do cromossomo que será mutado
          randomIndexC = np.random.randint(0, chromosomes - 1)

#Tratamento para que a mutação não ocasione números > 10 ou < -10
# Neste primeiro caso, é o caso em que o bit mais significativo é 0, neste caso ele pode alterar os 3 bits anteriores
          if population_bin[randomIndexC][1] == '0':
  
              randomIndexG = np.random.randint(0, genes-2)
  
              if randomIndexG != 0:
                  randomIndexG += 1
  # Caso não seja o caso, somente os bits com valores 1 serão alterados, ou seja, o valor(módulo) do número será reduzido para 0
          else:
  
              aux = []
  # Seleciona a posição dos bits que serão alterados
              for i in range(0, len(population_bin[randomIndexC])):
  
                  if i == 1:
                      continue
                  elif population_bin[randomIndexC][i] == '1':
                      aux.append(i)
  
  
              if len(aux) == 0:
  
                  for i in range(0,5):
                      if i == 2:
                          continue
                  aux.append(i)
                
  # Sorteia o indice/bit/gene que será alterado
              randomIndexG = np.random.choice(aux)   

  # Faz a mutação
          if population_bin[randomIndexC][randomIndexG] == '0':
              mutated_c = population_bin[
              randomIndexC][:randomIndexG] + '1' + population_bin[randomIndexC][
                  randomIndexG + 1:]
          else:
              mutated_c = population_bin[
              randomIndexC][:randomIndexG] + '0' + population_bin[randomIndexC][
                  randomIndexG + 1:]
  
          population_bin[randomIndexC] = mutated_c
  

  # Convertendo populacao_bin em uma população em decimal para imprimir a população
  
  # Vai ser usado para selecionar o numero binário sem o bit que indica o sinal
    binary_str = ""
  
    population = []
    for j in range(0,4):
        if population_bin[j][0] == '1':     
            for i in range(1,5):
                binary_str += population_bin[j][i]
            population.append([-int(binary_str,2)])
            binary_str = ""

        else:
            for i in range(1,5):
                binary_str += population_bin[j][i]
            population.append([int(binary_str,2)])
            binary_str = ""
    np.array(population)
    print(population)

# Faz a verificação de qual o melhor cromossomo dada o resultado qeu ele apresenta para a função
aux = []

for c in population:
  cf = float(c[0])
  aux.append(
      eval("cf**2 - 3*cf + 4"))  

max = aux[0]
posi = 0

for i in range(1,4):
  if max < aux[i]:
    max = aux[i]
    posi = i

print(f'Resultado: {population[posi]}')