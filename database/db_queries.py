import oracledb

def get_fornecedor_info(cursor, fornecedor_ids):
    query = """
    SELECT f.id_pj, p.nome_pessoa, f.email_forn
    FROM fornecedor f
    JOIN pj ON f.id_pj = pj.id_pessoa
    JOIN pessoa p ON pj.id_pessoa = p.id_pessoa
    WHERE f.id_pj IN (:1, :2, :3)
    """
    cursor.execute(query, fornecedor_ids)
    return cursor.fetchall()

def create_sequence_fornecedor(cursor):
    cursor.execute("""
        CREATE SEQUENCE pessoa_seq
            START WITH 1
            INCREMENT BY 1
            NOCACHE
            NOCYCLE
    """)

def inserir_pessoa(cursor, nome_empresa):
    id_var = cursor.var(oracledb.NUMBER)
    cursor.execute("""
        INSERT INTO pessoa (id_pessoa, nome_pessoa) VALUES (pessoa_seq.NEXTVAL, :nome)
        RETURNING id_pessoa INTO :id
    """, [nome_empresa, id_var])
    return id_var.getvalue()[0]

def inserir_pj(cursor, cnpj, id_pessoa):
    id_var = cursor.var(oracledb.NUMBER)
    cursor.execute("""
        INSERT INTO pj (cnpj, id_pessoa) VALUES (:cnpj, :id_pessoa)
        RETURNING id_pessoa INTO :id
    """, [cnpj, id_pessoa, id_var])
    return id_var.getvalue()[0]

def inserir_fornecedor(cursor, email_forn, id_pj):
    cursor.execute("""
        INSERT INTO fornecedor (dt_entrada, email_forn, id_pj) VALUES (SYSDATE, :email, :id_pj)
    """, [email_forn, id_pj])