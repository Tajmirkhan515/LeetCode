
#In the world of Dota2, there are two parties: the Radiant and the Dire.

#The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

#Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
#Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
#Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

#The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.




from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        radiant=deque()
        dire=deque()

        for i,senator in enumerate(senate):
            if senator =="R":
                radiant.append(i)
            else:
                dire.append(i)

                
        n=len(senate)

        while radiant and dire:
            r=radiant.popleft()
            d=dire.popleft()

            if r<d:
                radiant.append(r+n)
            else:
                dire.append(d+n)

        return "Radiant" if radiant else "Dire"         
