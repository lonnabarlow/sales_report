"""Generate sales report showing total melons each salesperson sold."""


salespeople = []                            #open arrays are made to store the data that will be sorted from the function
melons_sold = []                        """I would add the file as a constant at top"""                            

f = open('sales-report.txt')                #opening the data list that we will be looping through.
for line in f:                              #Here we are looping through each line and seperating lines into arrays.
    line = line.rstrip()                """I would change the variables to be more semantic to the data."""
    entries = line.split('|')

    salesperson = entries[0]                #Here we are going to loop through at the index indicated looking for the 
    melons = int(entries[2])                # salesperson and how many melons were sold by each salesperson.

    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons         
    else:
        salespeople.append(salesperson)             # the loop increments and adds the totals to the empty array.
        melons_sold.append(melons)


for i in range(len(salespeople)):                   #the range function here returns a sequence of numbers starting at 0
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') # going the length of the salespeople array, and prints  
                                                            # the total number of melons sold by each salesperson. 


""" I would add a close for for the open() that we used at the top of the function"""                                                           