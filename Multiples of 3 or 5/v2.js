function solution(number) {
  function sumMultiples(n, limit) {
    const p = Math.floor((limit - 1) / n);
    return (n * p * (p + 1)) / 2;
  }
  if (number <= 2) return 0;
  return (
    sumMultiples(3, number) + sumMultiples(5, number) - sumMultiples(15, number)
  );
}
