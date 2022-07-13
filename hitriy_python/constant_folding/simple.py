
def func():
    return 86400


if __name__ == '__main__':
    import dis
    print(dis.dis(func))