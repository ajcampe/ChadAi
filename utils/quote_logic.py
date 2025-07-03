from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def extract_quote_items(items_data, products):
    quote_items = []
    for item in items_data:
        sku = item.get("sku")
        quantity = item.get("quantity", 1)
        if sku in products:
            product = products[sku]
            quote_items.append({
                "sku": sku,
                "description": product.get("description", ""),
                "unit_price": product.get("price", 0),
                "quantity": quantity,
                "total_price": quantity * product.get("price", 0),
            })
    return quote_items

def generate_quote_pdf(customer, items, filename="quote.pdf"):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Header
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, height - 50, "Quote")

    # Customer info
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, f"Customer: {customer.get('name', 'Unknown')}")

    # Table headers
    c.drawString(50, height - 110, "SKU")
    c.drawString(150, height - 110, "Description")
    c.drawString(350, height - 110, "Quantity")
    c.drawString(420, height - 110, "Unit Price")
    c.drawString(500, height - 110, "Total")

    y = height - 130
    total_amount = 0
    for item in items:
        c.drawString(50, y, item["sku"])
        c.drawString(150, y, item["description"])
        c.drawString(350, y, str(item["quantity"]))
        c.drawString(420, y, f"${item['unit_price']:.2f}")
        c.drawString(500, y, f"${item['total_price']:.2f}")
        total_amount += item["total_price"]
        y -= 20

    # Total
    c.drawString(420, y - 10, "Total Amount:")
    c.drawString(500, y - 10, f"${total_amount:.2f}")

    c.showPage()
    c.save()

    pdf = buffer.getvalue()
    buffer.close()
    return pdf

def update_quote():
    # Placeholder for future logic if needed
    pass
