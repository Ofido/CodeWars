def reverse_words(text:str):
  return ' '.join([a[::-1] for a in text.split(' ')])