function solution(number) {
  let a = 0;
  for (let index = 1; index < number; index++) {
    if (index % 3 === 0 || index % 5 === 0) {
      a += index;
    }
  }
  return a;
}
