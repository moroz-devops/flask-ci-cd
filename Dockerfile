# Базовий образ Python
FROM python:3.11-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файли залежностей
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо решту файлів проєкту
COPY . .

# Відкриваємо порт 5000
EXPOSE 5000

# Команда для запуску додатку
CMD ["python", "app.py"]
