from collections import OrderedDict


class Solution:

    def contains_duplicate_iii(self, nums, max_dist_between_indices, max_dist_between_values):
        if not max_dist_between_indices:
            return False
        odict = OrderedDict()
        for num in nums:
            bucket = num if not max_dist_between_values else num // max_dist_between_values
            for b in (bucket - 1, bucket, bucket + 1):
                # print("b: {}, value stored: {}, num: {}".format(b, odict.get(b, 'no value'), num))
                if odict.get(b) is not None and abs(num - odict[b]) <= max_dist_between_values:
                    return True
            if len(odict) == max_dist_between_indices:
                odict.popitem(last=False)
            odict[bucket] = num
        return False
