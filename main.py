# Ein einfaches Konsolen-Kassenprogramm in Python ohne Verwendung von Bibliotheken

# Ein Wörterbuch, um die Speisekartenartikel und ihre Preise zu speichern
menu = {
    "Heißgetränke": {
        "Kaffee": 3000,
        "Tee": 2000,
        "Heiße Schokolade": 4000,
        "Cappuccino": 5000
    },
    "Kuchen": {
        "Schokoladenkuchen": 8000,
        "Vanillekuchen": 7000,
        "Heidelbeerkuchen": 9000,
        "Orangenkuchen": 7500
    }
}

# Ein Wörterbuch, um die Bestellungen für jeden Tisch zu speichern
orders = {}

# Funktion zum Anzeigen der Speisekartenartikel und ihrer Preise
def display_menu():
    print("Liste und Preise der Produkte:")
    for category, items in menu.items():
        print(f"{category}:")
        for index, (item, price) in enumerate(items.items(), start=1):
            print(f"   {index}. {item}: {price} Toman")
        print()

# Funktion zum Anzeigen der Artikel für eine bestimmte Tischnummer
def display_items_for_table(table):
    if table in orders:
        print(f"Bestellungen für Tisch {table}:")
        for index, (category, item) in enumerate(orders[table], start=1):
            print(f"{index}. {item} aus der Kategorie {category}")
    else:
        print(f"Die Tischnummer {table} existiert nicht.")

# Funktion zum Löschen eines Artikels für eine bestimmte Tischnummer
def delete_item_for_table(table):
    display_items_for_table(table)
    if table in orders:
        try:
            item_index = int(input("Geben Sie die Nummer des zu löschenden Artikels ein: ")) - 1
            if 0 <= item_index < len(orders[table]):
                deleted_item = orders[table].pop(item_index)
                print(f"Der Artikel {deleted_item[1]} aus der Kategorie {deleted_item[0]} wurde gelöscht.")
            else:
                print("Ungültige Artikelnummer.")
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Nummer ein.")
    else:
        print(f"Die Tischnummer {table} existiert nicht.")

# Funktion zum Anzeigen der Optionen für den Tischwechsel
def display_table_change_options():
    print("Optionen für Tischwechsel:")
    print("1. Tisch wechseln")
    print("2. Name des Tisches ändern")
    print("3. Tisch löschen")
    print("4. Zurück zur Startseite")

# Funktion zum Anzeigen der Optionen für den Kunden
def display_start_options():
    print("Startseite:")
    print("1. Produkt bestellen")
    print("2. Rechnung anzeigen")
    print("3. Tisch wechseln")
    print("4. Bestellung löschen oder bearbeiten")
    print("5. Gesamte Rechnungen anzeigen")
    print("6. Programm verlassen")

# Funktion zum Anzeigen der Artikel für alle Tische
def display_all_items():
    print("Übersicht aller Tische und ihrer Bestellungen:")
    for table, items in orders.items():
        print(f"Tisch {table}:")
        for index, (category, item) in enumerate(items, start=1):
            print(f"   {index}. {item} aus der Kategorie {category}")
        print()

# Funktion zum Ändern des Tisches (Tisch wechseln oder löschen)
def change_table_options():
    display_table_change_options()
    option = input("Geben Sie Ihre Option für den Tischwechsel ein: ")

    if option == "1":
        change_table()
    elif option == "2":
        change_table_name()
    elif option == "3":
        delete_table()
    elif option == "4":
        return_to_start()
    else:
        print("Ungültige Option für den Tischwechsel.")

# Funktion zum Berechnen der Rechnung für einen Tisch
def calculate_bill():
    print("Übersicht aller offenen Tische:")
    for table, items in orders.items():
        total_bill = sum(menu[category][item] for category, item in items)
        print(f"Tisch {table}: Gesamtbetrag: {total_bill} Toman")

    table = input("Geben Sie die Tischnummer ein, für die Sie die detaillierte Rechnung anzeigen möchten ('0' zum Beenden): ")
    if table == '0':
        return

    if table in orders:
        print(f"Detaillierte Rechnung für Tisch {table}:")
        print("{:<20} {:<20} {:<20}".format("Kategorie", "Artikel", "Preis (Toman)"))
        for category, item in orders[table]:
            price = menu[category][item]
            print("{:<20} {:<20} {:<20}".format(category, item, price))
        total_bill = sum(menu[category][item] for category, item in orders[table])
        print(f"Gesamtbetrag: {total_bill} Toman")
    else:
        print(f"Die Tischnummer {table} existiert nicht.")

# Funktion zum Wechseln des Tisches
def change_table():
    global orders
    current_table = input("Geben Sie die aktuelle Tischnummer ein: ")
    new_table = input("Geben Sie die neue Tischnummer ein: ")

    if current_table in orders:
        orders[new_table] = orders.pop(current_table)
        print(f"Die Bestellungen wurden erfolgreich von Tisch {current_table} zu Tisch {new_table} verschoben.")
    else:
        print(f"Die Tischnummer {current_table} existiert nicht.")

