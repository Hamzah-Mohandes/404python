import tkinter as tk
from tkinter import messagebox


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

# Funktion zum Anzeigen der GUI
def main_gui():
    global root
    root = tk.Tk()
    root.title("Kassenprogramm")

    load_orders_from_file()
    display_start_options_gui()

    root.mainloop()


# Funktion zum Laden der Bestellungen aus einer Textdatei
def load_orders_from_file():
    global orders
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

# Funktion zum Anzeigen der Startseite in der GUI
def display_start_options_gui():
    start_options_label = tk.Label(root, text="Startseite:")
    start_options_label.pack()

    order_button = tk.Button(root, text="Produkt bestellen", command=take_order_gui)
    order_button.pack()

    bill_button = tk.Button(root, text="Rechnung anzeigen", command=calculate_bill_gui)
    bill_button.pack()

    change_table_button = tk.Button(root, text="Tisch wechseln", command=display_table_change_options_gui)
    change_table_button.pack()

    edit_order_button = tk.Button(root, text="Bestellung löschen oder bearbeiten", command=edit_order_gui)
    edit_order_button.pack()

    display_all_bills_button = tk.Button(root, text="Gesamte Rechnungen anzeigen", command=display_all_bills_gui)
    display_all_bills_button.pack()

    exit_button = tk.Button(root, text="Programm verlassen", command=root.destroy)
    exit_button.pack()

# Funktionen zum Anzeigen der Artikel für alle Tische, Optionen für Tischwechsel und Artikel für eine bestimmte Tischnummer in der GUI
def display_all_items_gui():
    all_items_label = tk.Label(root, text="Übersicht aller Tische und ihrer Bestellungen:")
    all_items_label.pack()

    for table, items in orders.items():
        table_label = tk.Label(root, text=f"Tisch {table}:")
        table_label.pack()

        for index, (category, item) in enumerate(items, start=1):
            item_label = tk.Label(root, text=f"{index}. {item} aus der Kategorie {category}")
            item_label.pack()

        empty_line_label = tk.Label(root, text="")
        empty_line_label.pack()

def display_table_change_options_gui():
    table_change_options_label = tk.Label(root, text="Optionen für Tischwechsel:")
    table_change_options_label.pack()

    change_table_button = tk.Button(root, text="Tisch wechseln", command=change_table_gui)
    change_table_button.pack()

    change_table_name_button = tk.Button(root, text="Name des Tisches ändern", command=change_table_name_gui)
    change_table_name_button.pack()

    delete_table_button = tk.Button(root, text="Tisch löschen", command=delete_table_gui)
    delete_table_button.pack()

    return_to_start_button = tk.Button(root, text="Zurück zur Startseite", command=return_to_start_gui)
    return_to_start_button.pack()

def display_items_for_table_gui(table):
    if table in orders:
        table_label = tk.Label(root, text=f"Bestellungen für Tisch {table}:")
        table_label.pack()

        for index, (category, item) in enumerate(orders[table], start=1):
            item_label = tk.Label(root, text=f"{index}. {item} aus der Kategorie {category}")
            item_label.pack()
    else:
        messagebox.showinfo("Fehler", f"Die Tischnummer {table} existiert nicht.")

# Funktionen zum Anzeigen aller Rechnungen und zur Rückkehr zur Startseite in der GUI
def display_all_bills_gui():
    for table, items in orders.items():
        bill_label = tk.Label(root, text=f"Rechnung für Tisch {table}:")
        bill_label.pack()

        for category, item in items:
            price = menu[category][item]
            item_label = tk.Label(root, text=f"{item}: {price} Toman")
            item_label.pack()

        total_bill = sum(menu[category][item] for category, item in items)
        total_bill_label = tk.Label(root, text=f"Gesamtbetrag: {total_bill} Toman")
        total_bill_label.pack()

        empty_line_label = tk.Label(root, text="")
        empty_line_label.pack()

def return_to_start_gui():
    save_orders_to_file()
    root.destroy()
    main()

# Funktionen zum Bestellen von Produkten, Berechnen der Rechnung, Ändern des Tisches, Ändern des Tischnamens, Löschen des Tisches und Bearbeiten der Bestellung
def take_order_gui():
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


def calculate_bill_gui():
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

def change_table_gui():
    global orders
    current_table = input("Geben Sie die aktuelle Tischnummer ein: ")
    new_table = input("Geben Sie die neue Tischnummer ein: ")

    if current_table in orders:
        orders[new_table] = orders.pop(current_table)
        print(f"Die Bestellungen wurden erfolgreich von Tisch {current_table} zu Tisch {new_table} verschoben.")
    else:
        print(f"Die Tischnummer {current_table} existiert nicht.")

def change_table_name_gui():
    table = input("Geben Sie die Tischnummer ein, dessen Namen Sie ändern möchten: ")
    if table in orders:
        new_name = input("Geben Sie den neuen Namen für den Tisch ein: ")
        orders[new_name] = orders.pop(table)
        print(f"Der Tisch wurde erfolgreich in '{new_name}' umbenannt.")
    else:
        print(f"Die Tischnummer {table} existiert nicht.")

def display_menu():
    print("Speisekarte:")
    for i, (category, items) in enumerate(menu.items(), start=1):
        print(f"{i}. {category}:")
        for j, (item, price) in enumerate(items.items(), start=1):
            print(f"   {j}. {item} - {price} Toman")
def delete_table_gui():
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

def edit_order_gui():
    table = input("Geben Sie die Tischnummer ein, dessen Bestellung Sie bearbeiten oder löschen möchten: ")
    if table in orders:
        while True:
            display_items_for_table_gui(table)
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

def save_orders_to_file():
    with open("bestellungen.txt", "w") as file:
        for table, items in orders.items():
            for category, item in items:
                file.write(f"Tisch {table}: {category} {item}\n")

if __name__ == "__main__":
    main_gui()
