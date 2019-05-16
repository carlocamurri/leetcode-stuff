class Solution:

    def max_chunks_to_make_sorted(self, arr):
        count = 0
        index_to_end_chunk = 0
        for i, val in enumerate(arr):
            index_to_end_chunk = max(index_to_end_chunk, arr[i])
            if i == index_to_end_chunk:
                count += 1
        return count
