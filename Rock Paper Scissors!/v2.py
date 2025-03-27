play = {
    "scissors": lambda p2: p2 == "paper",
    "paper": lambda p2: p2 == "rock",
    "rock": lambda p2: p2 == "scissors",
}


def rps(p1, p2) -> str:
    if p1 == p2:
        return "Draw!"
    if play[p1](p2):
        return "Player 1 won!"
    return "Player 2 won!"
