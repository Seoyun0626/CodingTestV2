# 낚시왕 문제

def get_next_loc(y, x, speed, dir):
    if dir == UP or dir == DOWN: # y
        cycle = R * 2 - 2
        if dir == UP:
            speed += 2 * (R - 1) - y
        else:
            speed += 1

        speed %= cycle
        if speed > R:
            return (2 * R - 2 - speed, x, UP)
        return (speed, x, DONW)
    else:
        cycle = C * 2 - 2
        if dir == LEFT:
            speed += 2 * (C - 1) - x
        else:
            speed += x

        speed %= cycle
        if speed >= C:
            return (y, 2 * C - 2 - speed, LEFT)
        return (y, speed, RIGHT)
