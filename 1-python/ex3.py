#prints the average of the values in the list:

a = [1, 2, 5, 10, 255, 3]
sum = 0.0

for val in a:
    sum += val
avg = sum/len(a)
print avg
