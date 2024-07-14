from math import factorial, sqrt
from fractions import Fraction
from prettytable import PrettyTable
from typing import Final, Tuple, List, Callable, NewType


# the function of calculating the number of combinations
C: Callable[[int, int], int] = lambda n, k: factorial(n) / (factorial(k) * factorial(n - k))

greek: Final = {  # греческие символы
        "epsi" : chr(958),
        "nu" : chr(951)
    }

# type alias
Pair = NewType('Pair', 'Tuple[int]')

"""
---------------------------
| ВВЕСТИ ПАРАМЕТРЫ ЗАДАЧИ |
---------------------------
n1: Final[int] = 5
n2: Final[int] = 3
n3: Final[int] = 2
m:  Final[int] = 6
a:  Tuple[int] = (2, 2)
b:  Tuple[int] = (3, 4)
c:  Tuple[int] = (4, 2)
d:  Tuple[int] = (6, 3)
------------------------"""

def solve(n1: int, n2: int, n3: int, m: int,
          a: Pair, b: Pair, c: Pair, d: Pair) -> None:
    def calculate_characteristic(table: List[List[int]], 
                             expression: Callable[[int, int, List[List[int]]], int]) -> Fraction:
        nonlocal n1, n2
        value = Fraction()
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                try:
                    value += expression(i, j, table)
                except IndexError:
                    continue
        return value
    

    print("\n\n+" + "-"*9 + "+" + "\n| РЕШЕНИЕ |\n" + "+" + "-"*9 + "+\n")
    TABLE_FOR_PRINT = PrettyTable([f"{greek['nu']} / {greek['epsi']}"] + [i for i in range(m + 1)])

    table_with_return = [[] for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(m + 1):
            if i + j <= m:
                numerator:   int = factorial(m) * n1**i * n2**j * n3**(m - i - j)
                denominator: int = factorial(i) * factorial(j) * factorial(m - i -j) *\
                                sum([n1, n2, n3])**i * sum([n1, n2, n3])**j * sum([n1, n2, n3])**(m - i - j)
                table_with_return[i].append(Fraction(numerator=numerator, denominator=denominator))
            else:
                table_with_return[i].append(0)
        TABLE_FOR_PRINT.add_row([i] + table_with_return[i])

    print("С ВОЗВРАЩЕНИЕМ")
    print(TABLE_FOR_PRINT, "\n")
    TABLE_FOR_PRINT.clear_rows()

    table_without_return = [[] for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(m + 1):
            if i + j <= m and i <= n1 and j <= n2 and m - i - j <= n3:
                numerator:   int = int(C(n1, i) * C(n2, j) * C(n3, m - i - j))
                denominator: int = int(C(sum([n1 + n2 + n3]), m))
                table_without_return[i].append(Fraction(numerator=numerator, denominator=denominator))
            else:
                table_without_return[i].append(0)
        TABLE_FOR_PRINT.add_row([i] + table_without_return[i])

    print("БЕЗ ВОЗВРАЩЕНИЯ")
    print(TABLE_FOR_PRINT, "\n")
    TABLE_FOR_PRINT.clear()

    TABLE_FOR_PRINT.field_names = ["\\"] + [f"F({greek['epsi']} < {i[0]}, {greek['nu']} < {i[1]})" for i in [a, b, c, d]]

    tmp_row = []; tmp_row.append("с возвращением")
    for item in [a, b, c, d]:
        F = Fraction()
        for i in range(item[0]):
            for j in range(item[1]):
                try:
                    F += Fraction(table_with_return[i][j])
                except IndexError:
                    continue
        tmp_row.append(F)
    TABLE_FOR_PRINT.add_row(tmp_row)

    tmp_row.clear(); tmp_row.append("без возвращения")
    for item in [a, b, c, d]:
        F = Fraction()
        for i in range(item[0]):
            for j in range(item[1]):
                try:
                    F += Fraction(table_without_return[i][j])
                except IndexError:
                    continue
        tmp_row.append(F)
    TABLE_FOR_PRINT.add_row(tmp_row)

    print("ФУНКЦИИ РАСПРЕДЕЛЕНИЯ")
    print(TABLE_FOR_PRINT, "\n")
    TABLE_FOR_PRINT.clear();

    Pe = [[greek["epsi"]], [f"P({greek['epsi']})"]]
    for i in range(m + 1):
        try:
            Pe[1].append(Fraction(int(C(n1, i) * C(sum([n1, n2, n3]) - n1, m - i)), int(C(sum([n1, n2, n3]), m))))
            Pe[0].append(i)
        except ValueError:
            continue
    TABLE_FOR_PRINT.field_names = Pe[0];
    TABLE_FOR_PRINT.add_row(Pe[1])

    print("ЗАКОНЫ РАСПРЕДЕЛЕНИЯ КОМПОНЕНТ БЕЗ ВОЗВРАЩЕНИЯ")
    print(TABLE_FOR_PRINT, "\n")
    TABLE_FOR_PRINT.clear()

    Pn = [[greek["nu"]], [f"P({greek['nu']})"]]
    for i in range(m + 1):
        try:
            Pn[1].append(Fraction(int(C(n2, i) * C(sum([n1, n2, n3]) - n2, m - i)), int(C(sum([n1, n2, n3]), m))))
            Pn[0].append(i)
        except ValueError:
            continue

    TABLE_FOR_PRINT.field_names = Pn[0];
    TABLE_FOR_PRINT.add_row(Pn[1])
    print(TABLE_FOR_PRINT, "\n")

    print("ЧИСЛОВЫЕ ХАРАКТЕРИСТИКИ ВЕЛИЧИН ДЛЯ СЛУЧАЯ БЕЗ ВОЗВРАЩЕНИЯ")

    Me = calculate_characteristic(table=table_without_return, expression=lambda i, j, table: i * table[i][j])
    print(f"M{greek['epsi']} = {str(Me)}")

    Mn = calculate_characteristic(table=table_without_return, expression=lambda i, j, table: j * table[i][j])
    print(f"M{greek['nu']} = {str(Mn)}")

    De = calculate_characteristic(table=table_without_return, expression=lambda i, j, table: (i - Me)**2 * table[i][j])
    print(f"D{greek['epsi']} = {str(De)}")

    Dn = calculate_characteristic(table=table_without_return, expression=lambda i, j, table: (j - Mn)**2 * table[i][j])
    print(f"D{greek['nu']} = {str(Dn)}")

    Men = calculate_characteristic(table=table_without_return, expression=lambda i, j, table: i * j * table[i][j])
    print(f"M{greek['epsi']}{greek['nu']} = {str(Men)}")

    print(f"P{greek['epsi']}{greek['nu']} = {round((Men - Me * Mn) / sqrt(De * Dn), 6)}")
