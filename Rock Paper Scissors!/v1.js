const scissors = (p2) => {
  return p2 == "paper";
};

const paper = (p2) => {
  return p2 == "rock";
};

const rock = (p2) => {
  return p2 == "scissors";
};

const change_p1 = (p1) => {
  if (p1 === "scissors") return scissors;
  if (p1 === "paper") return paper;
  if (p1 === "rock") return rock;
};

const rps = (p1, p2) => {
  if (p1 === p2) {
    return "Draw!";
  } else {
    if (change_p1(p1)(p2)) {
      return "Player 1 won!";
    }
    return "Player 2 won!";
  }
};
