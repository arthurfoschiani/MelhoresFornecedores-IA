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