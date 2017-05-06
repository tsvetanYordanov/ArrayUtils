class ArraySplitterUtil:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        return "Array splitter: " % self.array

    def split_array(self, num_of_splits):
        arr = self.array
        array_len = len(arr)
        arr_remainder = (array_len % num_of_splits)
        arr_quotient = array_len / num_of_splits
        result = []
        remainder_arr = []
        print "num of splits required: " + str(num_of_splits)
        print "input is: " + str(arr)
        if arr_remainder > 0:
            remainder_arr = arr[-arr_remainder:]
            num_of_splits -= 1
            array_len -= arr_remainder
            arr_quotient = array_len / num_of_splits

        for i in range(num_of_splits):
            curr_split = arr[i * arr_quotient:i * arr_quotient + arr_quotient]
            print "curr split is: " + str(curr_split)
            result.append(curr_split)
        if arr_remainder > 0:
            result.append(remainder_arr)
        print "resulting split is: " + str(result)
        return result
