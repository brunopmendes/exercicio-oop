class Contato:
    

    def __init__(self, nome: str, telefone: int) -> None:
        self.nome = nome
        self.telefone = telefone


    def exibir_info(self) -> str:
        return f'nome: {self.nome}, telefone: {self.telefone}'


    def __str__(self) -> str:
        return f'nome: {self.nome}, telefone: {self.telefone}'



class Agenda:


    def __init__(self) -> None:
        self.contatos = []


    def adicionar_contatos(self, contato: Contato) -> None:
        self.contatos.append(contato)


    def buscar_contato(self, nome_contato: str) -> Contato:
        for contato in self.contatos:
            if contato.nome == nome_contato:
                return contato


    def remover_contato(self, nome_contato: str) -> None:
        for contato in self.contatos:
            if contato.nome == nome_contato:
                self.contatos.remove(contato)


    def __str__(self) -> str:
        return '\n'.join([contato.exibir_info() for contato in self.contatos])
    

if __name__ == '__main__':
    c1 = Contato('Bruno', 11983903316)
    c2 = Contato('Felipe', 11983482304)
    # print(c1.exibir_info())

    ag1 = Agenda()
    ag1.adicionar_contatos(c1)
    ag1.adicionar_contatos(c2)
    # print(ag1.buscar_contato('Bruno'))
    # c1.telefone = 11983090944
    # print(ag1.buscar_contato('Bruno'))
    ag1.remover_contato('Felipe')
    print(ag1)

