def func():
    return 60 * 60 * 24


if __name__ == '__main__':
    import dis
    print(dis.dis(func))
