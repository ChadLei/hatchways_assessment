import json
import sys

from collections import defaultdict

class fileConverter():
    def __init__(self, orders_file, dependencies_file, output_file_name):
        # Sets file name variables
        self.orders_file = orders_file
        self.dependencies_file = dependencies_file
        self.output_file_name = output_file_name
        # Sets up dictionaries to hold the orders and a set of order ids
        self.all_orders = defaultdict(dict)
        self.non_dependent_orders = set()
        self.independent_orders = {"orders":[]}

    '''Creates singular dictionaries to store info on each order'''
    def set_orders_as_dicts(self):
        with open(self.orders_file,'r') as f:
            next(f)
            for line in f:
                id,name = line.strip('\n').split(',')
                single_order = {
                  "id": int(id),
                  "name": name,
                  "dependencies": []
                }
                self.all_orders[id] = single_order

    '''Adds all corresponding dependencies to the orders'''
    def set_dependencies_to_orders(self):
        self.set_orders_as_dicts()
        with open(self.dependencies_file,'r') as f:
            next(f)
            for line in f:
                id,child_id = line.strip('\n').split(',')
                self.all_orders[id]["dependencies"].append(self.all_orders[child_id])
                self.non_dependent_orders.add(child_id)

    '''Adds only the orders that are independent of others into the root level'''
    def remove_dependent_orders(self):
        self.set_dependencies_to_orders()
        for order in self.all_orders:
            if order not in self.non_dependent_orders:
                self.independent_orders["orders"].append(self.all_orders[order])

    '''Creates the output file in json format'''
    def sets_dicts_to_json(self):
        self.remove_dependent_orders()
        with open(self.output_file_name,'w') as outfile:
            json.dump(self.independent_orders,outfile,indent=2)

def main(orders_file, dependencies_file, output_file_name):
    file_converter = fileConverter(orders_file,dependencies_file,output_file_name)
    file_converter.sets_dicts_to_json()

if __name__ == '__main__':
    # file_converter = fileConverter("orders.txt","dependencies.txt")
    orders_file = sys.argv[1]
    dependencies_file = sys.argv[2]
    output_file_name = sys.argv[3]
    main(orders_file, dependencies_file, output_file_name)
