ans = input("Enter character to be reversed:")
rans = ""
for i in ans:
    rans = i + rans
if ans == rans:
    print(f"{rans} is palindrome!")
else:
    print(rans)
