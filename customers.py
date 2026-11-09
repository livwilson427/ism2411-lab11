# Reflection 1:
# I would use .get() when a field might be missing, such as an optional phone number or email.
# I would use bracket notation when I know the key exists and need its value. My rule is to use .get()
# for optional information and brackets for required information.

# Reflection 2:
# Exercise 8 reminds me of using SUMIF or a PivotTable in Excel to total sales by category or region.
# Python can be more useful for large datasets because a loop can process many records automatically,
# and the code can be reused or changed without manually updating spreadsheet formulas.


# EXERCISE 1: One customer
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400.00
}

print("EXERCISE 1: One customer")
print("Name:", customer["name"])
print("Email:", customer["email"])
print("Tier:", customer["tier"])
print("YTD spend:", customer["ytd_spend"])
print("Full customer dictionary:", customer)


# EXERCISE 2: Update and add
print("\nEXERCISE 2: Update and add")

customer["phone"] = "555-123-4567"
print("After adding phone:", customer)

customer["tier"] = "platinum"
print("After updating tier:", customer)

del customer["email"]
print("After deleting email:", customer)


# EXERCISE 3: Safe lookup
print("\nEXERCISE 3: Safe lookup")

email = customer.get("email", "no email on file")
print("Safe email lookup:", email)

try:
    print(customer["email"])
except KeyError:
    print('Bracket lookup caused a KeyError because "email" is not in the dictionary.')


# EXERCISE 4: Iterate
print("\nEXERCISE 4: Iterate")

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), looping through a dictionary gives only its keys.
# You can then use customer[key] to get each value.


# EXERCISE 5: Lookup table
print("\nEXERCISE 5: Lookup table")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

discount_rate = tier_discounts.get(customer["tier"], 0)
purchase_price = 200
discount_amount = purchase_price * discount_rate
final_price = purchase_price - discount_amount

print("Tier:", customer["tier"])
print(f"Discount rate: {discount_rate * 100:.0f}%")
print(f"Final price for a $200 purchase: ${final_price:.2f}")


# EXERCISE 6: List of dictionaries
print("\nEXERCISE 6: List of dictionaries")

customers = [
    customer,
    {"name": "Bob", "email": "bob@example.com", "tier": "silver", "ytd_spend": 3200.00},
    {"name": "Carol", "email": "carol@example.com", "tier": "gold", "ytd_spend": 8500.00}
]

purchase_amount = 300

for person in customers:
    rate = tier_discounts.get(person["tier"], 0)
    discount = purchase_amount * rate
    print(
        f"{person['name']} ({person['tier']}): "
        f"{rate * 100:.0f}% discount = ${discount:.2f} off a $300 purchase"
    )


# EXERCISE 7: Nested catalog
print("\nEXERCISE 7: Nested catalog")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product_name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product_name} — only {details['stock']} left")


# EXERCISE 8: Sales by region
print("\nEXERCISE 8: Sales by region")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_by_region = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")