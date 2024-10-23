class Node:
    # Classe que representa um nó na lista duplamente encadeada.
    def __init__(self, data):
        self.data = data  # Dado armazenado no nó
        self.next = None  # Referência para o próximo nó
        self.prev = None  # Referência para o nó anterior

class ListaDuplamenteEncadeada:
    # Classe que representa a lista duplamente encadeada.
    def __init__(self):
        self.head = None  # Referência para o primeiro nó da lista
        self.tail = None  # Referência para o último nó da lista

    def incluir(self, data):
        # Inclui um novo nó com o dado fornecido no final da lista.
        new_node = Node(data)  # Cria um novo nó
        if self.head is None:
            # Se a lista estiver vazia, o novo nó é o primeiro e o último nó
            self.head = self.tail = new_node
        else:
            # Caso contrário, adiciona o novo nó ao final da lista
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remover(self, ra):
        # Remove o nó que contém o aluno com o RA fornecido.
        current = self.head  # Começa pelo primeiro nó
        while current:
            if current.data.aluno.ra == ra:
                # Se encontrar o nó com o RA fornecido, ajusta as referências
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return True  # Retorna True se o nó foi removido
            current = current.next
        return False  # Retorna False se o nó não foi encontrado

    def consultar(self, ra):
        # Consulta e retorna o nó que contém o aluno com o RA fornecido.
        current = self.head  # Começa pelo primeiro nó
        while current:
            if current.data.aluno.ra == ra:
                return current.data  # Retorna o dado do nó encontrado
            current = current.next
        return None  # Retorna None se o nó não foi encontrado

    def exibir(self):
        # Exibe todos os nós da lista.
        current = self.head  # Começa pelo primeiro nó
        while current is not None:
            print(current.data)  # Imprime o dado do nó atual
            current = current.next  # Move para o próximo nó

    def __iter__(self):
        # Torna a lista iterável.
        current = self.head  # Começa pelo primeiro nó
        while current is not None:
            yield current.data  # Retorna o dado do nó atual
            current = current.next  # Move para o próximo nó