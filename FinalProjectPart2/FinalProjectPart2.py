# Kyle Dela Pena
# 2038252

import csv # import file to read and write csv files
from datetime import datetime # Needed to have the recent day and time imported into the program

# Class to generate inventory files
class CreateInventory:

    # Create a list of all the items
    def __init__(self, item_list):

        self.item_list = item_list

    # Create a csv file of all items in the inventory files
    def complete(self):

        # Find key order based on Manufacturer
        with open('FullInventory.csv', 'w') as file:
            items = self.item_list
            # Sort items in alphabetical order based on manufacturer
            keys = sorted(items.keys(), key=lambda x: items[x]['manufacturer'])
            # Group items into columns

            # for each item inside of the sorted keys
            for item in keys:
                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                # write each item information respectively: id, man_name, price, service_date, damaged
                file.write('{},{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date, damaged))

    # Creates new csv files for each item type
    def type(self):

        items = self.item_list
        types = []
        # Items sorted based on Item ID
        keys = sorted(items.keys())

        for item in items:
            item_type = items[item]['item_type']
            if item_type not in types:
                types.append(item_type)
        for type in types:
            file_name = type.capitalize() + 'Inventory.csv'
            with open(file_name, 'w') as file:
                for item in keys:
                    id = item
                    man_name = items[item]['manufacturer']
                    price = items[item]['price']
                    service_date = items[item]['service_date']
                    damaged = items[item]['damaged']
                    item_type = items[item]['item_type']
                    if type == item_type:
                        # write each item information respectively: id, man_name, price, service_date, damaged
                        file.write('{},{},{},{},{}\n'.format(id, man_name, price, service_date, damaged))


    # Creates a new csv file for all items that have past the service date
    def past_service_date(self):

        items = self.item_list
        # Sort items based on oldest to newest
        keys = sorted(items.keys(), key=lambda x: datetime.strptime(items[x]['service_date'], "%m/%d/%Y").date(), reverse=True)

        with open('PastServiceDateInventory.csv', 'w') as file:
            for item in keys:
                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                today = datetime.now().date()
                service_expiration = datetime.strptime(service_date, "%m/%d/%Y").date()
                expired = service_expiration < today
                # If product has past expiry date
                if expired:
                    # write each item information respectively: id, man_name, price, service_date, damaged
                    file.write('{},{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date, damaged))

    # Creates a new csv file file for every time that is damaged
    def damaged(self):

        items = self.item_list
        # Sort items based on price
        keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)

        with open('DamagedInventory.csv', 'w') as file:
            for item in keys:
                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                # If item is damaged
                if damaged:
                    # write each item information respectively: id, man_name, price, service_date, damaged
                    file.write('{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date))

# main method
if __name__ == '__main__':

    # instantiate storage for items
    items_storage = {}
    # state list of files to be read
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                item_id = line[0]
                if file == files[0]:
                    items_storage[item_id] = {}
                    man_name = line[1]
                    item_type = line[2]
                    damaged = line[3]
                    items_storage[item_id]['manufacturer'] = man_name.strip()
                    items_storage[item_id]['item_type'] = item_type.strip()
                    items_storage[item_id]['damaged'] = damaged
                elif file == files[1]:
                    price = line[1]
                    items_storage[item_id]['price'] = price
                elif file == files[2]:
                    service_date = line[1]
                    items_storage[item_id]['service_date'] = service_date

    # Creation of object to use methods which output all csv files
    inventory = CreateInventory(items_storage)
    inventory.complete()
    inventory.type()
    inventory.past_service_date()
    inventory.damaged()

    # Get the different manufacturers and types in a list
    list_types = []
    list_manufacturers = []


    for item in items_storage:
        checked_manufacturer = items_storage[item]['manufacturer']
        checked_type = items_storage[item]['item_type']
        if checked_manufacturer not in list_types:
            list_manufacturers.append(checked_manufacturer)
        if checked_type not in list_types:
            list_types.append(checked_type)

    # Prompt the user for input
    user_input = None
    while user_input != 'q':
        user_input = input("\n Enter an item manufacturer and item type (ex: Lenovo tower) or enter 'q' to quit:\n")
        print("Make sure manufacturer first letter is Capitalized")
        if user_input == 'q':
            break
        else:
            # Check each word from user to see if there is a match in manufacturer and item type
            selected_manufacturer = None
            selected_type = None
            user_input = user_input.split()
            bad_input = False
            for word in user_input:
                if word in list_manufacturers:
                    if selected_manufacturer:
                        # Should only have one submitted manufacturer
                        bad_input = True
                    else:
                        selected_manufacturer = word
                elif word in list_types:
                    if selected_type:
                        # Should only have one submitted type
                        bad_input = True
                    else:
                        selected_type = word

            if not selected_manufacturer or not selected_type or bad_input:
                print("No such item in inventory")
            else:
                # sort keys based on highest price
                keys = sorted(items_storage.keys(), key=lambda x: items_storage[x]['price'], reverse=True)

                # Get the matching list of items based on user input
                matching_items = []
                # storage for items that are the same type but different manufacturers
                # items must match and not be past service date or damaged
                similar_items = {}
                for item in keys:
                    if items_storage[item]['item_type'] == selected_type:
                        # Does not add items that are past the service date or damaged
                        today = datetime.now().date()
                        service_date = items_storage[item]['service_date']
                        service_expiration = datetime.strptime(service_date, "%m/%d/%Y").date()
                        expired = service_expiration < today
                        if items_storage[item]['manufacturer'] == selected_manufacturer:
                            if not expired and not items_storage[item]['damaged']:
                                matching_items.append((item, items_storage[item]))
                        else:
                            if not expired and not items_storage[item]['damaged']:
                                similar_items[item] = items_storage[item]

                # If the item matches display the result
                if matching_items:
                    item = matching_items[0]
                    item_id = item[0]
                    man_name = item[1]['manufacturer']
                    item_type = item[1]['item_type']
                    price = item[1]['price']
                    # Display matched item information respectively: item_id, man_name, item_type, price
                    print("Your item is: {}, {}, {}, {}\n".format(item_id, man_name, item_type, price))

                    # Display item that is the same type but different manufacturer, must also be the closest in price
                    if similar_items:
                        matched_price = price
                        # Find the closest item that is closest in price to the matched item
                        closest_item = None
                        closest_price_diff = None
                        for item in similar_items:
                            if closest_price_diff == None:
                                closest_item = similar_items[item]
                                closest_price_diff = abs(int(matched_price) - int(similar_items[item]['price']))
                                item_id = item
                                man_name = similar_items[item]['manufacturer']
                                item_type = similar_items[item]['item_type']
                                price = similar_items[item]['price']
                                continue
                            price_diff = abs(int(matched_price) - int(similar_items[item]['price']))
                            if price_diff < closest_price_diff:
                                closest_item = item
                                closest_price_diff = price_diff
                                item_id = item
                                man_name = similar_items[item]['manufacturer']
                                item_type = similar_items[item]['item_type']
                                price = similar_items[item]['price']
                        # Display similar item information respectively: tem_id, man_name, item_type, price
                        print("You may, also, consider: {}, {}, {}, {}\n".format(item_id, man_name, item_type, price))
                else:
                    # If there is no item that patches, output item does not exist in inventory
                    print("No such item in inventory")