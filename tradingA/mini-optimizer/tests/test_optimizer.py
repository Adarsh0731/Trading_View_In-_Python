import pytest
from optimizer import run_optimizer

def test_run_optimizer():
    result = run_optimizer([1, 2, 3])
    assert "mean" in result
    assert "std_dev" in result
    assert isinstance(result["optimized"], list)
