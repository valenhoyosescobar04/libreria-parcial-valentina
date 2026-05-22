import pytest
from src.solution import Solution

# Estas deben PASAR
def test_add_valid_value():
    s = Solution()
    s.add(10)

def test_total_with_values():
    s = Solution()
    s.add(3)
    s.add(7)
    assert s.total() == 10

def test_total_with_no_values():
    s = Solution()
    assert s.total() == 0

# Estas deben FALLAR
def test_add_negative_value():
    s = Solution()
    with pytest.raises(ValueError):
        s.add(-1)

def test_wrong_total():
    s = Solution()
    s.add(5)
    assert s.total() == 99  # Este falla a propósito