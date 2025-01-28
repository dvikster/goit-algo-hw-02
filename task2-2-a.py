from collections import deque

def is_palindrome(string):
    # Видаляємо всі пробіли, перетворюємо на нижній регістр і залишаємо лише алфавітно-цифрові символи
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    
    # Створюємо двосторонню чергу з очищеного рядка
    char_deque = deque(cleaned_string)
    
    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False  # Якщо символи не збігаються, це не паліндром
    
    return True  # Якщо всі символи збігаються, це паліндром

# Тестування функції
if __name__ == "__main__":
    test_strings = [
        "Око",                        # Паліндром
        "Я несу гусеня",              # Паліндром
        "А роза упала на лапу Азора", # Паліндром
        "Дід",                        # Паліндром
        "Тато встиг свататись татам", # Паліндром
        "Книга",                      # Не паліндром
        "Море",                       # Не паліндром
        "Привіт, світе!",             # Не паліндром
        "Сонце",                      # Не паліндром
        "Чи їде хтось у місто?"       # Не паліндром
    ]
    
    for string in test_strings:
        result = is_palindrome(string)
        print(f"'{string}' -> {'Паліндром' if result else 'Не паліндром'}")
