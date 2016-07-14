"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

# #initialize empty lists for salespeople and melons sold
# salespeople = []
# melons_sold = []

# # open the file sales-report.txt into f 
# f = open("sales-report.txt")

# #loop over each line in file f
# for line in f:
#     #strip the space at the end of the line for each line
#     line = line.rstrip()
#     #split the line on the | symbol
#     entries = line.split("|")
#     #the first entry is the salesperson
#     salesperson = entries[0]
#     #the third entry is the number of melons
#     melons = int(entries[2])

#     # if salesperson is in salespeople list, increment the 
#     # number of melons that is associate with the salesperson
#     # this is done by find the  position of the person and 
#     # incrementing its corresponding position inmelons_sold list
#     if salesperson in salespeople:
#         position = salespeople.index(salesperson)
#         melons_sold[position] += melons
#     else:
#     # if salesperson is not in the salespeople list, add the person and the add the number of melons sold
#         salespeople.append(salesperson)
#         melons_sold.append(melons)

# # for each person in the salespeople list, print the name and number of melons sold
# for i in range(len(salespeople)):
#     print "{} sold {} melons".format(salespeople[i], melons_sold[i])



# Reimplement with dictionary

salespeople = {}

f = open("sales-report.txt")

#loop over each line in file f
for line in f:
    #strip the space at the end of the line for each line
    line = line.rstrip()
    #split the line on the | symbol
    entries = line.split("|")
    salespeople[entries[0]] = {'num_melons' : entries[2],
                               'melons_sold' : entries[1]}

for person, attribute in salespeople.items():
    print "{} sold {} melons".format(person, attribute['num_melons'])



