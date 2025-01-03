#sample script with logical error


def calculate_total(price, tax_rate):
    total = price + price * tax_rate
    return total

def main():
    price = 80
    tax_rate = 0.01
    total = calculate_total(price, tax_rate)
    print(f"The total price is: {total}")

if __name__ == "__main__":
    main()
