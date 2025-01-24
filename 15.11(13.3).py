def creat(filename):
    with open(filename, 'w', encoding='utr-8') as f:
        for i in range(1, 10):
            f.write(str(i) * i + '\n')