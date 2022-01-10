def sqrtN(n):
    s = 0
    e = n
    ans = 0
    while (s<=e):
        mid = int(s+(e-s)/2)
        square = mid*mid
        if square == n:
            return mid
        if square<n:
            ans = mid
            s = mid+1
        else:
            e = mid-1
    return ans

def morePrecision(n,precision,tempsol):
    factor = 1
    ans = float(tempsol)
    for i in range(0,precision):
        factor = factor/10
        for j in range(ans):
            if j*j < n:

                j = j + factor
                ans =j 
    return ans

n = int(input("Enter No."))      
tempsol = sqrtN(n)
print(tempsol)
