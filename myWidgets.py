def printInMyFormat2d(set2d):
    for i in range(len(set2d)):
        print(i+1, "{0:9.2f}".format(set2d[i][0]), "{0:9.4f}".format(set2d[i][1]), "{0:9.0f}".format(set2d[i][2]), sep=" ")
def printInMyFormat1d(set1d):
    print("{0:9.2f}".format(set1d[0]), "{0:9.1f}".format(set1d[1]), "{0:9.0f}".format(set1d[2]), sep=" ")

def printInMyFormat2d8(set2d):
    for i in range(len(set2d)):
        print(i+1,
              "{0:9.2f}".format(set2d[i][0]),
              "{0:9.2f}".format(set2d[i][1]),
              "{0:9.2f}".format(set2d[i][2]),
              "{0:9.2f}".format(set2d[i][3]),
              "{0:9.2f}".format(set2d[i][4]),
              "{0:9.2f}".format(set2d[i][5]),
              "{0:9.2f}".format(set2d[i][6]),
              "{0:9.2f}".format(set2d[i][7]),
              sep=" ")
