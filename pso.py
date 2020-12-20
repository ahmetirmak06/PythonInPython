import random, math


class particleSwarmOptimization():
    def __init__(self, nsp = 4, mi = 100, c1 = 1.3, c2 = 1.3, ll = 0.0, ul = 10.0, afv = 0.99):
        self.__nsp = nsp
        self.__mi = mi
        self.__c1 = c1
        self.__c2 = c2
        self.__ll = ll
        self.__ul = ul
        self.__afv = afv
        self.__lsp = []
        self.__ra = self.__mainCore()
        # nsp     : number of swarm particles
        # mi     : maximum iteration
        # c1     : coefficient 1
        # c2     : coefficient 2
        # ll     : lower limit of the area to be searched
        # ul     : upper limit of the area to be searched
        # afv    : acceptable fitness value ( 0 - 1 )
        # lsp   : list of swarm particles
        # ra     : result array
    def getParticles(self):
        return self.__lsp

    def __generateParticles(self):
        k = []
        for i in range(self.__nsp):
            xValue = random.uniform(self.__ll, self.__ul)
            V = random.random()
            r1 = random.random()
            r2 = random.random()
            fv = self.__fitnessValue(xValue)
            k.append([fv, xValue, xValue, V, r1, r2, self.__c1, self.__c2 ])
            #fitness,best,X,V,r1,r2,c1,c2
        return k

    def __fitnessValue(self, p):
        return 1 / (1 + math.fabs(self.__polynom(p)))

    def __polynom(self, x):
        return x * x - 2 * x - 15

    def __mainCore(self):
        self.__lsp = self.__generateParticles()
        ra = ["", "", ""]
        i = 1
