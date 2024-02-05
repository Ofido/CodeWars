fn square_sum(vec: Vec<i32>) -> i32 {
    let mut output: i32 = 0;
    for num in vec.iter() {
        output += num.pow(2);
    }
    // return output;
    // why return its not req????????
    output
}

fn square_sum_2(vec: Vec<i32>) -> i32 {
    vec.iter().map(|s| s * s).sum()
}

fn square_sum_3(vec: Vec<i32>) -> i32 {
    vec.iter().fold(0, |t, i| t + i * i)
}

fn square_sum_4(vec: Vec<i32>) -> i32 {
    vec.iter().map(|v| v.pow(2)).sum()
}

#[test]
fn returns_expected() {
    assert_eq!(square_sum(vec![1, 2]), 5);
    assert_eq!(square_sum(vec![-1, -2]), 5);
    assert_eq!(square_sum(vec![5, 3, 4]), 50);
    assert_eq!(square_sum(vec![]), 0);
}
