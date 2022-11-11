export const digitalRoot = (n:number):number => {
    var tot:number = 0
    n.toString().split('').forEach((a) => tot = tot + Number(a))
    return tot
  };