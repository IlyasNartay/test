from datetime import datetime, timedelta
import locale

# Устанавливаем локаль для английского языка (для вывода дня недели)
locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')

# 1. Вычисляем текущую дату и время
current_date = datetime.now()
print(f"1. Current date/time: {current_date}")

# 2. Добавляем 1 год, 6 дней, 2 часа и 300 секунд
future_date = current_date + timedelta(days=365+6, hours=2, seconds=300)
print(f"2. Future date/time: {future_date}")

# 4. Повторно вычисляем текущую дату
new_current_date = datetime.now()
print(f"4. New current date/time: {new_current_date}")

# 5. Определяем день недели на английском
day_of_week = new_current_date.strftime("%A")
print(f"5. Today is: {day_of_week}")