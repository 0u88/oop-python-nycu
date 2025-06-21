import pytest
import lec4
def test_is_even_with_return(capfd):
    result = lec4.is_even_with_return(4)
    out, _ = capfd.readouterr()
    assert "with return" in out
    assert result is True

    result = lec4.is_even_with_return(3)
    out, _ = capfd.readouterr()
    assert result is False

def test_is_even_without_return(capfd):
    result = lec4.is_even_without_return(4)
    out, _ = capfd.readouterr()
    assert "without return" in out
    assert result is None

def test_bisection_cuberoot_approx():
    result = lec4.bisection_cuberoot_approx(8, 0.01)
    assert result == pytest.approx(2.0, rel=1e-2)

    result = lec4.bisection_cuberoot_approx(27, 0.001)
    assert result == pytest.approx(3.0, rel=1e-3)

def test_add_returning_function():
    f = lec4.add_returning_function()
    assert callable(f)
    assert f(3, 4) == 7
    assert f(0, 0) == 0

def test_f_scope(capfd):
    result = lec4.f_scope(3)
    out, _ = capfd.readouterr()
    assert "in f(x): x = 4" in out
    assert result == 4

def test_g_scope(capfd):
    result = lec4.g_scope(3)
    out, _ = capfd.readouterr()
    assert "in g(x): x = 4" in out
    assert "in h(x): x = 5" in out
    assert result == 4

