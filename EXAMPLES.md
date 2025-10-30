# Примеры использования

## 🧪 Локальное тестирование

### Вариант 1: С временными переменными окружения

**Windows CMD:**
```cmd
set TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
set TELEGRAM_CHAT_ID=123456789
python send_message.py
```

**Windows PowerShell:**
```powershell
$env:TELEGRAM_BOT_TOKEN="1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"
$env:TELEGRAM_CHAT_ID="123456789"
python send_message.py
```

**Linux/Mac:**
```bash
export TELEGRAM_BOT_TOKEN="1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"
export TELEGRAM_CHAT_ID="123456789"
python send_message.py
```

### Вариант 2: С .env файлом (для разработки)

1. Создайте файл `.env` в корне проекта:
```env
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_CHAT_ID=123456789
```

2. Установите python-dotenv:
```bash
pip install python-dotenv
```

3. Добавьте в начало `send_message.py`:
```python
from dotenv import load_dotenv
load_dotenv()
```

> **Важно:** Файл `.env` уже добавлен в `.gitignore` и не будет загружен на GitHub

---

## 📋 Примеры вывода скрипта

### Если сегодня последний четверг месяца:

```
🤖 Telegram Reminder Bot запущен

📅 Сегодня: 28.11.2024 (Thursday)
✅ Сегодня последний четверг месяца!
📨 Приступаем к отправке сообщения...

💬 Текст сообщения: "Сегодня в библиотеке санитарный день!"

✅ Сообщение успешно отправлено!
📱 Chat ID: 123456789
📅 Дата: 28.11.2024 12:00:35

🎉 Задача выполнена успешно!
```

### Если сегодня НЕ последний четверг:

```
🤖 Telegram Reminder Bot запущен

📅 Сегодня: 21.11.2024 (Thursday)
ℹ️  Сегодня НЕ последний четверг месяца.
⏭️  Пропускаем отправку сообщения.
```

---

## 🔧 Ручное тестирование в GitHub Actions

### Способ 1: Кнопка "Run workflow"

1. Откройте ваш репозиторий на GitHub
2. **Actions** → **Monthly Library Reminder**
3. **Run workflow** → выберите ветку `main` → **Run workflow**
4. Дождитесь завершения и проверьте логи

### Способ 2: Push commit

Любой push в репозиторий НЕ запустит workflow автоматически.  
Workflow запускается только:
- По расписанию (каждый четверг в 09:00 UTC)
- При ручном запуске через "Run workflow"

---

## 🎯 Проверка работы алгоритма

### Тест: Определение последнего четверга

Вы можете временно изменить дату в скрипте для тестирования:

```python
# В функции main() замените:
today = datetime.now()

# На тестовую дату:
today = datetime(2024, 11, 28)  # Последний четверг ноября 2024
```

Это позволит проверить логику без ожидания реальной даты.

---

## 📊 Календарь последних четвергов 2025

| Месяц | Дата | День недели |
|-------|------|-------------|
| Январь | 30 | Четверг |
| Февраль | 27 | Четверг |
| Март | 27 | Четверг |
| Апрель | 24 | Четверг |
| Май | 29 | Четверг |
| Июнь | 26 | Четверг |
| Июль | 31 | Четверг |
| Август | 28 | Четверг |
| Сентябрь | 25 | Четверг |
| Октябрь | 30 | Четверг |
| Ноябрь | 27 | Четверг |
| Декабрь | 25 | Четверг |

---

## 🐛 Отладка ошибок

### Ошибка: "Chat not found"

**Причина:** Бот не может отправить сообщение пользователю, который не нажал Start.

**Решение:**
1. Найдите вашего бота в Telegram
2. Нажмите `/start`
3. Получите Chat ID заново

### Ошибка: "Unauthorized"

**Причина:** Неверный токен бота.

**Решение:**
1. Проверьте токен в GitHub Secrets
2. Убедитесь, что нет лишних пробелов
3. Создайте нового бота через BotFather (если нужно)

### Ошибка: "Connection timeout"

**Причина:** Проблемы с сетью или API Telegram недоступен.

**Решение:**
- Подождите несколько минут
- Проверьте статус API: https://www.githubstatus.com/
- Workflow автоматически повторит попытку на следующий четверг

---

## 💡 Расширенные примеры

### Отправка форматированного текста

Измените текст сообщения с Markdown:

```python
message = """
📚 *Напоминание*

Сегодня в библиотеке санитарный день!

_С уважением, ваш бот_ 🤖
"""
```

### Добавление кнопок (inline keyboard)

```python
payload = {
    "chat_id": chat_id,
    "text": message,
    "parse_mode": "Markdown",
    "reply_markup": {
        "inline_keyboard": [[
            {"text": "✅ Понятно", "callback_data": "ok"}
        ]]
    }
}
```

### Отправка нескольким получателям

```python
chat_ids = [
    os.environ.get("TELEGRAM_CHAT_ID_1"),
    os.environ.get("TELEGRAM_CHAT_ID_2"),
]

for chat_id in chat_ids:
    if chat_id:
        send_telegram_message(bot_token, chat_id, message)
```

---

**Удачного тестирования! 🚀**
