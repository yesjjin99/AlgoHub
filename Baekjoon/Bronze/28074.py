s = input()

if all(c in s for c in ['M', 'O', 'B', 'I', 'S']):
    print("YES")
else:
    print("NO")