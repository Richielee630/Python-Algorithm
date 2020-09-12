
# 1. quick-find
# 2. quick-union
# 3. weighted QU
# 4. QU + path compression
# 5. weighted QU + path compression

import time
import random
from math import log
import matplotlib.pyplot as plt

class UF(object):
    """Union Find class

    """

    def __init__(self):
        self.id = []
        self.sz = []

    def qf_init(self, N):
        """initialize the data structure

        """
        for x in range(N):
            self.id.append(x)
            self.sz.append(1)

    def qf_union(self, p, q):
        """Union operation for Quick-Find Algorithm.

        connect p and q. You need to
        change all entries with id[p] to id[q]
        (linear number of array accesses)

        """

        if self.qf_connected(p ,q):
            return True

        pid = self.id[p]
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = self.id[q]
        return True


    def qf_connected(self, p, q):
        """Find operation for Quick-Find Algorithm.
        simply test whether p and q are connected

        """
        return self.id[p] == self.id[q]



    def qu_union(self, p, q):
        """Union operation for Quick-Union Algorithm.
         connect p and q.

         """

        if self.qu_connected(p ,q):
            return True

        p_pa ,q_pa = p ,q
        while p_pa != self.id[p_pa]:
            p_pa = self.id[p_pa]
        while q_pa != self.id[q_pa]:
            q_pa = self.id[q_pa]
        self.id[p_pa] = q_pa

        return True


    def qu_connected(self, p, q):
        """Find operation for Quick-Union Algorithm.
         test whether p and q are connected

         """
        p_pa ,q_pa = p ,q
        while p_pa != self.id[p_pa]:
            p_pa = self.id[p_pa]
        while q_pa != self.id[q_pa]:
            q_pa = self.id[q_pa]

        return  p_pa == q_pa


    def wqu_union(self, p, q):
        """Union operation for Weighted Quick-Union Algorithm.
         connect p and q.

         """

        if self.wqu_connected(p ,q):
            return True

        p_pa ,q_pa = p ,q
        while p_pa != self.id[p_pa]:
            p_pa = self.id[p_pa]
        while q_pa != self.id[q_pa]:
            q_pa = self.id[q_pa]

        if self.sz[p_pa] >= self.sz[q_pa]:
            self.id[q_pa] = p_pa
            self.sz[p_pa] += self.sz[q_pa]
        else:
            self.id[p_pa] = q_pa
            self.sz[q_pa] += self.sz[p_pa]
        return True


    def wqu_connected(self, p, q):
        """Find operation for Weighted Quick-Union Algorithm.
         test whether p and q are connected

         """

        return self.qu_connected(p ,q)


    def pqu_union(self, p, q):
        """Union operation for path compressed Quick-Union Algorithm.
         connect p and q.

        """
        if self.pqu_connected(p ,q):
            return True
        self.id[self.id[p]] = self.id[q]
        return True


    def pqu_connected(self, p, q):
        """Find operation for path compressed Quick-Union Algorithm.
         test whether p and q are connected

         """
        p_pa ,q_pa = [p] ,[q]
        while p_pa[-1] != self.id[p_pa[-1]]:
            p_pa.append(self.id[p_pa[-1]])
        while q_pa[-1] != self.id[q_pa[-1]]:
            q_pa.append(self.id[q_pa[-1]])
        for idx in p_pa:
            self.id[idx] = p_pa[-1]
        for idx in q_pa:
            self.id[idx] = q_pa[-1]
        return self.id[p ]= =self.id[q]

    def wpqu_union(self, p, q):
        """Union operation for Weighted path compressed Quick-Union Algorithm.
         connect p and q.

         """
        if self.wpqu_connected(p ,q):
            return True;

        p_pa ,q_pa = self.id[p] ,self.id[q]

        if self.sz[p_pa] >= self.sz[q_pa]:
            self.id[q_pa] = p_pa
            self.sz[p_pa] += self.sz[q_pa]
        else:
            self.id[p_pa] = q_pa
            self.sz[q_pa] += self.sz[p_pa]
        return True


    def wpqu_connected(self, p, q):
        """Find operation for Weighted path compressed Quick-Union Algorithm.
         test whether p and q are connected

         """

        return self.pqu_connected(p ,q)

if __name__ == "__main__":

    # iteration
    set_szs = [1e1 ,1e2 ,1e3 ,1e4 ,1e5 ,1e6]
    timing = []

    # gives the timing for union operation only, you might want to do this for all functions you wrote.
    for set_sz in set_szs:
        # initialize network nodes
        set_sz = int(set_sz)
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

            inodes.wpqu_union(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)

        print(total_time)

    # this plots things in log scale (pls google it), you need to add matplotlib to your virtualenv first!
    plt.plot(set_szs, timing)
    plt.xscale('log')
    plt.yscale('log')
    plt.title('log')
    plt.ylabel('some numbers')
    plt.show()
