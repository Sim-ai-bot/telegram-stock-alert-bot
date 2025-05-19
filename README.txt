ИНСТРУКЦИЯ:

1. Залей содержимое в GitHub (можешь создать репозиторий telegram-stock-alert-bot)
2. На Render.com создай New Web Service -> выбери GitHub
3. Стартовая команда: python main.py
4. Добавь ENV переменные:
   - FINNHUB_API_KEY
   - TELEGRAM_BOT_TOKEN
   - TELEGRAM_CHAT_ID

5. Чтобы бот на ПК выключал Render — вставь свой API ключ и SERVICE_ID в pause_bot.py
6. Чтобы включить обратно — используй resume_bot.py
