from impl import *

N = 7  # размер стороны игрового поля
fields = init_fields(2, N)
# draw_fields(fields)

# Добавляем корабль
is_success = add_ship(fields[0], 2, ('А',2), True)
if is_success:
    print('Корабль добавлен')

draw_fields(fields)

exit()
