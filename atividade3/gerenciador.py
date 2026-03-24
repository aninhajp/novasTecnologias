class Equipamento:
    def __init__(self, id_equipamento, nome, preco_diaria):
        self.id_equipamento = id_equipamento
        self.nome = nome
        self.preco_diaria = preco_diaria
        self.status = "Disponível"

    def alugar(self):
        self.status = "Alugado"

    def devolver(self):
        self.status = "Disponível"

class Locadora:
    def __init__(self):
        self.inventario = []
        self.faturamento_por_cliente = {}

    def cadastrar_equipamento(self, equipamento):
        self.inventario.append(equipamento)

    def realizar_locacao(self, nome_cliente, id_equipamento, dias):
        for item in self.inventario:
            if item.id_equipamento == id_equipamento and item.status == "Disponível":
                item.alugar()
                custo = item.preco_diaria * dias
                
                total_atual = self.faturamento_por_cliente.get(nome_cliente, 0)
                self.faturamento_por_cliente[nome_cliente] = total_atual + custo
                return f"Locação de {item.nome} feita para {nome_cliente}!"
        return "Equipamento não disponível."

    def equipamentos_disponiveis(self):
        return [e.nome for e in self.inventario if e.status == "Disponível"]

loja_estoque_de_vento = Locadora()
e1 = Equipamento(1, "Projetor", 50.0)
loja_estoque_de_vento.cadastrar_equipamento(e1)

print(loja_estoque_de_vento.equipamentos_disponiveis())
loja_estoque_de_vento.realizar_locacao("Ana Julia", 1, 3)
print(loja_estoque_de_vento.faturamento_por_cliente)