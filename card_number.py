import random
t= random.randint(1000000000000000,9999999999999999)

def check_card_number(s):
   def f(i,c):
      if i % 2 == 0: return c
      t = c * 2
      if t > 9: t -= 9
      return t

   lst = [f(i,int(c)) for i,c in enumerate(reversed(s))]
   return sum(lst) % 10 == 0

if __name__ == '__main__':
   print(check_card_number('5082337440657928'))
   print(check_card_number('4601496706376197'))
assert check_card_number ( 5082337440657928 ) # valid Mastercard card number
assert not check_card_number_str (’ 4601496706376197 ’) # invalid Visa card number