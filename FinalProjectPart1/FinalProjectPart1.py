# Kyle Dela Pena
# 2038252

import csv
import datetime

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
            # Sort items in alphabetical order based on manfucaturer
            keys = sorted(items.keys(), key=lambda x: items[x]['manufacturer'])
            # Group items into columns

            for item in keys:
                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
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
                if expired:
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
                if damaged:
                    file.write('{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date))

# main method
if __name__ == '__main__':

    items = {}
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                item_id = line[0]
                if file == files[0]:
                    items[item_id] = {}
                    man_name = line[1]
                    item_type = line[2]
                    damaged = line[3]
                    items[item_id]['manufacturer'] = man_name.strip()
                    items[item_id]['item_type'] = item_type.strip()
                    items[item_id]['damaged'] = damaged
                elif file == files[1]:
                    price = line[1]
                    items[item_id]['price'] = price
                elif file == files[2]:
                    service_date = line[1]
                    items[item_id]['service_date'] = service_date

    # Creation of object to use methods which output all csv files
    inventory = CreateInventory(items)
    inventory.complete()
    inventory.type()
    inventory.past_service_date()
    inventory.damaged()
