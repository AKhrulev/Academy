from random import randint, choice

# коды содержимого ячеек
EMPTY = 0  # пустая ячейка
SHIP  = 1  # ячейка с кораблем
MISS  = 5  # удар мимо
HIT   = 6  # удар в корабль
NEAR  = 7  # окорестность корабля


def init_fields(fields_number, side):
    return [[[0 for j in range(side)] for i in range(side)] for k in range(fields_number)]


def draw_fields(fields):
    SPACE_FIELDS = 4  # Space between fields
    SPACE_CELLS = 2   # Space between cells in field
    SPACE_VERT_LEGEND = '  '  # Space equal to letters legend column

    upper_legend_row = ' '
    for k in range(len(fields)):
        for j in range(len(fields[0])):
            n = coord_atou(0, j)[1]
            upper_legend_row += f"{n:>2}" + ' ' * (SPACE_CELLS - 1)  # Values >9 are displayed correctly
        upper_legend_row += ' ' * SPACE_FIELDS + SPACE_VERT_LEGEND
    print(upper_legend_row)

    for i in range(len(fields[0])):
        for k in range(len(fields)):
            print(coord_atou(i, 0)[0], end=' ')
            for j in range(len(fields[0])):
                print(get_cell_symbol(fields[k][i][j]), end=' ' * SPACE_CELLS)
            print(' ' * SPACE_FIELDS, sep='', end='')
        print()


def get_cell_symbol(value):
    if value == EMPTY:
        symbol = '.'
    elif value == SHIP:
        symbol = '#'
    elif value == MISS:
        symbol = '~'
    elif value == HIT:
        symbol = 'X'
    elif value == NEAR:
        symbol = '-'
    else:
        symbol = '?'
    return symbol


def coord_utoa(vert, horiz):
    return ({'А':0, 'Б':1, 'В':2, 'Г':3, 'Д':4, 'Е':5, 'Ж':6, 'З':7, 'И':8, 'К':9 }[vert], horiz - 1)

def coord_atou(i, j):
    return ('AБВГДЕЖЗИКЛМНОПРСТ'[i], str(j + 1))


def is_on_field(field: list, i, j):
    """Проверяет, находится ли клетка с координатами i,j в пределах игрового поля"""
    return (0 <= i < len(field)) and (0 <= j < len(field))


def get_near_coords(i, j) -> list:
    """Возвращает список кортежей координат ячеек в окрестности заданной ячейки"""
    return [(i-1, j-1),(i, j-1),(i+1, j-1),(i, j-1),(i,j+1),(i-1, j+1),(i, j+1),(i+1, j+1)]


def add_ship(field: list, ship_len: int, head_coord: tuple, is_horizonal: bool) -> bool:
    if isinstance(head_coord[0], str):
        head_coord_a = coord_utoa(head_coord[0], head_coord[1])
    else:
        head_coord_a = head_coord

    ship_cells = []  # координаты ячеек корабля в виде кортежей (i,j)
    for m in range(ship_len):
        i = head_coord_a[0] + (m if not is_horizonal else 0)
        j = head_coord_a[1] + (m if is_horizonal else 0)
        if not is_on_field(field, i, j):
           return False
        ship_cells.append( (i, j) )

    # Заполняем окрестность каждой клетки корабля
    for i, j in ship_cells:
        near_coords = get_near_coords(i, j)
        for a, b in near_coords:
            if is_on_field(field, a, b):
                field[a][b] = NEAR

    # Добавляем ячейки корабля на поле
    for i, j in ship_cells:
        field[i][j] = SHIP

