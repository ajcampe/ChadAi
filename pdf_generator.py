from fpdf import FPDF

def generate_quote_pdf(customer_info, item, qty, unit_price, tax, total):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Chuck Quote", ln=True, align='C')
    pdf.ln(10)

    pdf.cell(100, 10, txt=f"Customer: {customer_info.get('Account Name')}", ln=True)
    pdf.cell(100, 10, txt=f"Address: {customer_info.get('Address')}", ln=True)
    pdf.ln(10)

    pdf.cell(100, 10, txt=f"Item: {item}", ln=True)
    pdf.cell(100, 10, txt=f"Quantity: {qty}", ln=True)
    pdf.cell(100, 10, txt=f"Unit Price: ${unit_price:.2f}", ln=True)
    pdf.cell(100, 10, txt=f"Tax: ${tax:.2f}", ln=True)
    pdf.cell(100, 10, txt=f"Total: ${total:.2f}", ln=True)

    pdf_path = "/tmp/quote.pdf"
    pdf.output(pdf_path)
    return pdf_path
