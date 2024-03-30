import pandas as pd

def calcular_pontuacao(fornecedor, fornecedores_conhecidos):
    pontuacao = fornecedor['Avaliação do Cliente'] * 15
    pontuacao += 20 if fornecedor['Frete Grátis'] else 0
    pontuacao += 5 if fornecedor['Escolha Ideal'] else 0
    pontuacao += 15 if fornecedor['Práticas Sustentáveis'] else 0
    pontuacao += fornecedor['Tempo de Mercado (anos)'] / 2
    pontuacao += 50 if fornecedor['ID Fornecedor'] in fornecedores_conhecidos else 0
    pontuacao -= fornecedor['Preço'] / 10
    return pontuacao

def melhores_fornecedores(produtos_solicitados, fornecedores_conhecidos):
    data = pd.read_csv('datasets/dataset_fornecedores_atualizado.v3.csv')
    data['Pontuação'] = data.apply(calcular_pontuacao, fornecedores_conhecidos=fornecedores_conhecidos, axis=1)
    fornecedores_com_produtos = data.groupby('ID Fornecedor').filter(lambda x: produtos_solicitados.issubset(set(x['Nome do Produto'])))
    produtos_desejados = fornecedores_com_produtos[fornecedores_com_produtos['Nome do Produto'].isin(produtos_solicitados)]
    pontuacao_media = produtos_desejados.groupby('ID Fornecedor')['Pontuação'].mean()
    melhores_fornecedores_ids = pontuacao_media.sort_values(ascending=False).head(3).index.tolist()
    return melhores_fornecedores_ids, fornecedores_com_produtos