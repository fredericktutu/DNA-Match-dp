import numpy as np

class Match:
    def __init__(self,p0,p1,p2):
        self.p0, self.p1, self.p2 = p0, p1, p2
        self.isGlobal = True

    def credit(self, c1, c2):
        if c1 == '-' or c2 == '-':
            return self.p2
        if c1 == c2:
            return self.p0
        else:
            return self.p1

    def resetScores(self, p0, p1, p2):
        assert type(p0) == int and type(p0) == type(p1) and type(p1) == type(p2)
        self.p0, self.p1, self.p2 = p0, p1, p2

    def setGlobal(self, yes):
        assert type(yes) == bool
        self.isGlobal = yes


    def match(self, s, t):
        m = len(s)
        n = len(t)
        if self.isGlobal:
            p2 = self.p2
            A = np.empty((m+1,n+1))
            A[0][0] = 0 #初始化左上角
            
            for k in range(1, n+1): #初始化第0行第0列
                A[0][k] = A[0][k-1] + p2
            for k in range(1, m+1):
                A[k][0] = A[k-1][0] + p2
            maxFunc = max
        else:
            A = np.zeros((m+1,n+1))
            maxFunc = lambda x, y, z: max(0, max(x,y,z))

        maxLocal = 0
        for i in range(1, m+1): #行
            for j in range(1, n+1): #列
                replaceOrEqual = A[i-1][j-1] + self.credit(s[i-1],t[j-1])
                deletej = A[i][j-1] + self.credit('-',t[j-1])
                insertj = A[i-1][j] + self.credit(s[i-1],'-')
                A[i][j] = maxFunc(replaceOrEqual, deletej, insertj)
                maxLocal = max(A[i][j], maxLocal)
        if self.isGlobal:
            print(A[m,n])
        else:
            print(maxLocal)

