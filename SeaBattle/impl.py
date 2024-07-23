def init_fields(fields_number, side):
    fields = []
    for field in range(side):
        pass
    return fields


def get_cell_symbol(value):
    print(value)

def draw_fields(fields):
    SPACE_FIELDS = 4  # Зазор между игровыми полями по горизонтали
    SPACE_CELLS = 2

def coord_utoa(vert, horiz):
    j = horiz - 1
    tmp = {'A':0, 'Б':1, 'В':2, 'Г':3, 'Д':4, 'Е':5, 'Ж':6, 'З':7, 'И':8, 'К':9 }
    i = tmp[vert]
    return (i, j)

def coord_atou(i, j):
    return ('AБВГДЕЖЗИК'[i], j + 1)

def add_ship(field: list, ship_len: int, head_coord: tuple, is_horizonal: bool) -> bool:
    return False
