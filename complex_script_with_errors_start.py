# complex_script_with_errors.py

def calculate_total(price, quantity, tax_rate=0.08):
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

def apply_discount(total, discount_code):
    discount_codes = {
        'SUMMER10': 0.10,
        'WINTER20': 0.20,
        'SPRING15': 0.15
    }
    if discount_code not in discount_codes:
        raise ValueError("Invalid discount code")
    discount = discount_codes[discount_code]
    discounted_total = total - (total * discount)
    return discounted_total

def main():
    items = [
        {'price': 10, 'quantity': 3},
        {'price': 20, 'quantity': 5},
        {'price': 15, 'quantity': 2}
    ]

    total_cost = 0
    for item in items:
        total_cost += calculate_total(item['price'], item['quantity'])

    print("Total cost before discount:", total_cost)

    discount_code = 'SUMMER10'
    try:
        final_total = apply_discount(total_cost, discount_code)
    except ValueError as e:
        print("Error applying discount:", e)
        final_total = total_cost

    print("Final total after discount:", final_total)

if __name__ == "__main__":
    main()
