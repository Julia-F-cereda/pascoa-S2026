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