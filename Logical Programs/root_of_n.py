def square_root(x, precision=1e-6):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")

    low = 0
    high = max(1.0, x)
    mid = (low + high) / 2

    while abs(mid * mid - x) > precision:
        if mid * mid < x:
            low = mid
        else:
            high = mid
        mid = (low + high) / 2

    return round(mid, 6)

print(square_root(25))     

print(square_root(2))      

print(square_root(0.04))   

