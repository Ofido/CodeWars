use std::collections::HashMap;

fn scissors(p2: &str) -> bool {
    p2 == "paper"
}

fn paper(p2: &str) -> bool {
    p2 == "rock"
}

fn rock(p2: &str) -> bool {
    p2 == "scissors"
}

fn rps(p1: &str, p2: &str) -> &'static str {
    let mut hi: HashMap<&str, fn(&str) -> bool> = HashMap::new();

    hi.insert("scissors", scissors);
    hi.insert("paper", paper);
    hi.insert("rock", rock);

    if p1 == p2 {
        "Draw!"
    } else {
        // if hi.get(p1)(p2) { por que isso não funciona?
        if hi.get(p1).unwrap()(p2) {
            "Player 1 won!"
        } else {
            "Player 2 won!"
        }
    }
}
