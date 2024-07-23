from impl import *

N = 3  # размер стороны игрового поля
fields = init_fields(2, N)
draw_fields(fields)

# Добавляем корабль
is_success = add_ship(fields[0], 2, ('А',2), False)
if is_success:
    print('Корабль добавлен')

draw_fields(fields)

#     1 2 3    1 2 3
#   А . . .  А . . .
#   Б . . .  Б . . .
#   В . . .  В . . .




