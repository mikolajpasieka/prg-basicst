stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
val = lambda x: stock[x][0]*stock[x][1]
total = 0 
y = len(stock) 
for n in range(0,y):
    total += val(n)
print(total)

