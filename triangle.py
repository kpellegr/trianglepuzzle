import itertools

# the orginial puzzle uses numbers in the range of hundreds, but we realized they are all multiples of 60. 
# So we optimized a bit and solved the puzzle with numbers 1 through 9 and try to add up to 17.

goal = 17
perm = itertools.permutations(range(1,10)) 

for p in perm:
  l = list(p)
  l.append(p[0]) # copy the first element to the end, to create the notion of a closed triangle

  side1 = sum(l[0:4]) #sum elements 1-4 (1st side of triangle)
  side2 = sum(l[3:7]) #sum elements 4-7 (2nd side of triangle)
  side3 = sum(l[6:10]) #sum elements 7-1 (3rd side of triangle)

  if side1 == side2 == side3 == goal:
    print (l)
