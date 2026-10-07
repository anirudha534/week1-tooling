def add(a: int, b: int) -> int:
    return a + b


def greet(name: str, greeting: str = "Hello") -> str:
    """Return a greeting, falling back to 'there' for a blank name."""
    name = name.strip()
    if not name:
        name = "there"
    return f"{greeting}, {name}"

def parse_numbers(lines: list[str]) -> list[float]:
    """Convert lines to floats, skipping any that are not valid numbers."""
    numbers: list[float] = []
    for line in lines:
        try:
            numbers.append(float(line))
        except ValueError:
            continue
    return numbers

def main() -> None:
    print("Hello from week1-tooling!")
    print(add(2, 3))
