def pretty_print(board):
    pretty_sol = ""
    for i, s in enumerate(board):
        pretty_sol += f"| ({i}) {s.upper()} "
        if ((i + 1) % 3) == 0:
            pretty_sol += "|\n"
    return pretty_sol
