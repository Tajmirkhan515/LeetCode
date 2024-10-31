#735. Asteroid Collision

#We are given an array asteroids of integers representing asteroids in a row.

#For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

#Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.



class Solution(object):
    def asteroidCollision(self, asteroids):
        
        result=[]

        for ast in asteroids:
            
            while result and ast<0 and result[-1]>0:
                if result[-1]<abs(ast):
                    result.pop()
                    continue
                elif result[-1]==abs(ast):
                    result.pop()
                break

            else:
                result.append(ast)

        return result
