# CASH ME OUSSIDE - HackFSU'17

# CASH ME OUSSIDE is a program that allows users to quickly
# check their funds based on certain budgeting standards
# that can be set by the user

# The budgets and values don't have to represent all their money
# But can instead represent their savings, or spending money, and be further
# Divided amongst categories

# Ideally there will be a button that checks to see if the user is approaching low values for their money
# So that they will know to spend less or reevaluate their budget in a way
# that allows them to continue their spending habits in a more acceptable way

# Begin lineItem class
class lineItem(object):

	# lineItem methods

	def __init__(lineItem,percentage,name):
		lineItem.percentage = percentage
		lineItem.name = name

	def showBudget(lineItem):
		print("Percentage allocated to "+lineItem.name)
		print lineItem.percentage

	def getPercentage(lineItem):
		return lineItem.percentage

	def getName(lineItem):
		return lineItem.name

	def setPercentage(lineItem, newPercentage):
		lineItem.percentage = newPercentage

	def setName(lineItem, newName):
		lineItem.name = newName

# End Class

# Begin readFile
def readFile():
	import os
	tf = open(os.path.expanduser("~/Desktop/AllCode/Python/hackfsu.txt"))
	var = tf.readline()
	x = int(var)
	numLineItems = x
	budgetList = [None]*x;

	for i in xrange(0, numLineItems):
		itemName = tf.readline().splitlines()
		var = tf.readline().splitlines()
		x = int(var[0])
		budget = x
		budgetList[i] = lineItem(budget,itemName[0])

	return budgetList

def updateFile(budgetList):
	tf = open("hackfsu.txt", 'w')
	for i in xrange(0, len(budgetList)):
		string = str(budgetList[i].getName())+"\n"
		var = str(int(budgetList[i].getPercentage()))+"\n"
		tf.write(string)
		tf.write(var)
	return budgetList

# get the current sum of values and redistrubute
def alterBudget(budgetList):
	for i in xrange(0, len(budgetList)):
		newPercentage = input("Please enter the new percentage for line item #"+str(i+1)+", "+str(budgetList[i].getName())+":\n")
		budgetList[i].setPercentage(newPercentage)

	updateFile(budgetList)
	return budgetList

def alterCash(cashList, budgetList):
	totalCash = 0
	for i in xrange(0, len(cashList)):
		totalCash += cashList[i]
	for i in xrange(0, len(cashList)):
		cashList[i] = (budgetList[i].getPercentage()/100.0)*(totalCash*1.0)
	return cashList

def cashMath(budgetList,cashList,cashInput):
	for i in xrange(0, len(cashList)):
		cashList[i] = (cashList[i]*1.0)+cashInput*(budgetList[i].getPercentage()/100.0)
	return cashList

def printCurrentMoneyz(cashList, budgetList):
	print("Current funds:")
	for i in xrange(0, len(cashList)):
		print str(budgetList[i].getName()) +": $"+ str(cashList[i])

def subtractCash(cashList, budgetList):
	print("Please select the line item you would like to subtract funds from: ")
	for i in xrange(0, len(cashList)):
		print(str(i+1)+". "+budgetList[i].getName())
	userInput = input("")
	subtract = input("Please enter the amount you would like to remove from this line item\nYou have $"+str(cashList[userInput-1])+" left\n")
	if cashList[userInput-1] - subtract >= 0:
		cashList[userInput-1] -= subtract
		print("$"+str(subtract)+" subtracted from "+str(budgetList[userInput-1].getName()))
	else:
		print("Subtracting results in a negative value. Cannot execute.")
	return cashList

def initializeAccount():
	tf = open("hackfsu.txt", 'w')
	print("Welcome to the \"Cash me Ousside\" Account Manager!")
	b = True
	while b == True:
		numItems = input("Please enter the number of line items you plan to include in this budget plan:\n")
		if numItems > 0:
			b = False

	tf.write(str(int(numItems))+"\n")
	sumInput = 0

	for i in xrange(0 , numItems):
		b = True
		while b == True:
			itemName = raw_input("Please enter the name of line item #"+str(i+1)+":\n")
			itemPercent = input("Please enter the percentage to allocate to that item:\n")
			if sumInput + itemPercent <= 100:
				sumInput = sumInput + itemPercent
				tf.write(str(itemName)+"\n")
				tf.write(str(itemPercent)+"\n")
				b = False
			else:
				print("Try again!")
def main():

	initializeAccount()

	validInput = True
	budgetList = readFile();
	cashList = [0]*len(budgetList)

	while validInput != False:

		print("Please select an option from the menu:")
		userInput = input("1. Add funds\n2. Display current funds per line item\n3. Alter budgeting\n4. Reduce funds to a line item\n5. Exit program\n")
		if userInput == 1:
			cashInput = input("Please enter the amount to add:\n")
			if cashInput >= 0:
				cashList = cashMath(budgetList, cashList, cashInput)
			else:
				print("Please input a non-negative number")

		elif userInput == 2:
			printCurrentMoneyz(cashList,budgetList)

		elif userInput == 3:
			budgetList = alterBudget(budgetList)
			cashList = alterCash(cashList,budgetList)

		elif userInput == 4:
			cashList = subtractCash(cashList, budgetList)

		elif userInput == 5:
			print("Exiting")
			exit()

		else:
			print("Invalid input")

if __name__ == "__main__": main()
