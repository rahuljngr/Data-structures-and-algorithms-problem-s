def mySqrt(self, n: int) -> int:
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