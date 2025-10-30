# ⚡ Быстрый старт

## 📦 Что уже готово

✅ **send_message.py** — основной скрипт с логикой отправки  
✅ **requirements.txt** — Python-зависимости  
✅ **.github/workflows/last_thursday.yml** — автоматизация через GitHub Actions  
✅ **README.md** — полная документация проекта  
✅ **SETUP_GUIDE.md** — пошаговая инструкция настройки  
✅ **.gitignore** — защита от случайной загрузки лишних файлов  

---

## 🚀 Три простых команды для старта

### 1️⃣ Установите зависимости
```bash
pip install -r requirements.txt
```

### 2️⃣ Создайте бота в Telegram
- Найдите @BotFather → `/newbot`
- Получите токен и Chat ID мамы (см. SETUP_GUIDE.md)

### 3️⃣ Загрузите на GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/ВАШ_USERNAME/Telegram-Reminders.git
git push -u origin main
```

**Затем:** Добавьте секреты в GitHub (Settings → Secrets → Actions)

---

## 📚 Документация

- **README.md** — общее описание, принцип работы, идеи расширения
- **SETUP_GUIDE.md** — подробная инструкция шаг за шагом

---

## 🎯 Результат

После настройки бот будет **автоматически** отправлять сообщение:

📅 **Когда:** каждый последний четверг месяца в 09:00 UTC (12:00 МСК)  
💬 **Текст:** "Сегодня в библиотеке санитарный день!"  
📱 **Кому:** вашей маме  

---

**Всё готово к работе! 🎉**
