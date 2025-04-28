# Y10 Mini Project - Temps
tempsList = []
tempDiff = []

def menu():
    print("Data Analysis Tool")
    print("1. Get Difference in temperatures")
    print("2. Find a countries temperature")

def readFile(fileName):
    with open(fileName, "r") as file:
        print("File opened successfully")
        for row in file:
            row = row.strip().split("\t")  # strip() is added to remove leading/trailing whitespaces
            tempsList.append(row)
    return tempsList

def calculateTempDiff(array):
    for row in array:
        difference = float(row[1]) - float(row[2])
        appendString = f"{row[0]} {difference:.4f}"
        tempDiff.append(appendString)
    return tempDiff

def findTemp(array, searchTerm):
    foundRow = []
    found = False
    for row in array:
        if searchTerm.lower() == row[0].lower():
            found = True
            foundRow = f"{row[0]} {row[1]}degrees celcius"
    if found:
        return foundRow
    else:
       return "Country not found"

input("Press enter to start")
tempsList = readFile("temperatures.csv")
print(tempsList)
menu()
choice = input("Enter Choice: ")
if choice == "1":
    tempDiff = calculateTempDiff(tempsList)
    for row in tempDiff:
        print(row)
elif choice == "2":
    searchTerm = input("Enter a country: ")
    result = findTemp(tempsList, searchTerm)
    print(result)  # print the result of findTemp
else:
    print("Invalid choice")
