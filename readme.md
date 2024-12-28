
```markdown
# 🚀 Сервер для общения с GPT через SSE

Этот сервер предоставляет два основных эндпоинта:
1. **`/api/chat`** — для отправки запросов к модели GPT-4 через SSE (Server-Sent Events).
2. **`/api/info`** — для получения информации о доступных эндпоинтах и их использовании.

## 🏃‍♂️ Запуск сервера

Для запуска сервера выполните следующую команду:

```bash
python server.py
```

Сервер будет запущен на [http://185.185.69.111:8765](http://185.185.69.111:8765).

## 📚 Эндпоинты

### 1. `/api/chat` 💬

Эндпоинт для общения с моделью GPT-4 с использованием SSE.

**Метод:** `GET`  
**Параметры запроса:**
- `text` (обязательный) — текст, который отправляется пользователем для обработки моделью GPT.

**Пример запроса:**

```http
GET http://185.185.69.111:8765/api/chat?text=Привет,%20как%20ты?
```

**Ответ:**

Сервер будет отправлять данные в реальном времени через SSE. Ответ будет представлять собой поток данных, где каждый фрагмент будет содержать часть ответа от модели GPT.

**Пример ответа (SSE):**

```text
data: Привет! Я в порядке, спасибо за вопрос.
data: Чем могу помочь?
event: end
data: [DONE]
```

- `data:` — текст, который генерируется моделью.
- `event: end` — сигнал окончания потока.

**Ошибки:**
- Если параметр `text` не передан, сервер вернет ошибку:
  ```json
  {
    "error": "Отсутствует параметр 'text'"
  }
  ```

### 2. `/api/info` ℹ️

Эндпоинт для получения информации о доступных эндпоинтах и их использовании.

**Метод:** `GET`  
**Ответ:**
Сервер вернет информацию о доступных эндпоинтах.

**Пример ответа:**

```json
{
  "message": "Инструкции по использованию",
  "endpoints": {
    "/api/chat": {
      "description": "Эндпоинт для взаимодействия с моделью GPT",
      "parameters": {
        "text": "Текст ввода пользователя"
      }
    },
    "/api/info": {
      "description": "Возвращает инструкции по использованию и доступные эндпоинты"
    }
  }
}
```

## ⚠️ Описание ошибок

- **400 Bad Request**: Ошибка, если не передан обязательный параметр `text` в запросе.
- **404 Not Found**: Если запрос отправлен на несуществующий эндпоинт.
- **500 Internal Server Error**: Ошибка на сервере, возникающая во время обработки запроса.

## 🧠 Используемая модель

Модель, использующаяся на сервере, основана на **GPT-4**. Она отвечает на текстовые запросы пользователя в реальном времени с использованием технологии **SSE**.

## 📝 Примечания

- Сервер использует кодировку **UTF-8** для всех сообщений.
- Обратите внимание, что сервер поддерживает только **GET-запросы**.

🎉 Приятного общения с GPT! 😄
```
