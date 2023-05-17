print ("Ingrese 2 palabras","\n")
p1 = str(input())
p2 = str(input())
print()
if len(p1)<len(p2):
  print (f"""La palabra 2 tiene más carácteres que la palabra 1. 
Total carácteres palabra 2: {len(p2)}.
Total carácteres palabra 1: {len(p1)}""")
else: 
  print (f"""La palabra 1 tiene más carácteres que la palabra 2.
Total carácteres palabra 1: {len(p1)}.
Total carácteres palabra 2: {len(p2)}""")