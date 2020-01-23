import math
from scanner import Scanner

class Store:
    def __init__(self, items):
        self.items = items
    
    def print_receipt(self):
        output = ''
        total_tax = 0
        total = 0
        for item in self.items:
            item_total, item_tax = self.calculate_item_tax(item)
            total_tax += item_tax
            total += item_total
            output += f'{item["quantity"]} {item["item"]}: {item_total:.2f}\n'
        
        output += f'Sales Taxes: {total_tax:.2f}\n'
        output += f'Total: {total:.2f}'

        return output

    def calculate_item_tax(self, item):
        item_subtotal_cents = round(float(item['price']) * 100, 0)

        tax_rate = 0
        if "book" in item['item'] or "pills" in item['item'] or "chocolate" in item['item']:
            tax_rate = 0
        else:
            tax_rate = 0.10
        
        if "imported" in item['item']:
            tax_rate += 0.05

        # round up to nearest 0.05, but with cents
        tax = math.ceil(item_subtotal_cents * tax_rate / 5) * 5
        item_total = item_subtotal_cents + tax 

        return item_total / 100, tax / 100