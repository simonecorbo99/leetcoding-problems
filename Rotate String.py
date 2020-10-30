class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        
        def rotate(L, n):
            return L[n:]+L[:n]
        
        if A == B == "":
            return True
        if not len(A) == len(B):
            return False
        for l in A:
            for i in range(len(B)):
                if l == B[i]:
                    R = rotate(A, i)
                    if R==B:
                        return True
        
        return False
