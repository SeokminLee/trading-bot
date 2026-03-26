#!/usr/bin/env python3
"""
Simple entrypoint for trading-bot skeleton.
Usage:
  python main.py backtest --ticker AAPL
  python main.py mock --ticker AAPL
"""

import argparse

from backtest.run_backtest import run_backtest
from broker.mock_broker import run_mock

parser = argparse.ArgumentParser()
parser.add_argument("mode", choices=["backtest", "mock"])
parser.add_argument("--ticker", default="AAPL")
args = parser.parse_args()

if args.mode == "backtest":
    run_backtest(args.ticker)
elif args.mode == "mock":
    run_mock(args.ticker)
