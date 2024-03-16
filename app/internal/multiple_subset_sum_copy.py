from app.models.inputpayload import InputPayload

# Recursive calculation of the subset sum problem

class MultipleSubsetSum:
    
    def __init__(self, list_a, list_b, target):
        self.list_a = list_a
        self.list_b = list_b
        self.target = target

    def recursive(self, index_a=0, index_b=0):
        
        # Base cases
        if self.target == 0:
            return True
        if index_a >= len(self.list_a) + len(self.list_b) or self.target <0:
            return False
        
        # If one of the elements in the list contain the target
        if self.target == self.list_a[index_a] or self.target == self.list_b[index_b]:
            return True

        # If each element of index added with each element of b equals the target return true
        if self.target == self.list_a[index_a] + self.list_b[index_b]:
            return True
        
        # If you reached the end of each list return false
        if index_b == len(self.list_b)-1 and index_a == len(self.list_a)-1:
            return False
        
        if index_b <= len(self.list_b):
            index_b += 1
            
        if index_b >= len(self.list_b) and index_a <= len(self.list_a):
            index_b = 0
            index_a += 1
    
        return self.recursive(index_a, index_b)