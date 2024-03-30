from faker import Faker
from database.connection import get_connection
from database.db_queries import create_sequence_fornecedor, inserir_pessoa, inserir_pj, inserir_fornecedor

def criar_fornecedores(cursor, n):
    for _ in range(n):
        nome_empresa = fake.company()
        email_forn = fake.email()
        cnpj = fake.ssn()

        id_pessoa = inserir_pessoa(cursor, nome_empresa)
        id_pj = inserir_pj(cursor, cnpj, id_pessoa)
        inserir_fornecedor(cursor, email_forn, id_pj)
        
conexao = get_connection()
cursor = conexao.cursor()

fake = Faker()

# create_sequence_fornecedor(cursor)

criar_fornecedores(cursor, 100)

conexao.commit()
cursor.close()
conexao.close()

print("Fornecedores inseridos com sucesso!")