import pytest
from week1_tooling import add, greet, parse_numbers, divide

@pytest.mark.parametrize(
"name, expected",
[
("Anirudha", "Hello, Anirudha"),
("", "Hello, there"),
(" ", "Hello, there"),
(" Asha ", "Hello, Asha"),
],
)

def test_greet(name: str, expected: str) -> None:
    assert greet(name) == expected

def test_add() -> None:
    assert add(2,3) == 5


@pytest.fixture
def messy_lines () -> list[str]:
    return ["10", "abc", "25.5", "", "7", "-3", "hello"]


def test_parse_numbers_skips_junk(messy_lines: list[str]) -> None:
    assert parse_numbers(messy_lines) == [10.0, 25.5, 7.0, -3.0]


def test_parse_numbers_all_junk() -> None:
    assert parse_numbers(["abc", "hello"]) == []

def test_parse_numbers_empty() -> None:
    assert parse_numbers([]) == []


@pytest.mark.parametrize("lines, expected", 
                         [(["1"], [1]),
                          ([" 7 "], [7]),
                          (["1e3"], [1000])],)

def test_parse_numbers_cases(lines: list[str], expected: list[float]) -> None:
    assert parse_numbers(lines) == expected

def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(1,0)
