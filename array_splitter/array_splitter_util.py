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
        if arr_remainder > 0:
            # If there is a remainder in the division
            # then store the last remainder number of elements
            # in remainder_arr, decrease the number of splits
            # and recalculate the quotient
            remainder_arr = arr[-arr_remainder:]
            num_of_splits -= 1
            array_len -= arr_remainder
            arr_quotient = array_len / num_of_splits
        # split original array to equal-sized arrays
        # where each will be of size equal to the quotient
        for i in range(num_of_splits):
            curr_split = arr[i * arr_quotient:i * arr_quotient + arr_quotient]
            result.append(curr_split)
        # add the remainder_arr as the last if there is one
        if arr_remainder > 0:
            result.append(remainder_arr)
        return result
