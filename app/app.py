from agno.agent import Agent  
   
  agent = Agent(id="Consultor de investimentos", name="Agente de Investimentos", role="Responda perguntas se baseando em fontes cientifícas e acadêmicas confiáveis", instructions=["Busque as principais fontes confiáveis sobre o problema","Entregue uma saída concisa explicando sobre o assunto do problema","Não invente links, priorize sites oficiais, artigos renomados e referências robustas", ])
     class BarraDePesquisa:  


    def __init__(self):

        self.cor = 0x000  

        self.altura = 3  

        self.largura = 5 

        self.comprimento = 5 




    def pesquisar(self):   

        self.print("Digite aqui")   

        barra_de_pesquisa = BarraDePesquisa 

        print(barra_de_pesquisa.pesquisar)  



