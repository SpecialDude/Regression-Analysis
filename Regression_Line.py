#Program to calculate the Regression Line Equation and the Slope
import sys
import math

def variance(meanx2, meanx):
	var = meanx2 - meanx**2
	return var
def reg_graph(x_list, y_list, x_name, y_name, slope, b0, label):
	import matplotlib.pyplot as plt
	plt.scatter(x_list,y_list)
	plt.xlabel(x_name)
	plt.ylabel(y_name)
	plt.title(label)
	regY = [(x*slope) +b0 for x in x_list]
	plt.plot(x_list, regY, "r-")
	plt.show()
print("copyright, AWA c.2020")
print("This Program will determine the Regression Equation\nAnd Calculate then Predicted Values")
print("\n")
print("Enter 1 to load previous data\n      2 for new data set ")
while True:
	dataInput = input("")
	if dataInput == "1":
		labelData = open(".label.txt","a+")
		labelData.close()
		labelData = open(".label.txt","r")
		labelList = labelData.readlines()
		if labelList == []:
			print("You have no saved data!!!")
			print("Enter '2' for New Data Entry")
			continue
		else:
			dataEntry = open(".dataentry.txt","r")
			dataList = dataEntry.readlines()
			print("")
			print ("Choose a label")
			count = 1
			for i in labelList:
				print(f"{count}. {i}")
				count+=1
			icount = 1
			while True:
				labelChoice = input()
				try:
					names = labelList[int(labelChoice)-1]
					break
				except:
					if icount > 3:
						print(f"Choose between the range (1 - {count - 1})")
					else:
						print("Invalid")
					icount+=1
			namelist = names.split("  ")
			label = namelist[0]
			x_name = namelist[-3]
			y_name = namelist[-1]
			count = 0
			for i in dataList:
				if i == f"{labelChoice}\n":
					break
				count += 1
			x = dataList[count+1]
			y = dataList[count+2]
			x1= x.split(" ")
			y1 = y.split(" ")
			x_list = []
			y_list = []
			for i in x1:
				if i == "\n":
					pass
				else:
					x_list.append(int(i))
			for i in y1:
				if i == "\n":
					pass
				else:
					y_list.append(int(i))
			n = len(x_list)
			sum_x, sum_y, sum_xy, sum_x2, sum_y2 = 0,0,0,0,0
			count = 0
			rList = []
			for x in x_list:
				y = y_list[count]
				xy = x * y
				x2 = x**2
				y2 = y**2
				sum_x += x
				sum_y += y
				sum_xy += xy
				sum_x2 += x2
				sum_y2 += y2
				count += 1
				rList.append(f"{x}\t{y}\t{xy}\t{x2}\t{y2}")
		break
	
	elif dataInput == "2":
		print("")
		x_name = input("Enter the name of the x-variable (Cause): ").title()
		y_name = input("Enter the name of the y-variable (Effect): ").title()
		
		print("\nHow to do want to Input Data?")
		print("1. Enter the values one after other\n2. Enter the Values at once")
		userChoice = input()
		if userChoice == "1":
			n = int(input("Enter the Number of Observations: "))
			count = 1
			sum_x, sum_y, sum_xy, sum_x2, sum_y2 = 0, 0, 0, 0, 0
			rList= []
			x_list = []
			y_list = []
			print("")
			while count <= n:
				x = int(input(f"Enter the value of {x_name} {count}: "))
				y = int(input(f"Enter the value of {y_name} {count}: "))
				xy = x*y
				x2 = x**2
				y2 = y**2
				sum_x += x
				sum_y += y
				sum_xy += xy
				sum_x2 += x2
				sum_y2 += y2
				count += 1
				x_list.append(x)
				y_list.append(y)
				rList.append(f"{x}\t{y}\t{xy}\t{x2}\t{y2}")
				
		elif userChoice == "2":
			print("")
			x = input ("Enter the values of x (seperated by space): ")
			x1=x.split(" ")
			y = input ("Enter the values of y (seperated by space): ")
			y1 = y.split(" ")
			if len(x1) == len(y1):
				n = len(x1)
				x_list = []
				y_list = []
				for i in x1:
					x_list.append(int(i))
				for i in y1:
					y_list.append(int(i))
				sum_x, sum_y, sum_xy, sum_x2, sum_y2 = 0,0,0,0,0
				count = 0
				rList = []
				for x in x_list:
					y = y_list[count]
					xy = x * y
					x2 = x**2
					y2 = y**2
					sum_x += x
					sum_y += y
					sum_xy += xy
					sum_x2 += x2
					sum_y2 += y2
					count += 1
					rList.append(f"{x}\t{y}\t{xy}\t{x2}\t{y2}")
			else:
				print ("Number of values of x does not tally with y")
				sys.exit()
		break
	else:
		print("Invalid input, Enter (1 or 2)")

