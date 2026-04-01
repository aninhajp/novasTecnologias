class Usuario:

    def __init__(self, id, nome, email):
        self.__id = id
        self.__nome = nome
        self.__email = None
        self.set_email(email)

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        if "@" in email:
            self.__email = email
        else:
            print("E-mail invalido")

    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | E-mail: {self.__email}"


class GerenciadorUsuarios:

    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"usuario '{usuario.get_nome()}' adicionado.")

    def remover_usuario_por_id(self, id):
        usuario_encontrado = None
        for u in self.usuarios:
            if u.get_id() == id:
                usuario_encontrado = u
        if usuario_encontrado:
            self.usuarios.remove(usuario_encontrado)
            print(f"usuario com ID {id} removido.")
        else:
            print(f"usuario com ID {id} não encontrado.")

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuario cadastrado.")
        else:
            print("\n── Lista de usuarios ──")
            for u in self.usuarios:
                print(u)



gerenciador = GerenciadorUsuarios()

u1 = Usuario(1, "Ana Julia matadora de lobisomem", "ANAContatePerseguicaogmail.com")
u2 = Usuario(2, "Ana Raquel Ratos e Fofos", "rainhaDosRatos@gmail.com")
u3 = Usuario(3, "Fellype jumento", "sehhorCapacho@gmail.com")

gerenciador.adicionar_usuario(u1)
gerenciador.adicionar_usuario(u2)
gerenciador.adicionar_usuario(u3)

gerenciador.listar_usuarios()

print("\nTestando e-mail invalido:")
u1.set_email("emailsemarroba.com")

u1.set_email("ana_novo1234456@email.com")
print(f"Novo e-mail da Ana Julia matadora de lobisomem: {u1.get_email()}")

print()
gerenciador.remover_usuario_por_id(2)
gerenciador.listar_usuarios()