# Funktion zum Ändern des Namens des Tisches
def change_table_name():
    table = input("Geben Sie die Tischnummer ein, dessen Namen Sie ändern möchten: ")
    if table in orders:
        new_name = input("Geben Sie den neuen Namen für den Tisch ein: ")
        orders[new_name] = orders.pop(table)
        print(f"Der Tisch wurde erfolgreich in '{new_name}' umbenannt.")
    else:
        print(f"Die Tischnummer {table} existiert nicht.")

# Funktion zum Löschen eines Tisches
def delete_table():
    table = input("Geben Sie die Tischnummer ein, den Sie löschen möchten: ")
    if table in orders:
        confirm = input(f"Sind Sie sicher, dass Sie Tisch {table} löschen möchten? (ja/nein): ").lower()
        if confirm == 'ja':
            del orders[table]
            print(f"Tisch {table} wurde erfolgreich gelöscht.")
        else:
            print("Löschvorgang abgebrochen.")
    else:
        print(f"Die Tischnummer {table} existiert nicht.")

# Funktion zum Zurückkehren zur Startseite
def return_to_start():
    print("Zurück zur Startseite.")
    save_orders_to_file()
    main()

# Funktion zum Löschen oder Bearbeiten einer Bestellung
def edit_order():
    table = input("Geben Sie die Tischnummer ein, dessen Bestellung Sie bearbeiten oder löschen möchten: ")
    if table in orders:
        while True:
            display_items_for_table(table)
            order_index = input("Geben Sie die Nummer der Bestellung ein, die Sie bearbeiten oder löschen möchten ('0' zum Speichern und Beenden): ")

            if order_index == '0':
                break

            try:
                order_index = int(order_index) - 1
                if 0 <= order_index < len(orders[table]):
                    edit_option = input("Möchten Sie die Bestellung bearbeiten (b) oder löschen (l)? ")

                    if edit_option.lower() == "b":
                        display_menu()
                        new_category = input("Geben Sie die Nummer der Kategorie ein: ")
                        new_item = input("Geben Sie die Nummer des Produkts ein: ")
                        orders[table][order_index] = (list(menu.keys())[int(new_category) - 1], list(menu.values())[int(new_category) - 1][int(new_item) - 1])
                        print("Die Bestellung wurde aktualisiert.")
                    elif edit_option.lower() == "l":
                        deleted_item = orders[table].pop(order_index)
                        print(f"Die Bestellung {deleted_item} wurde gelöscht.")
                    else:
                        print("Ungültige Option.")
                else:
                    print("Ungültige Bestellungsnummer.")
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine Nummer ein.")
    else:
        print(f"Die Tischnummer {table} existiert nicht.")

# Funktion zum Anzeigen aller Rechnungen
def display_all_bills():
    for table, items in orders.items():
        print(f"Rechnung für Tisch {table}:")
        for category, item in items:
            price = menu[category][item]
            print(f"{item}: {price} Toman")
        total_bill = sum(menu[category][item] for category, item in items)
        print(f"Gesamtbetrag: {total_bill} Toman")
        print()

# Funktion zum Speichern der Bestellungen in einer Textdatei
def save_orders_to_file():
    with open("bestellungen.txt", "w") as file:
        for table, items in orders.items():
            for category, item in items:
                file.write(f"Tisch {table}: {category} {item}\n")

# Funktion zum Laden der Bestellungen aus einer Textdatei
def load_orders_from_file():
    try:
        with open("bestellungen.txt", "r") as file:
            orders_data = file.readlines()
            for order in orders_data:
                order_parts = order.strip().split(": ")
                table = order_parts[0].replace("Tisch ", "")
                category, item = order_parts[1].split(" ")
                orders.setdefault(table, []).append((category, item))
    except FileNotFoundError:
        print("Die Datei 'bestellungen.txt' wurde noch nicht erstellt.")

# Funktion zum Bestellen von Produkten für einen Tisch
def take_order():
    table_number = input("Geben Sie die Tischnummer ein: ")

    while True:
        display_menu()
        category_number = input("Geben Sie die Nummer der Kategorie ein ('0' zum Speichern und Beenden): ")

        if category_number == '0':
            break

        item_number = input("Geben Sie die Nummer des Produkts ein: ")

        category = list(menu.keys())[int(category_number) - 1]
        item = list(menu[category].keys())[int(item_number) - 1]

        orders.setdefault(table_number, []).append((category, item))
        print(f"{item} aus der Kategorie {category} wurde zum Tisch {table_number} hinzugefügt.")

# Funktion zum Ausführen der Anwendung
def main():
    load_orders_from_file()
    while True:
        display_start_options()
        option = input("Geben Sie Ihre Option ein: ")

        if option == "1":
            take_order()
        elif option == "2":
            calculate_bill()
        elif option == "3":
            change_table_options()
        elif option == "4":
            edit_order()
        elif option == "5":
            display_all_bills()
        elif option == "6":
            print("Vielen Dank für die Nutzung der Anwendung!")
            break
        else:
            print("Ungültige Option!")

if __name__ == "__main__":
    main()
