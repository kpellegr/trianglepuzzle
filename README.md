# trianglepuzzle

So my son came home with a piece of math homework. The goal was to practice sums in the hundreds and the exercise was in the form of a puzzle.

The goal is as follows: 
 - you can only use the numbers: 60, 120, 180, 240, 300, 360, 420, 480 and 540 and use each number only once
 - construct a triangle whose sides consist of 4 numbers and each side adds up to 1020
 
 
                360
               /   \
            120    540
           /          \
         420            180
         /                \
       300 -- 240 -- 60 -- 480

Example of a valid triangle (each number is used exacly once), but not a solution to the problem (the sides add up to 1200, 1560 and 1080 respectively)

              180
             /   \
          540    300
         /          \
      240            420
      /                \
    60 -- 480 -- 360 -- 120

Example of a solution (each number is used exacly once and all sides add up to exactly 1020


We found the problem very hard to do by hand and after half an hour we suspected that there were no solutions. We decided to write a small script to test all permutations and found out there are actually 96 solutions. Due to symmetries, not all solutions can be considered unique. But the python script did prove us wrong :-)



