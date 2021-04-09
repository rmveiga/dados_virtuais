from random import randint


class DadoVirtual:

    def __init__(self, faces: int):
        self.faces = faces

    def __repr__(self):
        return f'D{self.faces}'

    def rolar(self) -> int:
        return randint(1, self.faces)


if __name__ == '__main__':
    total_dados = 1
    dados = [DadoVirtual(6) for i in range(total_dados)]

    print(dados)
    resultado = sum([dado.rolar() for dado in dados])
    print(resultado)
