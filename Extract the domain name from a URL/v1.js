function domainName(url) {
  let a = url
  a = a.split("://")
  if (a.length == 1) {
    a = a[0]
  } else {
    a = a[1]
  }
  a = a.split(".")
  if (a[0].startsWith("w")) {
    a = a[1]
  } else {
    a = a[0]
  }
  return a
}
