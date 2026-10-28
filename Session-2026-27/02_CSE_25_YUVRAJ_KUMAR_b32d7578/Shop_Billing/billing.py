from datetime import datetime
customer_name = input("Enter Customer Name: ")
if customer_name == "":
    customer_name = "Valued Customer"
customer_phone = input("Enter Customer Phone Number: ")
if customer_phone == "":
    customer_phone = "N/A"
bill_details = []
grand_total = 0
n=1
print(f"|{'~'*46}|\n|for exit, double press Enter{' '*18}|\n|for re-entering, type 're' in item price field|\n|{'~'*46}|")
while 1:
    print(f"\nEnter details for item {n}:")
    item_name = input("Enter Item Name: ")
    if item_name == "":
        cnfm = input("exit?(y/n): ")
        if cnfm == "" or cnfm.lower() == "y":
            break
        else:
            continue
    item_price = (input("Enter Item Price (₹): "))
    if item_price.lower() == "re":
      
        continue
    else:
        item_price = float(item_price)
    item_qty = int(input("Enter Quantity: "))

    total_item_price = item_price * item_qty
    grand_total += total_item_price

    bill_details.append({
    "name": item_name,
    "price": item_price,
    "qty": item_qty,
    "total": total_item_price
    })
    n+=1
print("\n")
now = datetime.now()
current_date = now.strftime("%d-%m-%Y")
current_time = now.strftime("%I:%M %p")
def br(char):
    print(f"|{char*69}|")
br("=")
print(f"|Date: {current_date:<46} Time: {current_time:<10}|")
br("=")
print(f"|" + " "*31 + "INVOICE" + " "*31 + "|")
br("-")
print(f"|Customer Name: {customer_name:<22} Customer Phone no.: {customer_phone:<11}|")
br("-")
print(f"|{'Item':<32} {'Price':<15} {'Qty':<10} {'Total(₹)':<9}|")
br("-")
for item in bill_details:
    print(f"|{item['name']:<32} {item['price']:<16.2f} {item['qty']:<9} {item['total']:<9.2f}|")
    
br("-")
print(f"|Grand Total: ₹{grand_total:<55.2f}|")
br("-")
print("|" + " "*23 + "Thank you for shopping!" + " "*23 + "|")
br("=")