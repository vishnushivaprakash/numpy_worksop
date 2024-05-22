# find if the given number is a palindrome or not?
# find if the given number is a palindrome or not?
a=int(input())
rev=str(a)
rev=a[::-1]
if(a==rev):
  print("its palindrome")
else:
  print("not a palindrome")