if dataInput == "1":
	pass
else:	
	print("Save Data entries? (yes or no)")
	userResp = input()
	if userResp == "yes":
		label = input("Enter a label for the Entry: ")
		labelData = open(".label.txt","a+")
		labelData.write(f'{label}:  {x_name}  &  {y_name} \n')
		labelData.close()
		dataEntry = open(".dataentry.txt","a+")
		dataEntry.close()
		dataEntry = open(".dataentry.txt","r")
		dataList = dataEntry.readlines()
		if dataList == []:
			dataEntry.close()
			dataEntry = open(".dataentry.txt","a+")
			dataEntry.write("1\n")	
		else:
			k = dataList[-3]
			k = int(k) + 1
			dataEntry.close()
			dataEntry = open(".dataentry.txt","a+")
			dataEntry.write(f"{str(k)}\n")
		for i in x_list:
			dataEntry.write(f"{str(i)} ")
		dataEntry.write("\n")
		for i in y_list:
			dataEntry.write(f"{str(i)} ")
		dataEntry.write("\n")
		dataEntry.close()
		print("Entry Saved!!!\n")
	else:
		label = ""

print("")
print(f"x\ty\txy\tx\u00B2\ty\u00B2")
print("\t\t\t\t")
for i in rList:
	print(i)
print("")
print(f"n = {n}")
print (f"\u03a3x = {sum_x}\n\u03a3y = {sum_y}\n\u03a3xy = {sum_xy}\n\u03a3x\u00B2 = {sum_x2}\n\u03a3y\u00B2 = {sum_y2}")
print("")
nume = sum_xy - ((sum_x * sum_y)/n)
denom = sum_x2 - (((sum_x)**2)/n)
slope = nume / denom
y_mean = sum_y/n
x_mean = sum_x/n
y2_mean = sum_y2/n
x2_mean = sum_x2/n
bO = y_mean - (slope * x_mean)

print("Determining the Type of Correlation of the two variables\n")
var_x = variance(x2_mean, x_mean)
var_y = variance(y2_mean,y_mean)
sd_x = math.sqrt(var_x * n)
sd_y = math.sqrt(var_y * n)

count = 0
coVar = 0
for i in x_list:
	xSub = i - x_mean
	ySub = y_list[count] - y_mean
	sCovar = xSub * ySub
	coVar += sCovar
	count += 1

r = round(coVar / (sd_y * sd_x),5)
print(f"The coefficient of correlation of the two variables is: \n     r  =  {r}")
print("\nType of Correlation:")
if r == 1:
	print("Perfect Positive Linear Correlation")
elif r == -1:
	print("Perfect Negative Linear Correlation")
elif r == 0:
	print("No Linear Correlation")
else:
	if r > 0:
		if r >= 0.7 and r < 1:
			print("Strong Positive Linear Correlation")
		elif r <= 0.3:
			print ("Week Positive Linear Correlation")
		else:
			print("Positive Linear Correlation")
	else:
		if r <= 0.7 and r > -1:
			print('Strong Negative Linear Correlation')
		elif r >= -0.3:
			print('Weak Negative Linear Correlation')
		else:
			print('Negative Linear Correlation')

print("")
print("Computing the Equation of Regression\n")

print(f"b\u2080 = {round(bO,2)}")
print(f"b\u2081 = {round(slope,2)}")
print("")

print ("The Equation of the Regression is:")
equation = f"y\u0302 = {round(sum_y/n,2)} + {round(slope,2)}(x - {round(sum_x/n,2)})"
print(equation)
equation2 = f"y\u0302 = {round(bO,2)} + {round(slope,2)}x"
print(equation2)

"""print("")
upper = (n * sum_xy) - (sum_x * sum_y)
lower = ((n * sum_x2) - (sum_x ** 2)) * ((n * sum_y2) - (sum_y ** 2))
lower = math.sqrt(lower)
r2 = round(upper/lower,5)
print(f"r = {r2}")
print(f"Difference = {r - r2}")"""

print("\nSHOWING THE GRAPH")
reg_graph(x_list, y_list, x_name, y_name, slope, bO, label)
while True:
	print(f"\nEnter 1 to calculate the Predicted {x_name}")
	print(f"      2 to calculate the Predicted {y_name}")
	print(f"      0 to quit")
	userInput = input()
	if userInput == "1":
		yn = float(input(f"Enter the value of {y_name}: "))
		pX = ((yn - y_mean) / slope) + x_mean
		print(f"The Predicted {x_name} = ", pX)
	elif userInput == "2":
		xn = float(input(f"Enter the value of {x_name}: "))
		pY = y_mean + (slope * (xn - x_mean))
		print(f"The Predicted {y_name} = ", pY)
	else:
		break
