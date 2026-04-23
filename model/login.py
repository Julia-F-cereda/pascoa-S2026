from database.conexao import conectar
def inserir_usuario(usuario: str, senha: str, nome: str="Anonimo"):
    conexao, cursor = conectar()
    cursor.execute("""INSERT INTO login (usuario, senha, nome)
    VALUES(%s, %s, %s)""", [usuario, senha, nome])
    conexao.commit()
    conexao.close()

def conferir_usuario(usuario:str, senha:str) -> list:
        conexao, cursor = conectar()
        cursor.execute(""" SELECT NOME FROM login WHERE USUARIO=%s AND SENHA=%s""", [usuario, senha])
        usuario = cursor.fetchone()
        conexao.close()

        return usuario
