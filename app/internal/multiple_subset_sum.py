from app.models.inputpayload import InputPayload

# Recursive calculation of the subset sum problem

def subset_sum_recursive(inputpayload: InputPayload, index_a=0, index_b=0):
    
    list_a = inputpayload.list_a
    list_b = inputpayload.list_b
    target = inputpayload.target
    
    # Base cases
    if target == 0:
        return True
    if index_a >= len(list_a) + len(list_b) or target <0:
        return False
    
    # If one of the elements in the list contain the target
    if target == list_a[index_a] or target == list_b[index_b]:
        return True

    # If each element of index added with each element of b equals the target return true
    if target == list_a[index_a] + list_b[index_b]:
        return True
    
    # If you reached the end of each list return false
    if index_b == len(list_b)-1 and index_a == len(list_a)-1:
        return False
    
    if index_b <= len(list_b):
        index_b += 1
        
    if index_b >= len(list_b) and index_a <= len(list_a):
        index_b = 0
        index_a += 1
 
    return subset_sum_recursive(inputpayload, index_a, index_b)