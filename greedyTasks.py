#import collections
def getStations(needed, data):
    need = set()
    result = []
    for it in needed:
        need.add(it)
    while(need):
        bestState = None
        biggestGraids = set()
        for state, graid in data.items():
            currentGraids = need & graid
            if (len(currentGraids) > len(biggestGraids)):
                biggestGraids = currentGraids
                bestState = state
        result.append(bestState)
        need -= biggestGraids
    return result