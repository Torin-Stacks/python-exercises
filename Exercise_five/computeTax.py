def compute_tax(status, taxable_income):

    tax = 0
    tax_rate = 0
    if status.lower() == "single":
        tax_rate = 0.17376
        tax = taxable_income * tax_rate

    elif status.lower() == "married joint":
        tax_rate = 0.1333
        tax = taxable_income * tax_rate

    elif status.lower() == "married separate":
        tax_rate = 0.17376
        tax = taxable_income * tax_rate

    elif status.lower() == "head of a house":
        tax_rate = 0.14704
        tax = taxable_income * tax_rate

    print(f"With your {status} status, your tax payable = {tax}")

compute_tax("Head of a house", 50000)