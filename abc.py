import random, math
class artificialBeeAlgorithm():
    def __init__(self, ncfs = 30, mi = 100, dl = 10, ll = -10.0, ul = 3.0, afv = 0.99):
        self.__ncfs = ncfs
        self.__mi = mi
        self.__dl = dl
        self.__ll = ll
        self.__ul = ul
        self.__afv = afv
        self.__cfs = []
        self.__ra = self.__mainCore()
        # ncfs   : number of candidate food sources
        # mi     : maximum iteration
        # dl     : drop limit
        # ll     : lower limit of the area to be searched
        # ul     : upper limit of the area to be searched
        # afv    : acceptable fitness value ( 0 - 1 )
        # lcfs   : list of candidate food sources
        # ra     : result array

    def getResult(self):
        return self.__ra

    def getCandidateFoodSources(self):
        return self.__cfs

    def __findBest(self):
        return max(self.__cfs)

    def __generateCandidateFoodSources(self):
        k = []
        for i in range(self.__ncfs):
            xValue = random.uniform(self.__ll, self.__ul)
            fv = self.__fitnessValue(xValue)
            k.append([fv, xValue, 0])
        return k

    def __fitnessValue(self, p):
        return 1 / (1 + math.fabs(self.__polynom(p)))

    def __polynom(self, x):
        return x * x - 8 * x + 15

    def __sendWorkerBees(self):
        Vij = 0.0
        Q_teta = 0.0
        # k=0
        for i in range(self.__ncfs):
            k = i
            while k == i:
                k = random.randrange(0, self.__ncfs)
            Q_teta = random.uniform(-1.0, 1.0)
            Vij = self.__cfs[i][1] + Q_teta * (self.__cfs[i][1] - self.__cfs[k][1])
            if Vij > self.__ul: Vij = self.__ul
            if Vij < self.__ll: Vij = self.__ll

            if self.__fitnessValue(Vij) > self.__cfs[i][0]:
                self.__cfs[i][0] = self.__fitnessValue(Vij)
                self.__cfs[i][1] = Vij
                self.__cfs[i][2] = 0
            else:
                self.__cfs[i][2] += 1

    def __sumList(self, index = 0):
        sums = 0.0
        for i in range(self.__ncfs):
            sums += self.__cfs[i][index]
        return sums

    def __selectionByLookoutBees(self):
        sumOfFitness = self.__sumList()
        Vij = 0.0
        Q_teta = 0.0
        # k=0
        for i in range(self.__ncfs):
            if random.random() < self.__cfs[i][0] / sumOfFitness:
                k = i
                while k == i:
                    k = random.randrange(0, self.__ncfs)
                Q_teta = random.uniform(-1.0, 1.0)
                Vij = self.__cfs[i][1] + Q_teta * (self.__cfs[i][1] - self.__cfs[k][1])
                if Vij > self.__ul: Vij = self.__ul
                if Vij < self.__ll: Vij = self.__ll

                if self.__fitnessValue(Vij) > self.__cfs[i][0]:
                    self.__cfs[i][0] = self.__fitnessValue(Vij)
                    self.__cfs[i][1] = Vij
                    self.__cfs[i][2] = 0
                else:
                    self.__cfs[i][2] += 1

    def __changeNonimprovingResources(self):
        for i in range(self.__ncfs):
            if self.__cfs[i][0] > self.__dl:
                xValue = random.uniform(self.__ll, self.__ul)
                fv = self.__fitnessValue(xValue)
                self.__cfs[i][0] = fv
                self.__cfs[i][1] = xValue
                self.__cfs[i][2] = 0

    def __mainCore(self):
        self.__cfs = self.__generateCandidateFoodSources()
        ra = ["", "", ""]
        i = 1
        while not (self.__findBest()[0] >= self.__afv or i > self.__mi):
            self.__sendWorkerBees()
            self.__selectionByLookoutBees()
            self.__changeNonimprovingResources()
            i += 1
        ra[0] = self.__findBest()[0]
        ra[1] = self.__findBest()[1]
        ra[2] = i - 1
        return ra
# ends class description
