from models.calculator import Calculator


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Nível de dificuldade: [1, 2, 3, 4]\n'))
    calc: Calculator = Calculator(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()
    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você possui {pontos} pontos.')

    continuar: str = str(input('Quer continuar? [S/N] '))

    if continuar == 'S' or continuar == 's':
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} pontos.')


if __name__ == '__main__':
    main()
