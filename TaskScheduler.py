class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        dicf={}
        for i in tasks:
            if i in dicf:
                dicf[i]+=1
            else:
                dicf[i]=1

        frq=sorted(dicf.values(),reverse=True)
        frequentcy=frq[0]
        repet=1
        i=1
        while i<len(frq) and frq[i]==frq[i-1]:
            repet +=1
            i+=1
        return max((frequentcy-1)*(n+1)+repet,len(tasks))
