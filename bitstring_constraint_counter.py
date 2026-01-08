def next(bitstrings, max_constraint=0, constraints=[]):
    new_bitstrings = []
    for b in bitstrings:
        illegal0=False
        illegal1=False
        for c in constraints:
            cut = b[(-len(c)+1):]
            if cut+"0" == c:
                illegal0=True
            if cut+"1" == c:
                illegal1=True
        if not illegal0: new_bitstrings.append(b+"0")
        if not illegal1: new_bitstrings.append(b+"1")
    return new_bitstrings
        
def get_x(n, constraints=[]):
    MAX_LENGTH_CONSTRAINT=0
    if len(constraints) > 0:
        MAX_LENGTH_CONSTRAINT = max([len(c) for c in constraints])
    bs = [""]
    for i in range(n):
        bs = next(bs, max_constraint=MAX_LENGTH_CONSTRAINT, constraints=constraints)
    return bs
    
for i in range(10):
    print(f"x_{i}={len(get_x(i, constraints=["000", "11"]))}")
    