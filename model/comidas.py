from database.conexao import conectar

def mostrar_comidas_destaque(destaque:bool = 0):
    conexao, cursor = conectar()
    #executado consulta genero
    
    cursor.execute("SELECT codigo, produto, descricao, destaque, valor, imagem, disponibilidade FROM itens WHERE destaque=0;")
    itens_destaque = cursor.fetchall()
    #Fechando
    conexao.close()
    return itens_destaque

def mostrar_comidas_rapidas(destaque:bool = 1):
    conexao, cursor = conectar()

    cursor.execute("SELECT codigo, produto, descricao, destaque, valor, imagem, disponibilidade FROM itens WHERE destaque=1;")
    #recuperando os dados do genero
    itens_rapidos = cursor.fetchall()

    #Fechando
    conexao.close()

    return itens_rapidos

def inserir_comidas(produto:str, descricao:str, valor: str, imagem: str):
    conexao, cursor = conectar()

    cursor.execute("""INSERT INTO itens (produto, descricao, valor, imagem) 
                    VALUES (%s, %s, %s, %s, %s, %s)""", [ produto, descricao,valor, imagem])

    conexao.commit()

      
    conexao.close()