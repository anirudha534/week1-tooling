import time


def make_toast() -> None:
    print("toast started")
    time.sleep(2)
    print("toast done")


def boil_egg() -> None:
    print("egg started")
    time.sleep(2)
    print("egg done")


start = time.perf_counter()
make_toast()
boil_egg()
print(f"took {time.perf_counter() - start:.1f} seconds")