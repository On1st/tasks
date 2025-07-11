user_input = input("Введіть рядок: ")
cleaned = ''.join(c.lower() for c in user_input if c.isalnum())
is_palindrome = True
for i in range(len(cleaned) // 2):
    if cleaned[i] != cleaned[-(i + 1)]:
        is_palindrome = False
        break
if is_palindrome:
    print("Це паліндром!")
else:
    print("Це не паліндром.")
