from database.conexao import conectar

def recuperar_carrinho(usuario: str) -> list:
    conexao, cursor = conectar()
    cursor.execute(""" SELECT 
    carrinho.cod_carrinho, 
    carrinho.cod_usuario, 
    carrinho.data, 
    carrinho.finalizado, 
    itens.produto,
    item_carrinho.quantidade,
    itens.valor, 
    itens.imagem 
    FROM carrinho 
    INNER JOIN item_carrinho ON carrinho.cod_carrinho = item_carrinho.cod_carrinho
    INNER JOIN itens ON itens.codigo = item_carrinho.cod_carrinho
    WHERE carrinho.cod_usuario = %s;
                    """, [usuario])
    recuperar = cursor.fetchall()
    conexao.close()
    return recuperar

def inserir_item(cod_usuario, cod_itens, quantidade):
    conexao, cursor = conectar()
    cursor.execute(""" SELECT cod_carrinho from carrinho WHERE cod_usuario = %s AND finalizado = 0 limit 1;""", [cod_usuario])
    resultado_carrinho = cursor.fetchone()

    if resultado_carrinho:
        codigo_carrinho = resultado_carrinho["cod_carrinho"]
    else:
        cursor.execute(""" INSERT INTO carrinho (cod_usuario)
                       VALUES (%s)""", [cod_usuario])
        codigo_carrinho = cursor.lastrowid

        cursor.execute(""" INSERT INTO item_carrinho (cod_carrinho, cod_itens, quantidade) VALUES (%s, %s, %s);""",[codigo_carrinho, cod_itens,quantidade])

        conexao.commit()  
        conexao.close()