def scissors(p2):
    return p2 == "paper"


def paper(p2):
    return p2 == "rock"


def rock(p2):
    return p2 == "scissors"


play = {
    "scissors": scissors,
    "paper": paper,
    "rock": rock,
}


def rps(p1, p2) -> str:
    if p1 == p2:
        return "Draw!"
    if play[p1](p2):
        return "Player 1 won!"
    return "Player 2 won!"
