def approx_point(x, y, c, dt, dx, future_field, present_field, past_field, force_field=0):
    coefficient = ((dt ** 2) * (c ** 2)) / (dx ** 2)
    future_field[x][y] = (coefficient * (present_field[x + 1][y] +
                                         present_field[x - 1][y] +
                                         present_field[x][y + 1] +
                                         present_field[x][y - 1] -
                                         4 * present_field[x][y]) +
                          (dt ** 2) * force_field[x][y] + 2 * present_field[x][y] - past_field[x][y])
    return future_field[x][y]


def approx_field(c, dt, dx, present_field, past_field, force_field=0):
    future_field = present_field
    for x in future_field[0]:
        for y in future_field[1]:
            future_field[x][y] = approx_point(x, y, c, dt, dx, future_field, present_field, past_field, force_field)
    return future_field
