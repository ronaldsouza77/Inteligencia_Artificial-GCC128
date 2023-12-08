import json
import spacy
import openai
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ChatBot:
    
    def __init__(self):
        self.Questoes = []
        self.Respostas = []
        self.load_data()

    def load_data(self):
        with open('faq.json', 'r') as arquivo_json:
            dados = json.load(arquivo_json)
            
        for indice in range(0, len(dados)):
            
            self.Questoes.append(dados[indice]["Question"])
            self.Respostas.append(dados[indice]["Answer"])

        #Lematização das perguntas e das respostas. Ex: "running" será "run"
        self.Questoes = self.clean_data(self.Questoes)
        self.Respostas = self.clean_data(self.Respostas)

    def joinAnswers(self, listaRespostas):
      
      # Configure a chave de API do GPT-3
      api_key = "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"
      openai.api_key = api_key
      
      # Frase de entrada com erro de sintaxe
      frase_entrada = "Collect the answers"

      respostas = ""
      for resposta in listaRespostas:
          respostas = respostas + self.Respostas[resposta]
      
      # Use o GPT-3 para corrigir a sintaxe
      try:
        resposta = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Collect the answers: '{frase_entrada}'",
            max_tokens=50  # Ajuste conforme necessário
        )
      except:
          return respostas


      return resposta

    def clean_data(self, string_list):
        nlp = spacy.load("en_core_web_sm")
        lemmatized_list = []
        for text in string_list:
            doc = nlp(text)
            lemmatized_words = []
            for token in doc:
                lemmatized_words.append(token.lemma_)
            lemmatized_text = ' '.join(lemmatized_words)
            lemmatized_list.append(lemmatized_text)
        return lemmatized_list

    def tratamentoResposta(self, listaRespostas):
        if len(listaRespostas) == 1:
            return self.Respostas[listaRespostas[0]]
        else:
            return self.joinAnswers(listaRespostas)

    def getResposta(self, pergunta):
        questoes_proximas = self.getListQuestoesProximas(pergunta)
        print(questoes_proximas)
        questoes40 = []
        questoes20 = []
        questoes10 = []
        for i, (questao, indice, tfidf_similarity) in enumerate(questoes_proximas):
            if tfidf_similarity >= 0.40:
                questoes40.append(indice)
            if tfidf_similarity >= 0.20:
                questoes20.append(indice)
            elif tfidf_similarity >= 0.10:
                questoes10.append(indice)
            #print(f"{i+1}. Questão: {questao}")
            #print(f"   Índice: {indice}")
            #print(f"   Similaridade TF-IDF: {tfidf_similarity}")
        

        if len(questoes40) > 0:
            return self.tratamentoResposta(questoes40)
        elif len(questoes20) > 0:
            return self.tratamentoResposta(questoes20)
        elif len(questoes10) > 0:
            return self.tratamentoResposta(questoes10)
        else:
            return "Não há uma resposta conclusiva em nossa base de dados"

    def getListQuestoesProximas(self, pergunta):
        tfidf_vectorizer = TfidfVectorizer()
        X_tfidf = tfidf_vectorizer.fit_transform(self.Questoes)
        nova_pergunta_tfidf = tfidf_vectorizer.transform([pergunta])

        # Calcular as similaridades de cosseno entre a nova pergunta e todas as questões
        similarities = cosine_similarity(nova_pergunta_tfidf, X_tfidf)

        # Obter os índices das questões mais semelhantes
        top_indices = similarities.argsort()[0][-10:][::-1]

        # Criar uma lista de tuplas com as 10 questões mais semelhantes e seus índices
        top_questions = []
        for i in top_indices:
            similarity_score = similarities[0][i]
            top_questions.append((self.Questoes[i], i, similarity_score))

        return top_questions
    
    def setDataset(self, pergunta, resposta):
        # Abrir o arquivo JSON em modo de leitura para carregar os dados existentes
        with open('faq.json', 'r') as arquivo_json:
            dados = json.load(arquivo_json)

        # Adicionar o novo registro ao conjunto de dados
        novo_registro = {"Question": pergunta, "Answer": resposta}
        dados.append(novo_registro)

        # Escrever os dados atualizados de volta para o arquivo JSON
        with open('faq.json', 'w') as arquivo_json:
            json.dump(dados, arquivo_json)
    
    def conversation(self):
        while True:
            print("1 - Fazer uma pergunta")
            print("2 - Sair")
                
            op = int(input("Escolha uma opção: "))
                
            if op == 1:
                    
                # Lematização da pergunta
                pergunta = input("Qual é a sua pergunta? ")
                aux2 = pergunta
                aux = []
                aux.append(pergunta)
                self.clean_data(aux)
                pergunta = aux[0]
                
                resposta = self.getResposta(pergunta)    
                print(resposta)
                self.setDataset(aux2, resposta)
                    
            elif op == 2:
                break
                  
            else:
                print("Opção inválida. Por favor, escolha 1 ou 2.")


teste = ChatBot()
teste.conversation()