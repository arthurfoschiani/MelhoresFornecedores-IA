from flask import request, jsonify
from app import app
from data.data_processing import melhores_fornecedores
from database.connection import get_connection
from database.db_queries import get_fornecedor_info
from app.utils import montar_payload

@app.route('/melhores-fornecedores', methods=['POST'])
def obter_melhores_fornecedores():
    request_data = request.json
    produtos_solicitados = set(request_data['produtos'])
    fornecedores_conhecidos = request_data['fornecedoresConhecidos']

    melhores_fornecedores_ids, fornecedores_com_produtos = melhores_fornecedores(produtos_solicitados, fornecedores_conhecidos)

    conexao = get_connection()
    cursor = conexao.cursor()
    melhores_fornecedores_info = get_fornecedor_info(cursor, melhores_fornecedores_ids)

    resposta = montar_payload(melhores_fornecedores_info, fornecedores_com_produtos, produtos_solicitados)

    return jsonify(resposta)