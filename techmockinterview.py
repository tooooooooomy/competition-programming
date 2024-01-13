
'''
Imagine we wanted to build a new feature into Google Maps where we help people plan roadtrips. As an example, a user might be trying to make it home in time for the holidays. For the minimum viable product (MVP):

You know:

   * The distance between each stop you want to make along the way
   * How much time you have to get to your destination (in hours)

But
   * You can only drive at one speed the entire trip
   * Even if you finish one stretch early (e.g. 25 miles going 50mph) you CANNOT start the next stretch in the same hours


QUESTION

Write a function that returns the minimum speed (distance per hour) you can drive across the entire trip and still arrive on time.


minDrivingSpeed([3,6,7,11], 8) => 4 because:
  * Cover distances[0] in Hour 1
  * Cover distances[1] in Hours 2 & 3
  * Cover distances[2] in hours 4 & 5
  * Cover distances[3] in Hours 6, 7, & 8
  * (5mph works too, but it is not the minimum speed)

  minimize the speed.
  
  n is lengh of dests
  n >= 1
  h number of hours
  h >= 1 more
output would be integer

speed  = max(dists) => 11

if total_hours = 4 < 8:

while 

M is the max speed

Time
O(log(M) * N + N)

Space
O(1)

      1st
      left = 1, right = 11
      m = 6
      
      3 => 1
      6 => 1
      7 => 2
      11 => 2
      total_hours = 6
      
      left = 1
      right = 5
      
      2nd
      m = 3

      3 => 1
      6 => 2
      7 => 3
      11 => 4
      total_hours = 10
      
      left = 4
      right = 5

[3,6,7,11], 8

1st
left = 1
right = 11

m = 6
th = 6
3 1
6 1
7 2
11 2

'''

def minDrivingSpeed(dests, hours):
   n = len(dests)
   left = 1
   right = max(dests) # => 11
   
   ans = float('inf')
   while left <= right:
       m = (left+right)//2

       th = 0
       for dest in dests:
           th += dest // m
           if th % m > 0:
               th += 1

       if th > hours:
           left = m + 1
       else:
           ans = min(ans, m)
           right = m - 1

   return ans

print(minDrivingSpeed([1, 3, 5, 100], 10))

'''
left = 1
'''
