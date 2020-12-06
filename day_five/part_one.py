def code_to_seat(line):
    """
    >>> code_to_seat("FBFBBFFRLR")
    357

    :param line:
    :return:
    """
    start = 0
    end = 127
    for char in line[:4]:
        if char == "F":
            end = end - round((end - start) / 2)
        if char == "B":
            start = start + round((end - start) / 2)
    for char in line[4:6]:
        if char == "F":
            end = end - round((end - start) / 2)
        if char == "B":
            start = start + round((end - start) / 2)
    row = start if line[6] == "F" else end

    seat_start = 0
    seat_end = 7
    for c in line[7:9]:
        if c == "L":
            seat_end = seat_end - round((seat_end - seat_start) / 2)
        if c == "R":
            seat_start = seat_start + round((seat_end - seat_start) / 2)
    seat = seat_start if line[9] == "L" else seat_end
    return row * 8 + seat


if __name__ == '__main__':
    with open("input.txt") as f:
        max_id = max(map(code_to_seat, f))

    print(max_id)
