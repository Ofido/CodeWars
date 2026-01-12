function narcissistic(value) {
  const digits = String(value).split("");
  const tamanho = digits.length;
  const soma = digits.reduce((acc, d) => acc + Number(d) ** tamanho, 0);
  return soma === value;
}
