def montar_payload(fornecedores_info, fornecedores_com_produtos, produtos_solicitados):
    resposta = []
    for info in fornecedores_info:
        id_fornecedor, nome_fornecedor, email_fornecedor = info
        produtos_do_fornecedor = fornecedores_com_produtos[
            (fornecedores_com_produtos['ID Fornecedor'] == id_fornecedor) &
            (fornecedores_com_produtos['Nome do Produto'].isin(produtos_solicitados))
        ]
        produtos = []
        for _, produto in produtos_do_fornecedor.iterrows():
            produtos.append({
                'nomeProduto': produto['Nome do Produto'],
                'preco': produto['Preço'],
                'freteGratis': produto['Frete Grátis'],
                'avaliacao': produto['Avaliação do Cliente'],
                'tempoVendendo': produto['Tempo de Mercado (anos)'],
                'localizacao': produto['Localização do Fornecedor'],
                'praticasSustentaveis': produto['Práticas Sustentáveis']
            })
        resposta.append({
            'idFornecedor': id_fornecedor,
            'nomeFornecedor': nome_fornecedor,
            'emailFornecedor': email_fornecedor,
            'produtos': produtos
        })
    return resposta