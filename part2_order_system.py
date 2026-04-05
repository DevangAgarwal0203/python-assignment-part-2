import copy

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}


# Task 1

print("Task 1 - Menu Explorer")

categories = []
for item in menu.values():
    if item["category"] not in categories:
        categories.append(item["category"])

for cat in categories:
    print(f"\n===== {cat} =====")
    for item_name, info in menu.items():
        if info["category"] == cat:
            status = "[Available]" if info["available"] else "[Unavailable]"
            print(f"  {item_name:<16} ₹{info['price']:.2f}   {status}")

total_items = len(menu)
available_items = sum(1 for v in menu.values() if v["available"])

most_exp_name = ""
most_exp_price = 0
for name, info in menu.items():
    if info["price"] > most_exp_price:
        most_exp_price = info["price"]
        most_exp_name = name

print(f"\nTotal items    : {total_items}")
print(f"Available      : {available_items}")
print(f"Most expensive : {most_exp_name} (₹{most_exp_price:.2f})")
print("\nItems under ₹150:")
for name, info in menu.items():
    if info["price"] < 150:
        print(f"  {name} — ₹{info['price']:.2f}")


# Task 2

print("\nTask 2 - Cart Operations")

cart = []

def add_item(item_name, qty):
    if item_name not in menu:
        print(f"  ✗ '{item_name}' does not exist in the menu.")
        return
    if not menu[item_name]["available"]:
        print(f"  ✗ '{item_name}' is currently unavailable.")
        return
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] += qty
            print(f"  ↑ Updated '{item_name}' quantity to {entry['quantity']}.")
            return
    cart.append({"item": item_name, "quantity": qty, "price": menu[item_name]["price"]})
    print(f"  ✓ Added '{item_name}' × {qty}.")

def remove_item(item_name):
    for entry in cart:
        if entry["item"] == item_name:
            cart.remove(entry)
            print(f"  ✓ Removed '{item_name}' from cart.")
            return
    print(f"  ✗ '{item_name}' is not in the cart.")

def print_cart(label="Cart"):
    print(f"\n  [{label}]")
    if not cart:
        print("   (empty)")
    for entry in cart:
        print(f"   {entry['item']:<18} x{entry['quantity']}  ₹{entry['price'] * entry['quantity']:.2f}")

print()
add_item("Paneer Tikka", 2)
print_cart("After adding Paneer Tikka x2")

add_item("Gulab Jamun", 1)
print_cart("After adding Gulab Jamun x1")

add_item("Paneer Tikka", 1)
print_cart("After adding Paneer Tikka x1 again")

add_item("Mystery Burger", 1)
add_item("Chicken Wings", 1)
print_cart("After failed additions")

remove_item("Gulab Jamun")
print_cart("After removing Gulab Jamun")

subtotal = sum(e["price"] * e["quantity"] for e in cart)
gst = round(subtotal * 0.05, 2)
total = round(subtotal + gst, 2)

print("\n========== Order Summary ==========")
for e in cart:
    print(f"  {e['item']:<18} x{e['quantity']}   ₹{e['price'] * e['quantity']:.2f}")
print("------------------------------------")
print(f"  {'Subtotal:':<26} ₹{subtotal:.2f}")
print(f"  {'GST (5%):':<26} ₹{gst:.2f}")
print(f"  {'Total Payable:':<26} ₹{total:.2f}")
print("====================================")


# Task 3

print("\nTask 3 - Inventory Tracker")

inventory_backup = copy.deepcopy(inventory)

print("\n[Proof of deep copy]")
inventory["Garlic Naan"]["stock"] = 999
print(f"  inventory['Garlic Naan']['stock']        = {inventory['Garlic Naan']['stock']}")
print(f"  inventory_backup['Garlic Naan']['stock'] = {inventory_backup['Garlic Naan']['stock']}")
inventory["Garlic Naan"]["stock"] = 30
print(f"  Restored to 30")

print("\n[Order fulfilment]")
for entry in cart:
    item = entry["item"]
    needed = entry["quantity"]
    available_stock = inventory[item]["stock"]
    if available_stock < needed:
        print(f"  Not enough stock for '{item}'. Deducting {available_stock}.")
        inventory[item]["stock"] = 0
    else:
        inventory[item]["stock"] -= needed
        print(f"  Deducted {needed} from '{item}'. Remaining: {inventory[item]['stock']}")

print("\n[Reorder Alerts]")
for item, data in inventory.items():
    if data["stock"] <= data["reorder_level"]:
        print(f"  ⚠ Reorder Alert: {item} — Only {data['stock']} unit(s) left (reorder level: {data['reorder_level']})")

print("\n[inventory vs inventory_backup]")
print(f"  {'Item':<18} Current   Backup")
for item in inventory:
    cur = inventory[item]["stock"]
    bak = inventory_backup[item]["stock"]
    diff = " <- changed" if cur != bak else ""
    print(f"  {item:<18} {cur:<9} {bak}{diff}")


# Task 4

print("\nTask 4 - Sales Log Analysis")

def revenue_per_day(log):
    rev = {}
    for date, orders in log.items():
        rev[date] = sum(o["total"] for o in orders)
    return rev

def best_day(rev_dict):
    best = max(rev_dict, key=rev_dict.get)
    return best, rev_dict[best]

rev = revenue_per_day(sales_log)
print("\nRevenue per day:")
for date, amount in rev.items():
    print(f"  {date} : ₹{amount:.2f}")

best_date, best_rev = best_day(rev)
print(f"\nBest-selling day : {best_date} (₹{best_rev:.2f})")

item_counts = {}
for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            item_counts[item] = item_counts.get(item, 0) + 1

most_ordered = max(item_counts, key=item_counts.get)
print(f"\nMost ordered item : {most_ordered} ({item_counts[most_ordered]} orders)")

sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

rev = revenue_per_day(sales_log)
print("\n[Updated] Revenue per day:")
for date, amount in rev.items():
    print(f"  {date} : ₹{amount:.2f}")

best_date, best_rev = best_day(rev)
print(f"\n[Updated] Best-selling day : {best_date} (₹{best_rev:.2f})")

print("\nAll Orders:")
all_orders = []
for date, orders in sales_log.items():
    for order in orders:
        all_orders.append((date, order))

for idx, (date, order) in enumerate(all_orders, start=1):
    items_str = ", ".join(order["items"])
    print(f"  {idx}. [{date}] Order #{order['order_id']}  — ₹{order['total']:.2f} — Items: {items_str}")
