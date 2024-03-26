def find_intersection(x1, x2, y1, y2) -> str:
    points_x = set()
    points_y = set()

    if x1 < x2:
        step = 1
    elif x1 > x2:
        step = -1
    else:
        step = 0

    if step:
        for i in range(min((x1, x2)), max((x1, x2)) +1, step):
            points_x.add(i)
        for i in range(y1, y2 +1, step):
            points_y.add(i)
    else:
        points_x.add(x1)


    if points_x.intersection(points_y):
        return 'да'
    else:
        return 'нет'


print(find_intersection(1, 3, -1, 3))