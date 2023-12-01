def read(day, test=False):
    s = str(day).zfill(2)
    if test:
        s += "_test"
    f = open(f"data/{s}.txt", "r")
    lines = f.readlines()
    lines = [l[:-1] for l in lines]
    return lines