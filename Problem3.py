a = int(input("Enter a number: "))
series = []

for i in range(a):
    series.append(2 * i + 1)

if a % 2 == 0: 
    series.pop()

print("Series:", series)