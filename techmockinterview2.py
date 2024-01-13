
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

m = 1

M = max(minDrivingSpeed)
the answer should be inbetween them

if go linear, start from 1 then find the speed which does not over 8
'''

def _minDrivingSpeed(dests, limit_hours):
    ans = max(dests)
    for speed in range(1, max(dests)):
        s = 0
        for dest in dests:
            t = dest // speed
            if t == 0:
                t += 1
            elif dest % speed != 0:
                t += 1

            s += t

        if s <= limit_hours:
            ans = min(ans, speed)

    return ans

def minDrivingSpeed(dests, limit_hours):
    left, right = 1, max(dests)

    while left <= right:
        m = (left+right)//2
        total_h = 0
        for dest in dests:
            t = dest // m

            if t == 0:
                t += 1
            elif dest % m != 0:
                t += 1

            total_h += t

        if total_h > limit_hours:
            left = m + 1
        else:
            right = m - 1

    return left

a = minDrivingSpeed([3,6,7,11], 8)
print(a)
