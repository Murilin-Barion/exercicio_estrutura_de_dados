import ctypes

class Node(ctypes.Structure):
    """
    Classe que representa um nó na lista duplamente encadeada.
    """
    _fields_ = [("data", ctypes.py_object),
                ("next", ctypes.POINTER(ctypes.py_object)),
                ("prev", ctypes.POINTER(ctypes.py_object))]

    def __init__(self, data):
        self.data = data  # Dado armazenado no nó
        self.next = ctypes.pointer(ctypes.py_object(None))  # Ponteiro para o próximo nó
        self.prev = ctypes.pointer(ctypes.py_object(None))  # Ponteiro para o nó anterior

class ListaDuplamenteEncadeada:
    """
    Classe que representa a lista duplamente encadeada.
    """
    def __init__(self):
        self.head = ctypes.pointer(ctypes.py_object(None))  # Ponteiro para o primeiro nó da lista
        self.tail = ctypes.pointer(ctypes.py_object(None))  # Ponteiro para o último nó da lista

    def incluir(self, data):
        """
        Inclui um novo nó com o dado fornecido no final da lista.
        """
        new_node = Node(data)  # Cria um novo nó
        if not self.head.contents:
            # Se a lista estiver vazia, o novo nó é o primeiro e o último nó
            self.head.contents = new_node
            self.tail.contents = new_node
        else:
            # Caso contrário, adiciona o novo nó ao final da lista
            self.tail.contents.next.contents = new_node
            new_node.prev.contents = self.tail.contents
            self.tail.contents = new_node

    def remover(self, ra):
        """
        Remove o nó que contém o aluno com o RA fornecido.
        """
        current_ptr = self.head
        while current_ptr.contents:
            current = current_ptr.contents
            if current.data.aluno.ra == ra:
                if current.prev.contents:
                    current.prev.contents.next.contents = current.next.contents
                if current.next.contents:
                    current.next.contents.prev.contents = current.prev.contents
                if current_ptr.contents == self.head.contents:
                    self.head.contents = current.next.contents
                if current_ptr.contents == self.tail.contents:
                    self.tail.contents = current.prev.contents
                return True  # Retorna True se o nó foi removido
            current_ptr = current.next
        return False  # Retorna False se o nó não foi encontrado

    def consultar(self, ra):
        """
        Consulta e retorna o nó que contém o aluno com o RA fornecido.
        """
        current_ptr = self.head
        while current_ptr.contents:
            current = current_ptr.contents
            if current.data.aluno.ra == ra:
                return current.data  # Retorna o dado do nó encontrado
            current_ptr = current.next
        return None  # Retorna None se o nó não foi encontrado

    def exibir(self):
        """
        Exibe todos os nós da lista.
        """
        current_ptr = self.head
        while current_ptr.contents:
            current = current_ptr.contents
            print(f"Dado: {current.data}, Endereço de memória: {ctypes.addressof(current)}")  # Imprime o dado e o endereço de memória do nó atual
            current_ptr = current.next  # Move para o próximo nó

    def __iter__(self):
        """
        Torna a lista iterável.
        """
        current_ptr = self.head
        while current_ptr.contents:
            current = current_ptr.contents
            yield current.data  # Retorna o dado do nó atual
            current_ptr = current.next  # Move para o próximo nó

    def ordenar_por_ra(self):
        """
        Ordena a lista de matrículas pelo RA do aluno usando Radix Sort.
        """
        if not self.head.contents:
            return

        # Encontra o maior RA na lista
        max_ra = self.head.contents.data.aluno.ra
        current_ptr = self.head.contents.next
        while current_ptr.contents:
            current = current_ptr.contents
            if current.data.aluno.ra > max_ra:
                max_ra = current.data.aluno.ra
            current_ptr = current.next

        # Aplica Radix Sort
        exp = 1
        while max_ra // exp > 0:
            self._counting_sort(exp)
            exp *= 10

    def _counting_sort(self, exp):
        """
        Função auxiliar para o Radix Sort.
        """
        output = [None] * self._length()
        count = [0] * 10

        current_ptr = self.head
        while current_ptr.contents:
            current = current_ptr.contents
            index = (current.data.aluno.ra // exp) % 10
            count[index] += 1
            current_ptr = current.next

        for i in range(1, 10):
            count[i] += count[i - 1]

        current_ptr = self.tail
        while current_ptr.contents:
            current = current_ptr.contents
            index = (current.data.aluno.ra // exp) % 10
            output[count[index] - 1] = current.data
            count[index] -= 1
            current_ptr = current.prev

        current_ptr = self.head
        for i in range(len(output)):
            current_ptr.contents.data = output[i]
            current_ptr = current_ptr.contents.next

    def _length(self):
        """
        Retorna o comprimento da lista.
        """
        count = 0
        current_ptr = self.head
        while current_ptr.contents:
            count += 1
            current_ptr = current_ptr.contents.next
        return count