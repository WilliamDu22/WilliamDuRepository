import random


def name(n, k):
  if n <= 1:
    return 1
  return n * name(n - k, k)


def test():
  n = random.randint(0, 750)
  k = random.randint(0, 900)
  print(f"{n}!({k}) =", name(n, k))
  n = random.randint(0, 750)
  k = random.randint(0, 900)
  print(f"{n}!({k}) =", name(n, k))
  n = random.randint(0, 750)
  k = random.randint(0, 900)
  print(f"{n}!({k}) =", name(n, k))


def run():
  try:
    n = int(input("What multifactorial? "))
    k = int(input("How many steps? "))
    if n > 750 or n < 0:
      print("input a number between 0 and 750")
    elif k < 0:
      print("input a number greater than 0")
    else:
      print(f"{n}!({k}) =", name(n, k))
  except:
    print("integer")
