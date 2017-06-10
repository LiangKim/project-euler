from functools import reduce

sum_square = reduce(lambda x,y:x+y,range(1,101))**2
square_sum = reduce(lambda x,y:x+y,map(lambda x:x**2, range(1,101)))
diff = sum_square - square_sum
print(diff)