

You’re a newly-hired software developer working at a home repair services company.
This company uses a very old job scheduling system: plain text files that list all of their
data models.
As part of their effort to join the 21st century, the company is transitioning to a more
modern system. However, all of the previous data still exists as plain text files and will
have to be converted. This is where you come in.
Your boss needs you to develop a utility that takes a pair of plain text files as the input
(orders and dependencies) and outputs a structured JSON file that shows all work
orders and their dependencies. The details are described in the sections below.

# The inputs to your application are two text files. Here is a compressed folder with an
# example of the two input files. The text files are described in the sections below.

orders.txt
This file contains information about the orders. The file has the following columns:
  ● id - the id of the order (any integer between 0 and 10000)
  ● name - the name of the order (any string of length 1 to 100)

Here is the content of the example input:
id,name
1,Pick up pipes and tiles
2,Install tiles
3,Install pipes
4,Waterproof pipes
5,Remove old tiles
6,Rustproof pipes

dependencies.txt
This file contains all dependency relationships. Each row represents one dependency
(i.e. in the example below, order 2 depends on order 1 being completed). The file has
the following columns:
  ● id - the id of an order
  ● child_id - the id of an order that depends on the order in column 1
Here is the content of the example input:
id,child_id
1,2
1,3
3,4
5,2
3,6

# Output
The expected output of the program is a JSON file that shows all the work orders and
their dependencies.
Note:
  ● At the root (first) level, only the orders that are not dependent on any other
  order are outputted
  ● For each order, show all the dependencies for that order
  ● Orders can be shown multiple times (i.e they may depend on multiple orders)
  
  
