def get_product_data(sheet):
    worksheet = sheet.sheet1
    data = worksheet.get_all_records()
    products = {}
    for row in data:
        sku = row.get("SKU") or row.get("sku") or row.get("Sku")
        price = row.get("Price") or row.get("price") or 0
        description = row.get("Description") or row.get("description") or ""
        if sku:
            products[sku] = {
                "price": float(price),
                "description": description
            }
    return products

def get_customer_data(sheet):
    worksheet = sheet.sheet1
    data = worksheet.get_all_records()
    customers = {}
    for row in data:
        name = row.get("Customer") or row.get("Name") or row.get("customer") or row.get("name")
        if name:
            customers[name] = row
    return customers
