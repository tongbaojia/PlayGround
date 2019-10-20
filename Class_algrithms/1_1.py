# http://www.marinamele.com/third-grade-karatsuba-multiplication-algorithms
# 3141592653589793238462643383279502884197169399375105820974944592
# 2718281828459045235360287471352662497757247093699959574966967627

# aws: 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184

a = 3141592653589793238462643383279502884197169399375105820974944592
b = 2718281828459045235360287471352662497757247093699959574966967627
import time

def k_multiply(x, y, base=10):
    # Calculate the number of digits of the numbers
    if x > base and y > base:
        # Split the digit sequences about the middle
        sx, sy = str(x), str(y)
        m = max(len(sx), len(sy)) // 2
        ix, iy = len(sx) - m, len(sy) - m
        x0, x1 = int(sx[:ix]), int(sx[ix:])
        y0, y1 = int(sy[:iy]), int(sy[iy:])
        # m = max(len(str(x)), len(str(y))) // 2
        # x1 = x // (base ** m)
        # x0 = x % (base ** m)
        # y1 = y // (base ** m)
        # y0 = y % (base ** m)

        z2 = k_multiply(x1, y1)
        z0 = k_multiply(x0, y0)
        z1 = k_multiply(x1 + x0, y1 + y0)
        xy = z2 * base ** (2 * m) + (z1 - z2 - z0) * base ** m + z0
        return xy
    else:
        return x*y

print(k_multiply(10**6, 10**6))
start = time.time()
print(k_multiply(a, b))
end = time.time()
print("k_mul: -->", end - start)
start = time.time()
print(k_multiply(a, b))
end = time.time()
print("k_mul: -->", end - start)
start = time.time()
print(a * b)
end = time.time()
print("built in: -->", end - start)