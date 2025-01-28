import queue
import random
import time

# Створення черги заявок
request_queue = queue.Queue()

# Функція для генерації нових заявок
def generate_request():
    # Генеруємо заявку з унікальним ідентифікатором
    request_id = random.randint(1000, 9999)
    print(f"Нова заявка {request_id} додана до черги.")
    request_queue.put(request_id)

# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        # Видаляємо заявку з черги та обробляємо її
        request_id = request_queue.get()
        print(f"Заявка {request_id} обробляється...")
        time.sleep(1)  # Імітація часу обробки
        print(f"Заявка {request_id} успішно оброблена.")
    else:
        print("Чергa пуста. Немає заявок для обробки.")

# Головний цикл програми
def main():
    print("Система обробки заявок запущена.")
    try:
        while True:
            action = input("\nВведіть '1' для генерації заявки, '2' для обробки заявки, або 'q' для виходу: ").strip().lower()
            if action == '1':
                generate_request()
            elif action == '2':
                process_request()
            elif action == 'q':
                print("Програма завершена.")
                break
            else:
                print("Невірна команда. Спробуйте ще раз.")
    except KeyboardInterrupt:
        print("\nПрограма завершена користувачем.")

# Запуск програми
if __name__ == "__main__":
    main()

