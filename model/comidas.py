from database.conexao import conectar

###############################################################################################################
def mostrar_comidas_destaque():
    conexao, cursor = conectar()
    
    cursor.execute("SELECT codigo, produto, descricao, destaque, valor, imagem, disponibilidade FROM itens;")
    itens_destaque = cursor.fetchall()

    conexao.close()
    return itens_destaque
    #morre aqui
    #se fosse ter uma coluna com um nome do banco de dados e um nome diferente no programa, voce chama ele assim: valor as preco
    #se o bool for um vai estar em rapidos
    #se o bool for 0, vai star em destaque

################################################################################################################
def mostrar_comidas_rapidas(destaque:bool = 1):
    conexao, cursor = conectar()

    cursor.execute("SELECT codigo, produto, descricao, destaque, valor, imagem, disponibilidade FROM itens WHERE destaque=1;")
    #recuperando os dados do genero
    itens_rapidos = cursor.fetchall()

    #Fechando
    conexao.close()

    return itens_rapidos
    #morre aqui

################################################################################################################
def inserir_comidas(produto:str, descricao:str, valor: str, imagem: str):
    conexao, cursor = conectar()

    cursor.execute("""INSERT INTO itens (produto, descricao, valor, imagem) 
                    VALUES (%s, %s, %s, %s, %s, %s)""", [ produto, descricao,valor, imagem])

    conexao.commit()

      
    conexao.close()

#################################################################################################################
#agora vai recuperar só um produto e na pagina produtos
def mostrar_produto(codigo:str):
    conexao, cursor = conectar()
    
    cursor.execute("""SELECT codigo, produto, descricao, destaque, valor, imagem, disponibilidade FROM itens WHERE codigo= %s""", [codigo])
    produto = cursor.fetchone()

    conexao.close()
    return produto
