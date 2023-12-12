import os

def read(day, test=False):
    s = str(day).zfill(2)
    if test:
        s += "_test"
    f = open(f"data/{s}.txt", "r")
    lines = f.readlines()
    lines = [l[:-1] for l in lines]
    return lines

def get_input(day, test_nbr=0, part=1, year=2023):
    with open(f"data/keys.txt", "r") as f:
        keys = f.read().splitlines()
        AOC_COOKIE = keys[0]
    dday = str(day).zfill(2)
    s = f'curl --cookie "session={AOC_COOKIE}" https://adventofcode.com/{year}/day/{day}/input > data/{dday}.txt'
    os.system(s)
    
    s = f'curl --cookie "session={AOC_COOKIE}" https://adventofcode.com/{year}/day/{day}'
    if part==2:
        s += f'#part2'
    res = os.popen(s).read()
    res = res.split("<pre><code>")[test_nbr+1].split("</code></pre>")[0]
    with open(f'data/{dday}_test.txt', 'w') as f:
        f.write(res)

    f = open(f"data/{dday}.txt", "r")
    L = f.readlines()
    L = [l[:-1] for l in L]

    f = open(f"data/{dday}_test.txt", "r")
    Ltest = f.readlines()
    Ltest = [l[:-1] for l in Ltest]

    return L, Ltest
