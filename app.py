import streamlit as st
from google_api import get_customer_info, get_product_price
from pdf_generator import generate_quote_pdf

st.set_page_config(page_title="Chuck QuoteBot", layout="wide")
st.title("🤖 Chuck – Your Quote Generator")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("What quote do you need today?")
if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Example logic – replace with NLP or parsing
    customer_name = "Port Crossing"
    item = "refrigerator"
    quantity = 2

    customer_info = get_customer_info(customer_name)
    unit_price = get_product_price(item)
    subtotal = unit_price * quantity
    tax = subtotal * 0.07
    total = subtotal + tax

    pdf_path = generate_quote_pdf(customer_info, item, quantity, unit_price, tax, total)

    response = f"Here's your quote for {quantity} {item}(s):\n\nSubtotal: ${subtotal:.2f}\nTax: ${tax:.2f}\nTotal: ${total:.2f}"
    st.chat_message("assistant").write(response)
    st.download_button("📄 Download Quote PDF", data=open(pdf_path, "rb"), file_name="quote.pdf")
    st.session_state.messages.append({"role": "assistant", "content": response})
