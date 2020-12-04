import search
import unittest
import random
import copy
import graph
random.seed()
class TestSearchMethod(unittest.TestCase):
    def test_bynarySearh_1(self):
        data = [1,2,45,56,100,178, 290]
        self.assertEqual(search.binarySearch(data, 100), 4)
        self.assertEqual(search.binarySearch(data, 178), 5)
        self.assertEqual(search.binarySearch(data, 1), 0)
        self.assertEqual(search.binarySearch(data, 2), 1)

    def test_bynarySearchRecursive_1(self):
        data = [1,2,45,56,100,178, 290]
        self.assertEqual(search.binarySearchRecursive(data, 100), 4)
        self.assertEqual(search.binarySearchRecursive(data, 178), 5)
        self.assertEqual(search.binarySearchRecursive(data, 1), 0)
        self.assertEqual(search.binarySearchRecursive(data, 2), 1)

    def test_binarySearch_Cmp(self):
        
        data = []
        for i in range (10000):
            data.append(random.randint(1, 100000000))
        for i in range (100):
            number = random.randint(1, 100000000)
            self.assertEqual(search.binarySearch(data, number), search.binarySearchRecursive(data, number))

        
class TestSortMethod(unittest.TestCase):
    def setUp(self):
        self.unorderedData = []
        maxValue = 100
        for i in range(maxValue):
            self.unorderedData.append(random.randint(1, maxValue))
        self.orderedData = copy.copy(self.unorderedData)
        self.orderedData.sort()

    def test_bubbles(self):
        self.assertNotEqual(self.unorderedData, self.orderedData)
        search.sortBubbles(self.unorderedData)
        self.assertEqual(self.unorderedData, self.orderedData)
    def test_Forward(self):
        self.assertNotEqual(self.unorderedData, self.orderedData)
        search.sortSimple(self.unorderedData)
        self.assertEqual(self.unorderedData, self.orderedData)    
    def test_ByInsert(self):
        self.assertNotEqual(self.unorderedData, self.orderedData)
        search.sortByInsert(self.unorderedData)
        self.assertEqual(self.unorderedData, self.orderedData)    
    def test_Quick(self):
        self.assertNotEqual(self.unorderedData, self.orderedData)
        self.assertEqual(search.quickSort(self.unorderedData), self.orderedData)    


class TestGraphWithoutWeighModule(unittest.TestCase):
    def setUp(self):
        self.data={}
        self.data["d0"] = ["d1", "d2", "d3"]
        self.data["d1"] = ["d11", "d12", "d13", "d0"]
        self.data["d2"] = ["d21", "d22", "d23"]
        self.data["d3"] = ["d31", "d32", "d33"]
        self.data["d11"] = []
        self.data["d12"] = []
        self.data["d13"] = []
        self.data["d21"] = []
        self.data["d22"] = []
        self.data["d23"] = []
        self.data["d31"] = []
        self.data["d32"] = []
        self.data["d33"] = []
    def test_extendSearch_Simple(self):
        self.assertEqual(graph.extendSearch(self.data, "d0", "d13"), ["d0", "d1", "d13"])
        self.assertEqual(graph.extendSearch(self.data, "d0", "d33"), ["d0", "d3", "d33"])
        self.assertEqual(graph.extendSearch(self.data, "d0", "d12"), ["d0", "d1", "d12"])
        self.assertEqual(graph.extendSearch(self.data, "d1", "d33"), ["d1", "d0", "d3", "d33"])
        self.assertEqual(graph.extendSearch(self.data, "d2", "d23"), ["d2", "d23"])

        
        
if __name__ == "__main__":
    unittest.main()
