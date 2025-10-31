def alldiff(n_ary: list[int], C: dict[int, list[int]]) -> None:
    """Convert alldiff constraint to C constraints, append to Constraint Graph.
    All constraints here are variable indexes.

    Args:
        n_ary (list[int]): Alldiff constraint values
        C (dict[int, list[int]]): Binary constraint dictionary
    """
    for i in n_ary:
        for j in n_ary:
            if i == j:
                continue
            else:
                if j not in C[i]:
                    C[i].append(j)
    return