const reverse = (str: string): string => str.split("").reverse().join("")

export const reverseWords = (str: string): string => str.split(' ').map(reverse).join(" ")
