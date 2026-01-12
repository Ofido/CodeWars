function narcissistic(value) {
  if (value < 10) return true;
  let valor = String(value).split("");
  let tamanho = valor.length;
  let comp = 0;
  for (const e of valor) {
    console.log("e ${e}" + e);
    comp += Number(e) ** tamanho;
    console.log("comp ${comp}" + comp);
  }
  return comp == value;
}
