export function comp(a1: number[] | null, a2: number[] | null): boolean {
    if (a1 === null || a2 === null) return false
    a1!.sort()
    a2!.sort()
    const a1e:number[] = a1!.map((e) => e*e)
    // const a2e:number[] = a2!.map((e) => e*e)
    // if (a1.filter((e, i) => e === a2e[i]).length === a1.length) return true
    if (a2.filter((e, i) => e === a1e[i]).length === a2.length) return true
    return false;
}