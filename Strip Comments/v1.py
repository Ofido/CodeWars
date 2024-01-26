def strip_comments(string: str, markers: list[str]):
    output = ""
    for line in string.splitlines():
        if idx := [
            line.find(marker) for marker in markers if line.find(marker) != -1
        ]:
            output += line[: min(idx)].rstrip()
        else:
            output += line.rstrip()
        output += "\n"
    return output[:-1]


if __name__ == "__main__":
    test_1 = strip_comments(
        "apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]
    )
    answer_test_1 = "apples, pears\ngrapes\nbananas"
    print(f"test_1: {test_1}")
    print(f"len(test_1): {len(test_1)}")
    print(f"answer_test_1: {answer_test_1}")
    print(f"len(answer_test_1): {len(answer_test_1)}")
    print(f"test_1 == answer_test_1: {test_1 == answer_test_1}")
    assert test_1 == answer_test_1  # nosec

    test_2 = strip_comments("a #b\nc\nd $e f g", ["#", "$"])
    answer_test_2 = "a\nc\nd"
    print(f"test_2: {test_2}")
    print(f"len(test_2): {len(test_2)}")
    print(f"answer_test_2: {answer_test_2}")
    print(f"len(answer_test_2): {len(answer_test_2)}")
    print(f"test_2 == answer_test_2: {test_2 == answer_test_2}")
    assert test_2 == answer_test_2  # nosec

    test_3 = strip_comments(" a #b\nc\nd $e f g", ["#", "$"])
    answer_test_3 = " a\nc\nd"
    print(f"test_3: {test_3}")
    print(f"len(test_3): {len(test_3)}")
    print(f"answer_test_3: {answer_test_3}")
    print(f"len(answer_test_3): {len(answer_test_3)}")
    print(f"test_3 == answer_test_3: {test_3 == answer_test_3}")
    assert test_3 == answer_test_3  # nosec
