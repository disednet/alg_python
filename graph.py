from collections import deque
def extendSearch(data, first, item):
    search_deque = deque()
    search_deque += data[first]
    handled = []
    parent = {}
    parent[first] = []
    for key in data[first]:
        parent[key] = first

    while (search_deque):
        currentItem = search_deque.popleft()
        if not currentItem in handled:
            if (currentItem == item):
                path = []
                path.append(currentItem)
                while (currentItem != first):
                    currentItem = parent[currentItem]
                    path.append(currentItem)
                path.reverse()
                return path

            else:
                search_deque += data[currentItem]
                handled.append(currentItem)
                for key in data[currentItem]:
                    parent[key] = currentItem
    return None

def getMinKey(costs, processed):
    if (len(costs) == 0):
        return None
    min = float('inf')
    outKey = None
    for key, val in costs.items():
        if (val < min and not key in processed):
            min = val
            outKey = key
    return outKey

def dekstraSearch(data, first, item):
    infinity = float('inf')
    parents = {}
    costs = {}
    processed = [first]
    for key in data.keys():
        costs[key] = infinity
    for key in data[first].keys():
        parents[key] = first
        costs[key] = data[first][key]
    #costs[first] = 0
    while (len(processed) < len(costs.keys())):
        currentItem = getMinKey(costs, processed)
        for key, value in data[currentItem].items():
            guessValue = costs[currentItem] + value
            if (costs[key] > guessValue):
                costs[key] = guessValue
                parents[key] = currentItem
        processed.append(currentItem)
    #-----------------------------------    
    path = []
    while (item != first):
        path.append(item)
        item = parents[item]
    path.append(first)
    path.reverse()
    return path