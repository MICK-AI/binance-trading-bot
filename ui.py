import streamlit as st

from bot.client import (
    place_market_order,
    place_limit_order
)


st.title("Binance Trading Bot")


symbol = st.text_input("Symbol")


side = st.selectbox(
    "Side",
    ["BUY", "SELL"]
)


order_type = st.selectbox(
    "Order Type",
    ["MARKET", "LIMIT"]
)


quantity = st.number_input(
    "Quantity",
    min_value=0.001,
    value=0.001,
    step=0.001,
    format="%.3f"
)


price = None

if order_type == "LIMIT":

    price = st.number_input(
        "Price",
        min_value=1.0
    )


if st.button("Place Order"):

    if order_type == "MARKET":

        response = place_market_order(
            symbol,
            side,
            quantity
        )

    else:

        response = place_limit_order(
            symbol,
            side,
            quantity,
            price
        )



    if "orderId" in response:

        st.success("Order Placed Successfully!")

        st.write(f"Order ID: {response['orderId']}")
        st.write(f"Symbol: {response['symbol']}")
        st.write(f"Side: {response['side']}")
        st.write(f"Order Type: {response['type']}")
        st.write(f"Status: {response['status']}")
        st.write(f"Quantity: {response['origQty']}")

        if response["type"] == "LIMIT":

            st.write(f"Price: {response['price']}")

    else:

        st.error("Order Failed!")