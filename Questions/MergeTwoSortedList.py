class MergeTwoList:
    def mergeSortedList(self, l1 : list, l2 : list) -> list:
        result = []
        i = j = 0

        l1_len = len(l1) 
        l2_len = len(l2)

        while i< l1_len and j< l2_len:
            if l1[i] < l2[j]:
                result.append(l1[i])
                i += 1
            else:
                result.append(l2[j])
                j += 1 
        
        if i< l1_len:
            result.extend(l1[i:])

        if j< l2_len:
            result.extend(l2[j:])

        return result

l1 = [1,2,4]
l2 = [1,3,4]

obj = MergeTwoList()

out = obj.mergeSortedList(l1, l2)
print(out)



