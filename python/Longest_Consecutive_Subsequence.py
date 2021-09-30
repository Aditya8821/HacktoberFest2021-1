def findMaxLenSubseq(A):
    s=set(A)
    maxlength=0
    for i in A:
        if i-1 not in s:
            len=1
            while i+len in s:
                len+=1
            maxlength=max(maxlength,len)
    return maxlength
A = [2, 0, 6, 1, 5, 3, 7]
print("The length of the maximum consecutive subsequence is:",findMaxLenSubseq(A))