import argparse

from bot.client import place_market_order

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--quantity", type=float, required=True)

args = parser.parse_args()

response = place_market_order(
    args.symbol,
    args.side,
    args.quantity
)

print(response)