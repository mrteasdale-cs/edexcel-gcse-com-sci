# Global Variables
cowTable = []
cowKey = ""
# MAIN PROGRAM
file = open("Cows.txt", "r")
# rows = file.readlines() #NOT NECESSARY

for row in file:
    row = row.split(",")
    print(row)
    # assign rows to variables
    breed = row[1]
    tag = int(row[2]) // 100
    name = row[0]
    cowKey = "{}{}{}".format(breed[0:2], str(tag), name[0:2]) # Create the key
    cowTable.append(cowKey)

print(cowTable)
file.close()
