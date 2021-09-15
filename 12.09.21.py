def generate_list(num, minimum, maximum):
    i = 0
    while i < num:
        yield random.randrange(minimum, maximum)
        i += 1