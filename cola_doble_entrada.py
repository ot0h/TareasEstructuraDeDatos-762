from cola import Cola


class ColaDobleEntrada(Cola):
    def add_at_beginning(self, element) -> None:
        self.elements.insert(0, element)

    def add_at_end(self, element):
        self.elements.append(element)
