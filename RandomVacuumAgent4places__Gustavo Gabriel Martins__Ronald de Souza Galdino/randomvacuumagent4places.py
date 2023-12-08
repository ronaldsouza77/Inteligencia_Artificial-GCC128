import random
import time
from typing import Literal, Tuple, Union

class Agente:

  def __init__(self):
    # Inicialização do agente
    self.agente = 0
    self.localization = (0,0)
    self.anterior = ()

  def setLocalization(self, localization):
    # Método para definir a localização do agente
    self.localization = localization

  def getLocalization(self) -> Union[Tuple[Literal[0], Literal[0]], Tuple[Literal[0], Literal[1]], Tuple[Literal[1], Literal[0]], Tuple[Literal[1], Literal[1]]]:
      # Método para obter a localização do agente
      return self.localization

  def exec(self, status):
    # Método que implementa a lógica do agente
    # Se o local estiver sujo, limpa; caso contrário, decide para onde se movimentar

    acao = ""

    if status == 'Dirty':
      status = 'Clean'
      acao = 'Limpar'

    elif self.localization == (0,0):
       # Lógica específica para a posição (0,0)
      if self.anterior == ():
        self.anterior = self.localization
        local_selecionado = random.choice([(0,1), (1,0)])
        acao = 'Direita' if local_selecionado == (0, 1) else 'Baixo'
        self.setLocalization(local_selecionado)

      elif self.anterior == (0,1):
        acao = 'Baixo'
        self.anterior = (0,0)
        self.setLocalization((1,0))

      elif self.anterior == (1,0):
        acao = 'Direita'
        self.anterior = (0,0)
        self.setLocalization((0,1))

    elif self.localization == (0,1):
       # Lógica específica para a posição (0,1)
      if self.anterior == ():
        self.anterior = self.localization
        local_selecionado = random.choice([(0,0), (1,1)])
        acao = 'Esquerda' if local_selecionado == (0, 0) else 'Baixo'
        self.setLocalization(local_selecionado)

      elif self.anterior == (0,0):
        acao = 'Baixo'
        self.anterior = (0,1)
        self.setLocalization((1,1))

      elif self.anterior == (1,1):
        acao = 'Esquerda'
        self.anterior = (0,1)
        self.setLocalization((0,0))

    elif self.localization == (1,0):
        # Lógica específica para a posição (1,0)
      if self.anterior == ():
        self.anterior = self.localization
        local_selecionado = random.choice([(0,0), (1,1)])
        acao = 'Cima' if local_selecionado == (0, 0) else 'Direita'
        self.setLocalization(local_selecionado)

      elif self.anterior == (0,0):
        acao = 'Direita'
        self.anterior = (1,0)
        self.setLocalization((1,1))

      elif self.anterior == (1,1):
        acao = 'Cima'
        self.anterior = (1,0)
        self.setLocalization((0,0))

    elif self.localization == (1,1):
      # Lógica específica para a posição (1,1)
      if self.anterior == ():
        self.anterior = self.localization
        local_selecionado = random.choice([(1,0), (0,1)])
        acao = 'Esquerda' if local_selecionado == (1, 0) else 'Cima'
        self.setLocalization(local_selecionado)

      elif self.anterior == (1,0):
        acao = 'Cima'
        self.anterior = (1,1)
        self.setLocalization((0,1))

      elif self.anterior == (0,1):
        acao = 'Esquerda'
        self.anterior = (1,1)
        self.setLocalization((1,0))


    return status, acao


class Ambiente:

  def __init__(self):
    # Inicialização do ambiente com quatro locais
    loc_A, loc_B, loc_C, loc_D = (0, 0), (0, 1), (1, 0), (1, 1)

    self.locais = [loc_A, loc_B, loc_C, loc_D]

    # Inicialização do agente e definição do estado inicial do ambiente
    self.agente = Agente()

    self.status = {loc_A: random.choice(['Clean', 'Dirty']),
       loc_B: random.choice(['Clean', 'Dirty']),
       loc_C: random.choice(['Clean', 'Dirty']),
       loc_D: random.choice(['Clean', 'Dirty'])}

  def ambienteMovimento(self):
    # Seleção aleatória de um local para o agente se movimentar
    local_selecionado = random.choice(self.locais)
    self.agente.setLocalization(local_selecionado)

    print("00  01\n10  11")
    print()

    while True:
       # Lógica para sujeira aparecer aleatoriamente nos locais
      if self.status.get((0,0)) == 'Clean':
        aux = random.choice([0, 0, 1])
        if aux:
          self.status[(0,0)] = 'Dirty'

      elif self.status.get((0,1)) == 'Clean':
        aux = random.choice([0, 0, 1])
        if aux:
          self.status[(0,1)] = 'Dirty'

      elif self.status.get((1,0)) == 'Clean':
        aux = random.choice([0, 0, 1])
        if aux:
          self.status[(1,0)] = 'Dirty'

      elif self.status.get((1,1)) == 'Clean':
        aux = random.choice([0, 0, 1])
        if aux:
          self.status[(1,1)] = 'Dirty'
          
      # Exibição do estado atual do ambiente e execução da lógica do agente  
      print('Localização atual: ', self.agente.getLocalization())
      print('Status atual: ', self.status)
      self.status[self.agente.getLocalization()], acao = self.agente.exec(self.status.get(self.agente.getLocalization()))
      print('Ação que será realizada: ', acao)
      time.sleep(3)
      print()

# Criação do ambiente e execução da simulação    
ambiente = Ambiente()

ambiente.ambienteMovimento()