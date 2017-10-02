sum = 0
square = 0
start = 1
end = 101

for n in range(start, end):
    square += n*n
    sum += n

print sum*sum - square
