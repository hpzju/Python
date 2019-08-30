from datetime import datetime


def stamper(fmt='%Y-%m-%d %H:%M:%S'):
    while True:
        yield datetime.strftime(datetime.now(), fmt)


stampit = stamper()


if __name__ == "__main__":
    print(stampit)
    for index, stamp in enumerate(stampit):
        print(f"{stamp}: {index}")
        if index > 100:
            break

