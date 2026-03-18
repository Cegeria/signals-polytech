import itertools

def check_hamming_dual(r):
    n = 2**r - 1
    columns = []
    for val in range(1, 2**r):
        bits = [(val >> i) & 1 for i in range(r)]
        columns.append(bits)
    assert len(columns) == n

    expected_weight = 2**(r-1)
    for a_tuple in itertools.product([0, 1], repeat=r):
        if all(x == 0 for x in a_tuple):
            continue
        word = []
        for col in columns:
            bit = sum(a_tuple[i] * col[i] for i in range(r)) % 2
            word.append(bit)
        weight = sum(word)
        if weight != expected_weight:
            print(f"error: for a={a_tuple} weight {weight} != {expected_weight}")
            return False
    print(f"r={r}: length {n}, dim {r}, weights {expected_weight}")
    return True

for r in range(2, 6):
    if not check_hamming_dual(r):
        break
else:
    print("Check completed")
