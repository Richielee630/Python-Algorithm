# 1. selection sort
# 2. insertion sort
# 3. shell sort
# 4. heap sort
# 5. merge sort
# 6. quick sort

import time
import random


# import matplotlib.pyplot as plt

class Sorting(object):
    """Sorting class

    """

    def __init__(self):
        self.id = []

    def sort_init(self, N):
        """initialize the data structure

        """

        try:
            self.id = random.sample(range(1, N ** 3), N)
        except ValueError:
            print('Sample size exceeded population size.')

        self.id = [random.randint(0, N - 1) for i in range(N)]

    def get_id(self):
        """initialize the data structure

        """

        return self.id

    def selection_sort(self):
        """Selection sort algorithm is an
        in-place comparison sort. It has O(n^2) time complexity, making it
        inefficient on large lists, and generally performs worse than the
        similar insertion sort

        """
        for i_idx, i_item in enumerate(self.id):
            min = i_idx

            for j_idx in range(i_idx + 1, len(self.id)):

                if (self.id[j_idx] < self.id[min]):
                    min = j_idx

            # swap
            temp = self.id[i_idx]
            self.id[i_idx] = self.id[min]
            self.id[min] = temp

        return self.id

    def insertion_sort(self):
        """Insertion sort is a simple sorting algorithm that builds the final
        sorted array (or list) one item at a time. More efficient in practice
        than most other simple quadratic (i.e., O(n^2)) algorithms such as
        selection sort or bubble sort specifically an

        """

        for i_idx, i_item in enumerate(self.id):
            pos = i_idx
            while pos > 0 and self.id[pos] < self.id[pos - 1]:
                tmp = self.id[pos]
                self.id[pos] = self.id[pos - 1]
                self.id[pos - 1] = tmp
                pos -= 1
        return self.id

    def shell_sort2(self, span):
        for i in range(span):
            j = i
            while j < len(self.id):
                k = j
                while k - span >= 0 and self.id[k] < self.id[k - span]:
                    tmp = self.id[k]
                    self.id[k] = self.id[k - span]
                    self.id[k - span] = tmp
                    k = k - span
                j += span

    def shell_sort(self):
        """Shell sort also known as  or Shell's method, is an in-place comparison sort.
        It can be seen as either a generalization of sorting by exchange (bubble sort)
        or sorting by insertion (insertion sort).

        """
        span = (len(self.id) + 1) / 2
        while span >= 1:
            self.shell_sort2(int(span))
            span /= 2
        return self.id

    def heap_sort(self):
        """Heapsort is an improved selection sort: it divides its input into a sorted
        and an unsorted region, and it iteratively shrinks the unsorted region by
        extracting the largest element and moving that to the sorted region.

        """
        for i in range(len(self.id)):
            nr = (i + 1) * 2
            nl = nr - 1
            if nl < len(self.id) and self.id[i] < self.id[nl]:
                tmp = self.id[i]
                self.id[i] = self.id[nl]
                self.id[nl] = tmp
                j = i
                while j != 0 and self.id[j] > self.id[int((j - 1) / 2)]:
                    tmp = self.id[j]
                    self.id[j] = self.id[int((j - 1) / 2)]
                    self.id[int((j - 1) / 2)] = tmp
                    j = int((j - 1) / 2)
            if nr < len(self.id) and self.id[i] < self.id[nr]:
                tmp = self.id[i]
                self.id[i] = self.id[nr]
                self.id[nr] = tmp
                j = i
                while j != 0 and self.id[j] > self.id[int((j - 1) / 2)]:
                    tmp = self.id[j]
                    self.id[j] = self.id[int((j - 1) / 2)]
                    self.id[int((j - 1) / 2)] = tmp
                    j = int((j - 1) / 2)
        p = len(self.id) - 1
        while p > 0:
            tmp = self.id[p]
            self.id[p] = self.id[0]
            self.id[0] = tmp
            i = 0
            while i < p:
                nr = (i + 1) * 2
                nl = nr - 1
                j = i
                if nr < p and self.id[nr] > self.id[nl]:
                    if self.id[nr] < self.id[i]:
                        break
                    tmp = self.id[i]
                    self.id[i] = self.id[nr]
                    self.id[nr] = tmp
                    i = nr
                elif nl < p and self.id[nl] > self.id[i]:
                    tmp = self.id[i]
                    self.id[i] = self.id[nl]
                    self.id[nl] = tmp
                    i = nl
                else:
                    break
                while j != 0 and self.id[j] > self.id[int((j - 1) / 2)]:
                    tmp = self.id[j]
                    self.id[j] = self.id[int((j - 1) / 2)]
                    self.id[int((j - 1) / 2)] = tmp
                    j = int((j - 1) / 2)
            p = p - 1

        return 1

    def merge_sort(self):
        """Merge sort is a divide and conquer algorithm that was invented
        by John von Neumann in 1945. Most implementations produce a stable
        sort, which means that the implementation preserves the input order
        of equal elements in the sorted output.
        """
        self.merge_sort2(0, len(self.id))
        return self.id

    def quick_sort(self):
        """Quicksort (sometimes called partition-exchange sort) is an efficient
        sorting algorithm. Developed by Tony Hoare in 1959. It is still a commonly
        used algorithm for sorting. When implemented well, it can be about two or
        three times faster than its main competitors, merge sort and heapsort.

        """

        return 1


    # this plots things in log scale (pls google it), you need to add matplotlib
    # to your virtualenv first!

    # plot also python's sorted() function to see how well you do.


    # plt.plot(set_szs, timing)
    # plt.xscale('log')
    # plt.yscale('log')
    # plt.title('log')
    # plt.ylabel('some numbers')
    # plt.show()