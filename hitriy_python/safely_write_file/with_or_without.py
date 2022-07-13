import tempfile
import os


items = ["it's!", "Just!", "Great!", "somehow!"]


def write():
    with open('text.txt', 'w', encoding='utf-8') as f:
        for count, item in enumerate(items):
            if count == 2:
                raise Exception("Writing interupted!")
            f.write(f"{item}\n")


def read():
    with open('text.txt', 'r', encoding='utf-8') as f:
        print(f.read())


class atomic_open:

    def __init__(self, path, mode='w', encoding="utf-8"):
        self.path = path
        self.mode = mode if mode == 'wb' else 'w'
        self.encoding = encoding

    def __enter__(self):
        self.tempfile = tempfile.NamedTemporaryFile(
            self.mode,
            encoding=self.encoding,
            delete=False,
        )
        return self.tempfile

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.tempfile.close()
        if exc_type is None:
            os.rename(self.tempfile.name, self.path)
        else:
            os.unlink(self.tempfile.name)


def atomic_write():
    with atomic_open('text.txt', 'w', encoding='utf-8') as f:
        for count, item in enumerate(items):
            if count == 2:
                raise Exception("Writing interupted!")
            f.write(f"{item}\n")


if __name__ == '__main__':
    try:
        atomic_write()
    except:
        pass
    read()