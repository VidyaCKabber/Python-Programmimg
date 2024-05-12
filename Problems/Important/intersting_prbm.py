class wicketOutException:
    def __init__(self, message):
        self.message = message
        
    def __str__(self):
        return self.message
    
class Match:
    def __init__(self, players1, players2):
        self.players1 = players1
        self.players2 = players2
        
    def findWinner(self):
        p1_count = 0
        p2_count = 0
        
        for i  in range(len(self.players1) - 2):
            if(self.players1[i] %2 == 0 and self.players1[i+1]%2 ==0 and self.players1[i+2]%2 ==0):
               p1_count += 1 
               
        for i  in range(len(self.players2) - 2):
            if(self.players2[i] %2 == 0 and self.players2[i+1]%2 ==0 and self.players2[i+2]%2 ==0):
               p2_count += 1 
    
        if p1_count > p2_count:
            return "Player1"
        elif p1_count < p2_count:
            return "Player2"
        else:
            return wicketOutException("ALL OUT")
        
p1 = [2, 2, 1, 6]
p2 = [4, 8, 1, 3]

a = Match(p1, p2)
print(a.findWinner())
