def func():
    minutes = 60
    seconds = 60
    hours = 24
    return seconds * minutes * hours


if __name__ == '__main__':
    import dis
    print(dis.dis(func))
