import streamlit as st
from google_api import get_customer_info, get_product_price
from pdf_generator import generate_quote_pdf

st.set_page_config(page_title="Chuck QuoteBot", layout="wide")
st.title("🤖 Chuck – Your Quote Generator")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Get user input from chat box
user_input = st.chat_input("What quote do you need today?")
if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Example placeholder logic for quoting - replace with real NLP or parsing
    customer_name = "Port Crossing"
    item = "refrigerator"
    quantity = 2

    # Fetch data and calculate pricing
    customer_info = get_customer_info(customer_name)
    unit_price = get_product_price(item)
    subtotal = unit_price * quantity
    tax = subtotal * 0.07
    total = subtotal + tax

    # Generate PDF quote (function should return path or bytes)
    pdf_path = generate_quote_pdf(customer_info, item, quantity, unit_price, tax, total)

    # Optional: show confirmation or link to download PDF
    st.success(f"Quote generated for {customer_name}: {quantity} x {item} at ${unit_price} each. Total: ${total:.2f}")

