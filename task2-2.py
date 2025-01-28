from collections import deque

def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    char_deque = deque(cleaned_string)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

if __name__ == "__main__":
    while True:
        user_input = input("Введіть текст для перевірки (або 'q' для виходу): ").strip()
        if user_input.lower() == 'q':
            print("Програма завершена.")
            break
        result = is_palindrome(user_input)
        print(f"'{user_input}' -> {'Паліндром' if result else 'Не паліндром'}")