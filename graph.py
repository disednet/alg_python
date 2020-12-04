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

def dekstraSearch(data, first, item):
    return None