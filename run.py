with open("poem.txt") as fh:
    data = fh.read()
    print(data[::-1])
