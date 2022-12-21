x = "0 2 1 4 0 0 0 0 2 0 1 0 0 3 0 2 0 1 5 0 1 0 42 0 0 0 0 0 0 0 6 0 2 1 2 0 0 0 0 0 10 0 1 2 2 20 5 1 0 4 5 26 0 0 6 0 0 0 0 130 0 0 0 0 0 0 0 55 11 1 0 1 0 0 2 1 63 0 0 0 2 8 1 0 35 3 0 0 0 0 0 6 0 0 0 0 3 0 0 3 0 2 2 2 25 1 0 6 0 0 0 2 47 0 0 0 2 8 2 0 5 3 0 2 0 0 6 3 0"
y = "4 5 4 6 4 4 2 3 5 2 9 2 1 2 2 2 2 9 10 2 0 9 20 4 6 2 1 14 3 3 4 5 4 4 4 1 10 2 2 0 20 1 4 5 9 0 15 6 7 6 5 32 10 6 17 8 6 5 4 260 2 3 9 1 5 2 1 6 0 4 3 2 2 0 7 1 235 3 2 5 2 14 5 6 51 7 4 2 1 7 1 9 6 1 5 13 8 6 3 8 3 5 3 3 50 2 5 8 3 6 2 8 83 12 4 0 4 10 6 2 5 7 10 9 7 2 3 4 2"
x1 = x.split(" ")
y1 = y.split(" ")

x_list = [int(x) for x in x1]
y_list = [int(y) for y in y1]
print(len(x_list), len(y_list))

print(50 in x_list)
print(50 in y_list)
count = 0
for x in x_list:
	if x > 50:
		del x_list[count]
		del y_list[count]
	count += 1
count = 0
for y in y_list:
	if y > 50:
		del x_list[count]
		del y_list[count]
	count += 1

print(len(x_list), len(y_list))


datawrite = open("newData2.txt","a+")
datawrite.write("x = ")
for x in x_list:
	datawrite.write(f"{str(x)} ")
datawrite.write("\ny = ")
for y in y_list:
	datawrite.write(f"{str(y)} ")
