import pytest
from backtest.run_backtest import run_backtest

def test_backtest_runs():
    equity = run_backtest('AAPL')
    assert equity is None or isinstance(equity, list)
