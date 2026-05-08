
def validate_order(side,order_type,quantity,price):

    valid_side = ["BUY", "SELL"]

    valid_types = ["MARKET", "LIMIT "]

    if side not in valid_side:
        raise ValueError("Side must be buy or sell")
    
    if order_type not in valid_types:
        raise ValueError("Order must be Market or Limit")
    
    if quantity<=0:
        raise ValueError("Quantity must be greater than 0")
    
    if order_type == "LIMIT" and price is None:
        raise ValueError("Limit order requires a price")