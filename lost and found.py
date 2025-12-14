# ==============================
# DIGITAL LOST & FOUND SYSTEM
# ==============================

lost_items = []
found_items = []

def report_lost():
    print("\n--- Report Lost Item ---")
    item = input("Item name: ")
    place = input("Last seen location: ")
    date = input("Date (DD/MM/YYYY): ")

    lost_items.append({
        "item": item,
        "place": place,
        "date": date
    })

    print("✅ Lost item recorded successfully!")

def report_found():
    print("\n--- Report Found Item ---")
    item = input("Item name: ")
    place = input("Found at location: ")
    date = input("Date (DD/MM/YYYY): ")

    found_items.append({
        "item": item,
        "place": place,
        "date": date
    })

    print("✅ Found item recorded successfully!")

def view_lost():
    print("\n--- Lost Items ---")
    if not lost_items:
        print("No lost items reported.")
    else:
        for i, item in enumerate(lost_items, 1):
            print(f"{i}. {item['item']} | {item['place']} | {item['date']}")

def view_found():
    print("\n--- Found Items ---")
    if not found_items:
        print("No found items reported.")
    else:
        for i, item in enumerate(found_items, 1):
            print(f"{i}. {item['item']} | {item['place']} | {item['date']}")

def match_items():
    print("\n--- Possible Matches ---")
    match_found = False

    for lost in lost_items:
        for found in found_items:
            if lost["item"].lower() == found["item"].lower():
                print(f"🔔 Match Found: {lost['item']}")
                print(f"   Lost at: {lost['place']} | Found at: {found['place']}")
                match_found = True

    if not match_found:
        print("No matches found yet.")

# ==============================
# MAIN MENU
# ==============================

while True:
    print("\n===== DIGITAL LOST & FOUND SYSTEM =====")
    print("1. Report Lost Item")
    print("2. Report Found Item")
    print("3. View Lost Items")
    print("4. View Found Items")
    print("5. Match Lost & Found")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        report_lost()
    elif choice == "2":
        report_found()
    elif choice == "3":
        view_lost()
    elif choice == "4":
        view_found()
    elif choice == "5":
        match_items()
    elif choice == "6":
        print("👋 Exiting system. Stay safe!")
        break
    else:
        print("❌ Invalid choice. Try again.")
