import copy
import random
from lib.hw3.search_trees import Array_Search
from lib.hw3.search_trees import BST
from lib.hw3.search_trees import RBBST


class Test_Search(object):
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""
        print("\n#####  Start Function Tests   #####\n")

    def test_one(self):
        pass

    def test_two(self):
        expected = (1, 2, 3)
        actual = (1, 2, 3)
        assert expected == actual

    def test_sequential_search_0(self):

        # initialize testbed
        set_sz = 10
        vals = random.sample(range(1, 100), set_sz)
        op_under_test = Array_Search(vals)

        # python search result
        key = vals[9]
        expected = vals.index(key)

        actual = op_under_test.squential_search(key)

        assert expected == actual


    def test_rbbst_0(self):

        # initialize testbed
        set_sz = 10
        op_under_test = RBBST()

        vals = random.sample(range(1, 100), set_sz)

        for idx in range(set_sz - 1):
            op_under_test.insert(vals[idx])

        # python search result
        key = vals[9]
        expected = vals.index(key)

        actual = op_under_test.bsearch(key)

        assert expected == actual

        # initialize testbed
        op_under_test = BST()
        op_under_test.init_bst(10)

        expected = sorted(op_under_test.get_id())

        actual = op_under_test.bsearch()

        assert expected == actual