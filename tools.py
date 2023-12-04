import os

def read(day, test=False):
    s = str(day).zfill(2)
    if test:
        s += "_test"
    f = open(f"data/{s}.txt", "r")
    lines = f.readlines()
    lines = [l[:-1] for l in lines]
    return lines

def get_input(day, test=False, year=2023):
    with open(f"data/keys.txt", "r") as f:
        keys = f.read().splitlines()
        AOC_COOKIE = keys[0]
    dday = str(day).zfill(2)
    s = f'curl --cookie "session={AOC_COOKIE}" https://adventofcode.com/{year}/day/{day}/input > data/{dday}.txt'
    os.system(s)
    
    s = f'curl https://adventofcode.com/{year}/day/{day}'
    res = os.popen(s).read()
    res = res.split("<pre><code>")[1].split("</code></pre>")[0]
    with open(f'data/{dday}_test.txt', 'w') as f:
        f.write(res)

    name = dday
    if test:
        name += "_test"
    f = open(f"data/{dday}.txt", "r")
    lines = f.readlines()
    lines = [l[:-1] for l in lines]
    return lines
