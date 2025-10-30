#!/usr/bin/env python3
"""
Telegram Reminder Bot - Send Message Script

Этот скрипт отправляет сообщение в Telegram через Bot API.
Используется для автоматических напоминаний через GitHub Actions.

Требует переменные окружения:
    TELEGRAM_BOT_TOKEN - токен бота от BotFather
    TELEGRAM_CHAT_ID - ID чата получателя
"""

import os
import sys
import requests
from datetime import datetime, timedelta
from typing import Optional


def is_last_thursday_of_month(date: datetime) -> bool:
    """
    Проверяет, является ли указанная дата последним четвергом месяца.
    
    Логика:
    1. Проверяем, что сегодня четверг (weekday() == 3)
    2. Проверяем, что следующий четверг уже в следующем месяце
    
    Args:
        date: Дата для проверки
        
    Returns:
        True если это последний четверг месяца, иначе False
    """
    # Четверг = 3 (Monday is 0, Sunday is 6)
    if date.weekday() != 3:
        return False
    
    # Проверяем, что следующий четверг будет в другом месяце
    next_thursday = date + timedelta(days=7)
    return next_thursday.month != date.month


def send_telegram_message(
    bot_token: str,
    chat_id: str,
    message: str
) -> bool:
    """
    Отправляет сообщение через Telegram Bot API.
    
    Args:
        bot_token: Токен бота от BotFather
        chat_id: ID чата получателя
        message: Текст сообщения
        
    Returns:
        True если сообщение отправлено успешно, иначе False
    """
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"  # Поддержка форматирования
    }
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        
        result = response.json()
        if result.get("ok"):
            print(f"✅ Сообщение успешно отправлено!")
            print(f"📱 Chat ID: {chat_id}")
            print(f"📅 Дата: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
            return True
        else:
            print(f"❌ Ошибка API: {result.get('description', 'Unknown error')}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка при отправке сообщения: {e}")
        return False


def get_env_variable(name: str) -> Optional[str]:
    """
    Безопасно получает переменную окружения.
    
    Args:
        name: Имя переменной
        
    Returns:
        Значение переменной или None
    """
    value = os.environ.get(name)
    if not value:
        print(f"⚠️  Переменная окружения {name} не установлена!")
        return None
    return value


def main():
    """
    Основная функция скрипта.
    
    Проверяет:
    1. Является ли сегодня последним четвергом месяца
    2. Наличие необходимых переменных окружения
    3. Отправляет сообщение, если все условия выполнены
    """
    print("🤖 Telegram Reminder Bot запущен\n")
    
    # Проверяем, является ли сегодня последним четвергом
    today = datetime.now()
    print(f"📅 Сегодня: {today.strftime('%d.%m.%Y (%A)')}")
    
    if not is_last_thursday_of_month(today):
        print("ℹ️  Сегодня НЕ последний четверг месяца.")
        print("⏭️  Пропускаем отправку сообщения.")
        sys.exit(0)
    
    print("✅ Сегодня последний четверг месяца!")
    print("📨 Приступаем к отправке сообщения...\n")
    
    # Получаем переменные окружения
    bot_token = get_env_variable("TELEGRAM_BOT_TOKEN")
    chat_id = get_env_variable("TELEGRAM_CHAT_ID")
    
    if not bot_token or not chat_id:
        print("\n❌ Не все переменные окружения установлены!")
        print("Требуется: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID")
        sys.exit(1)
    
    # Текст сообщения
    message = "Сегодня в библиотеке санитарный день!"
    
    print(f"💬 Текст сообщения: \"{message}\"\n")
    
    # Отправляем сообщение
    success = send_telegram_message(bot_token, chat_id, message)
    
    if success:
        print("\n🎉 Задача выполнена успешно!")
        sys.exit(0)
    else:
        print("\n💥 Не удалось отправить сообщение!")
        sys.exit(1)


if __name__ == "__main__":
    main()
