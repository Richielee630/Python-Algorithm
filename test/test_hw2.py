
import copy
from lib.hw2.sorting import Sorting

class Test_UF(object):
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""
        print ("\n#####  Start Function Tests   #####\n")

    def test_one(self):
        pass

    def test_two(self):
        expected = (1, 2, 3)
        actual = (1, 2, 3)
        assert expected == actual

    def test_selection_sort_0(self):

        # initialize testbed
        arr_under_test = Sorting()
        arr_under_test.sort_init(10)

        # test against built in python sorted() function.
        #expected = sorted(copy.deepcopy(arr_under_test.get_id()))
        expected = sorted(arr_under_test.get_id())

        actual = arr_under_test.selection_sort()

        assert expected == actual


    def test_insertion_sort_0(self):
       
        # initialize testbed
        arr_under_test = Sorting()
        arr_under_test.sort_init(10)

        expected = sorted(arr_under_test.get_id())

        actual = arr_under_test.insertion_sort()

        assert expected == actual

    def test_shell_sort_0(self):


        # initialize testbed
        arr_under_test = Sorting()
        arr_under_test.sort_init(10)

        expected = sorted(arr_under_test.get_id())

        actual = arr_under_test.shell_sort()

        assert expected == actual


    def test_heap_sort_0(self):


        # initialize testbed
        arr_under_test = Sorting()
        arr_under_test.sort_init(10)

        expected = sorted(arr_under_test.get_id())

        actual = arr_under_test.heap_sort()

        assert expected == actual

    def test_merge_sort_0(self):


        # initialize testbed
        arr_under_test = Sorting()
        arr_under_test.sort_init(10)

        expected = sorted(arr_under_test.get_id())

        actual = arr_under_test.merge_sort()

        assert expected == actual


    def test_quick_sort_0(self):


        # initialize testbed
        arr_under_test = Sorting()
        arr_under_test.sort_init(10)

        expected = sorted(arr_under_test.get_id())

        actual = arr_under_test.quick_sort()

        assert expected == actual


