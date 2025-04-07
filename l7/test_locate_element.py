import unittest
#from l7.locate_element import locate_element_linear as locate_element
from l7.locate_element import locate_element


class LocateElementTestCase(unittest.TestCase):
    def setUp(self):
        self.test_case = [{
            "in": {
                "elements": [3, 2, 1],
                "query": 2
            },
            "out": 1
        }, {
            "in": {
                "elements": [13, 12, 11, 8, 6, 5, 3, 2, 0],
                "query": 8
            },
            "out": 3
        }, {
            "in": {
                "elements": [9, 7, 5, -1],
                "query": 6
            },
            "out": -1
        }, {
            "in": {
                "elements": [],
                "query": 2
            },
            "out": -1
        }, {
            "in": {
                "elements": [8, 8, 6, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
                "query": 6
            },
            "out": 2
        }]

    def test_locate_element(self):
        for case in self.test_case:
            actual = locate_element(case["in"]["elements"], case["in"]["query"])
            self.assertEqual(actual, case["out"], msg=f"{case}; Actual: {actual}")


if __name__ == '__main__':
    unittest.main()
