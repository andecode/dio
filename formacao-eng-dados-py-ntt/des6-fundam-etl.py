'''Desafio de código - Fundamentos Sobre ETL
Descrição
O processo ETL (Extract, Transform, Load) é uma etapa crítica em Business Intelligence que envolve a integração de dados provenientes de diferentes fontes para análises e relatórios. Cada etapa do processo ETL tem um papel específico na preparação dos dados para serem analisados. Complete o código associando os conceitos e etapas do processo ETL às suas respectivas descrições para entender como cada fase contribui para a análise de dados.

Entrada
A entrada é um conceito ou etapa do processo ETL para o qual você deve retornar a descrição. Os conceitos considerados são:

Extract
Transform
Load
Data Integration
Saída
A saída esperada é a descrição associada ao conceito fornecido como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente:

Processo de coletar dados de diversas fontes.
Processo de converter dados para um formato adequado.
Carregamento de dados transformados em banco de dados ou warehouse.
Unificação de dados provenientes de múltiplas fontes.
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
Extract	Processo de coletar dados de diversas fontes.
Transform	Processo de converter dados para um formato adequado.
Load	Carregamento de dados transformados em banco de dados ou warehouse.
Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

Os desafios apresentados aqui têm como objetivo principal exercitar os conceitos aprendidos e proporcionar um primeiro contato com lógica de programação. Caso não tenha experiência em programação, utilize o template disponível e preencha com os conceitos aprendidos. Para resetar o template, basta clicar em “Restart Code”.
'''
# Função responsável por receber um conceito de ETL e retornar sua descrição.
def identificar_conceito_etl(conceito):
    if conceito == "Extract":
        return "Processo de coletar dados de diversas fontes."
    elif conceito == "Transform":
        return "Processo de converter dados para um formato adequado."
    elif conceito == "Load":
        return "Carregamento de dados transformados em banco de dados ou warehouse."
    elif conceito == "Data Integration":
        return "Unificação de dados provenientes de múltiplas fontes."
    else:
        return "Conceito não reconhecido"

entrada = input()

print(identificar_conceito_etl(entrada))