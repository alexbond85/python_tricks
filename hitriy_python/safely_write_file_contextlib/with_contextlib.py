import os
from tempfile import NamedTemporaryFile
from contextlib import contextmanager

items = ["it's!", "Just!", "Great!", "somehow!"]


def read():
    with open('text.txt', 'r', encoding='utf-8') as f:
        print(f.read())


@contextmanager
def atomic_writes(path, mode="w", encoding="utf-8"):
    mode = mode if mode == "wb" else "w"
    temp_file = NamedTemporaryFile(mode, encoding=encoding, delete=False)
    try:
        yield temp_file
    except Exception as e:
        temp_file.close()
        os.unlink(temp_file.name)
        print(f"Exception {e}")
    else:
        temp_file.close()
        try:
            os.rename(temp_file.name, path)
        except OSError as e:
            os.unlink(temp_file.name)
            print(f"Exception {e}")


def atomic_write():
    with atomic_writes('text.txt', 'w', encoding='utf-8') as f:
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
