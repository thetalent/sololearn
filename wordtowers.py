farben = {"r":"rot","g":"gelb","b":"blau"}
r ,g,b = "r","g","b"

class stein:
    def __init__(self,farbe,letter):
        self.farbe = farbe
        self.letter = letter
    def __eq__(self, other):
        return self.farbe == other.farbe and self.letter == other.letter
    def __repr__(self):
        return self.farbe+self.letter
class heap:
    def __init__(self,h):
        self.heap = h
    def __eq__(self,other):
        if not len(self) == len(other):
            return false
        for i in range(len(self.h)):
            if self.h[i]!= other.h[i]:
                return false        
        return true
    def __repr__(self):
        return " ".join([s for s in self.heap])
# Beide Stapel
class state:
    def __init__(self,links,rechts):
        self.links = links
        self.rechts = rechts
        
    def __repr__(self):
        return str((self.links,self.rechts))
    def __eq__(self,other):
        return self.links == other.links and self.rechts == other.rechts
    def createNewState(self,q,n):
        
        if q == "l":
            if len(self.links)<n+1:
                return None
            if self.rechts:
                if self.links[n].farbe == self.rechts[0].farbe:
                    return None
            #print(f"new state from {self} to {state(self.links[n+1:],self.links[:n+1]+self.rechts)} by {q}")
            return state(self.links[n+1:],self.links[:n+1]+self.rechts)
        if q == "r":
            if len(self.rechts)<n+1:
                return None
            if self.links:
                if self.rechts[n].farbe == self.links[0].farbe:
                    return None
            #print(f"new state from {self} to {state(self.rechts[n+1:]+self.links,self.rechts[:n+1])} by {q}")
            return state(self.rechts[:n+1]+self.links,self.rechts[n+1:])
class solution:
    def __init__ (self,moves,state):
        self.moves = moves
        self.state = state
    def solved(self,solheap):
        return self.state.rechts == solheap
        
              
    
    


class game:
    # start und ziel als
    def __init__(self):
        wort = "sololearn"
        self.farben = [r,g]*5
        self.heapl = []
        self.heapr = []
        
        self.done = []
        self.states = []
        self.solutions = []
        for i in range(len(wort)):
            s = stein(self.farben[i],wort[i])
            self.heapl.append(s)
        self.states.append(state(self.heapl,self.heapr))
        self.done.append(state(self.heapl,self.heapr))
        self.solutions.append(solution([],state(self.heapl,self.heapr)))
        self.ziel = self.heapl[:]
    def findSolution(self):
        tries = 10
        cnt = 0
        while self.solutions:
            cnt+=1
            if cnt == tries:
                print(f"{cnt} tries")
                tries*=10
            s = self.solutions.pop(0)
            self.done.append(s.state)
            o = "l"
            sstate = s.state
            for i in range(3):
                newm = s.moves[:]
                newstate=sstate.createNewState(o,i)
                if newstate:
                    newm.append(str(i+1)+o)
                    if newstate.rechts == self.ziel:                       
                        print("Ziel erreicht ",newm,newstate)
                        return
                        
                    else:
                        if all([s != newstate for s in self.done]):
                            self.solutions.append(solution(newm,newstate))
                            #self.done.append(newstate)
                            
                        
            o = "r"
         
            sstate = s.state
            for i in range(3):
                newm = s.moves[:]
                newstate=sstate.createNewState(o,i)
                newm.append(str(i+1)+o)
                if newstate:
                    if newstate.rechts == self.ziel:                        
                        print("Ziel erreicht",newm,newstate)
                        return
                    else:
                        if all([s != newstate for s in self.done]):
                            self.solutions.append(solution(newm,newstate))
                            self.done.append(newstate)
        print(self.solutions)
mygame = game()
mygame.findSolution()
                                      
                                      
                    
                
        
      
            