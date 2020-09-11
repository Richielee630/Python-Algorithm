
import lib.hw1.union_find

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

    def test_qf_not_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # test if (1, 2) is connected
        actual = inodes.qf_connected(1, 2)

        expected = False

        assert expected == actual

    def test_qf_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # connect (1, 2)
        inodes.qf_union(1, 2)

        # test if (1, 2) is connected
        actual = inodes.qf_connected(1, 2)

        expected = True

        assert expected == actual

    def test_qu_not_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # test if (1, 2) is connected
        actual = inodes.qu_connected(1, 2)

        expected = False

        assert expected == actual

    def test_qu_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # connect (1, 2)
        inodes.qu_union(1, 2)

        # test if (1, 2) is connected
        actual = inodes.qu_connected(1, 2)

        expected = True

        assert expected == actual


    def test_wqu_not_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # test if (1, 2) is connected
        actual = inodes.wqu_connected(1, 2)

        expected = False

        assert expected == actual

    def test_wqu_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # connect (1, 2)
        inodes.wqu_union(1, 2)

        # test if (1, 2) is connected
        actual = inodes.wqu_connected(1, 2)

        expected = True

        assert expected == actual


    def test_pqu_not_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # test if (1, 2) is connected
        actual = inodes.pqu_connected(1, 2)

        expected = False

        assert expected == actual

    def test_pqu_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # connect (1, 2)
        inodes.pqu_union(1, 2)

        # test if (1, 2) is connected
        actual = inodes.pqu_connected(1, 2)

        expected = True

        assert expected == actual

    def test_wpqu_not_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # test if (1, 2) is connected
        actual = inodes.wpqu_connected(1, 2)

        expected = False

        assert expected == actual

    def test_wpqu_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # connect (1, 2)
        inodes.wpqu_union(1, 2)

        # test if (1, 2) is connected
        actual = inodes.wpqu_connected(1, 2)

        expected = True

        assert expected == actual