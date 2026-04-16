from database.conexao import conectar
def inserir_usuario(usuario: str, senha: str):
    conexao, cursor = conectar()
    cursor.execute("""INSERT INTO login (usuario, senha)
    VALUES(%s, %s)""", [usuario, senha])
    conexao.commit()
    conexao.close()

# def conferir_usuario(nome:str, senha:str):
#         conexao, cursor = conectar()
#         cursor.execute(""" SELECT NOME, SENHA FROM login WHERE NOME=%s AND SENHA=%s""", [nome, senha])
#         usuario = cursor.fetchone()
#         conexao.close()
