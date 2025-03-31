import time

MOD = 10**9 + 7
base = 5000
exp = 10**6  # Large exponent

# Using normal exponentiation (inefficient)
start = time.time()
result1 = (base ** exp) % MOD  # Very slow
end = time.time()
print(f"Using **: {end - start:.5f} seconds")

# Using pow() with mod (efficient)
start = time.time()
result2 = pow(base, exp, MOD)  # Fast
end = time.time()
print(f"Using pow(): {end - start:.5f} seconds")

# Verify both methods give the same result
print(result1 == result2)  # True
