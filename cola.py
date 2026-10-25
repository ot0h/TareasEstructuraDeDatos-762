class Cola:
    def __init__(self) -> None:
        self.elements = []

    def push(self, element) -> None:
        self.elements.append(element)

    def sacation(self) -> None:
        if self.is_empty():
            return None

        return self.elements.pop(0)

    def size_cola(self) -> int:
        return len(self.elements)

    def is_empty(self) -> bool:
        return self.size_cola() == 0

    def make_empty(self) -> None:
        self.elements.clear()

    def show(self):
        return self.elements.copy()
