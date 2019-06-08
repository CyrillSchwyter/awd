class BubbleSort:

    @staticmethod
    def sort(a: list):
        for k in range(len(a) - 1, 0, -1):
            for i in range(k):
                if a[i] > a[i + 1]:
                    temp = a[i]
                    a[i] = a[i + 1]
                    a[i + 1] = temp


class MergeSort:

    def sort(self, arr: list):
        return self.sort_int(arr)

    def sort_int(self, arr: list):
        size = len(arr)
        if size <= 1:
            return arr

        mid: int = int(size / 2)
        re = self.sort_int(arr[:mid])
        le = self.sort_int(arr[mid:])
        return self.merge(re, le)

    @staticmethod
    def merge(r: list, l: list):

        res: list = []
        # merge
        while len(r) > 0 and len(l) > 0:

            if r[0] < l[0]:
                res.append(r[0])
                del r[0]
            else:
                res.append(l[0])
                del l[0]

        if len(r) > 0:
            res.extend(r)

        if len(l) > 0:
            res.extend(l)

        return res
