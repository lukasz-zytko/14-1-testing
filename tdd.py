import pytest

def get_fibonacci_number(n):
    fibonacci = []
    for i in range(0,n+1):
        if i == 0:
            fibonacci.append(0)
        elif i == 1 or i == 2:
            fibonacci.append(1)
        elif i > 2:
            fibonacci.append(sum(fibonacci[-2:]))
    return fibonacci[-1]


@pytest.mark.parametrize('n, result', (
   (0, 0),
   (1, 1),
   (2, 1),
   (3, 2),
   (10, 55),
   (15, 610)
))
def test_fibonacci(n, result):
   assert get_fibonacci_number(n) == result
