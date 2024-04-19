from math import factorial as f
class Solution(object):
    def getRow(self, rowIndex):
        numRows=rowIndex+1
        l=[]
        l2=[]
        for i in range(numRows):
            l=[]
            for z in range(i+1):
                l.append(f(i)//(f(z)*f(i-z)))
            l2.append(l)
        return l2[rowIndex]



#case 2 to print the whole data
from math import factorial as f
class Solution(object):
    def generate(self, numRows):
        l=[]
        l2=[]
        for i in range(numRows):
            l=[]
            for z in range(i+1):
                l.append(f(i)//(f(z)*f(i-z)))
            l2.append(l)
        return l2
