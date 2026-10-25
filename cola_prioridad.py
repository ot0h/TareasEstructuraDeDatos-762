from dataclasses import dataclass
from enum import IntEnum

from cola import Cola


class Priority(IntEnum):
    EMERGENCIA = 1
    URGENTE = 2
    GENERAL = 3


@dataclass
class Paciente:
    name: str
    priority: Priority


class ColaPrioridad(Cola):
    def push(self, paciente: Paciente) -> None:
        self.elements.append(paciente)

    def sacation(self) -> Paciente | None:
        if self.is_empty():
            return None

        index = min(range(self.size_cola()), key=lambda i: self.elements[i].priority)

        return self.elements.pop(index)
