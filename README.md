

# 🌐 AKGPT - Multilingual README

## 🇷🇺 Русская версия | [🇺🇸 English Version](#-english-version)

# 🚀 AKGPT

**AKGPT** — это простая и удобная Python-библиотека для взаимодействия с [Text-to-Text API](https://fullai.vercel.app/models/) от [fullai.vercel.app](https://fullai.vercel.app). Она позволяет легко генерировать текст с помощью различных языковых моделей, используя гибкие параметры настройки.

---

## 📦 Установка

Установите библиотеку через pip:

```bash
pip install akgpt
```

---

## 🚀 Использование

### 📌 Основной запрос

```python
from akgpt.main import AKGPT

client = AKGPT()

prompt = "Что такое искусственный интеллект?"
result = client.query(prompt)

if result:
    print("Ответ API:", result)
```

---
###Пример  Вызова всех моделей  
```python


from akgpt import AKGPT

# Инициализация клиента
client = AKGPT()

# Получаем список доступных моделей
models = client.get_available_models()
print(f"Доступно моделей: {len(models)}")
print(models)

# Выбор модели из списка
print("\n" + "="*50)
print("ДОСТУПНЫЕ МОДЕЛИ:")
for i, model in enumerate(models, 1):
    print(f"{i}. {model}")

# Пользователь выбирает модель
while True:
    try:
        choice = int(input("\nВыберите номер модели (1-{}): ".format(len(models))))
        if 1 <= choice <= len(models):
            selected_model = models[choice-1]
            break
        else:
            print("Пожалуйста, введите число из указанного диапазона")
    except ValueError:
        print("Пожалуйста, введите корректный номер")

# Ввод запроса от пользователя
print("\n" + "="*50)
user_prompt = input("Введите ваш запрос: ")

# Дополнительные параметры (опционально)
print("\nНастройте параметры генерации (нажмите Enter для значений по умолчанию):")
try:
    max_tokens = int(input("Максимальное количество токенов [150]: ") or "150")
    temperature = float(input("Температура (0.1-1.0) [0.7]: ") or "0.7")
except ValueError:
    print("Использую значения по умолчанию")
    max_tokens = 150
    temperature = 0.7

# Системный промпт (опционально)
system_prompt = input("Системный промпт (роль модели) [пусто]: ") or None

# Выполнение запроса
print("\n" + "="*50)
print(f"Генерирую ответ с помощью модели: {selected_model}")
print("="*50)

result = client.query(
    prompt=user_prompt,
    model=selected_model,
    system=system_prompt,
    max_tokens=max_tokens,
    temperature=temperature
)

# Вывод результата
print("\n📝 РЕЗУЛЬТАТ:")
print("="*50)
print(result)
print("="*50)

```
### ⚙️ Запрос с дополнительными параметрами

Вы можете настроить поведение генерации с помощью различных параметров:

```python
from akgpt.main import AKGPT

client = AKGPT()

prompt = "Напиши короткое стихотворение о роботах"
model = "mistral"
seed = 123
system_prompt = "Ты поэт"

result_poem = client.query(
    prompt,
    model=model,
    seed=seed,
    system=system_prompt
)

if result_poem:
    print("Ответ API:", result_poem)
```

---

### 📥 Получение JSON-ответа

Для получения ответа в формате JSON установите `json_response=True`:

```python
import json
from akgpt.main import AKGPT

client = AKGPT()

prompt = "Что такое AI?"
result_json = client.query(prompt, json_response=True)

if result_json:
    print("Ответ API (JSON):")
    print(json.dumps(result_json, indent=2, ensure_ascii=False))
```

---

## 🧠 Доступные параметры метода `query`

| Параметр           | Тип      | Описание |
|--------------------|----------|----------|
| `prompt` *(обязательный)* | `str` | Входной текстовый промпт |
| `model` *(опционально)* | `str` | Модель для генерации (см. список ниже) |
| `seed` *(опционально)* | `int` | Сид для воспроизводимых результатов |
| `temperature` *(опционально)* | `float` | Контроль случайности (0.0 - 3.0) |
| `top_p` *(опционально)* | `float` | Ядерная выборка (0.0 - 1.0) |
| `presence_penalty` *(опционально)* | `float` | Штраф за повторяющиеся токены (-2.0 до 2.0) |
| `frequency_penalty` *(опционально)* | `float` | Штраф за частоту токенов (-2.0 до 2.0) |
| `json_response` *(опционально)* | `bool` | Вернуть ответ в формате JSON |
| `system` *(опционально)* | `str` | Системный промпт |
| `stream` *(опционально)* | `bool` | Потоковая передача (SSE) |
| `private` *(опционально)* | `bool` | Не показывать в публичной ленте |
| `referrer` *(опционально)* | `str` | Источник запроса |

---

## 🤖 Доступные модели

| Код модели         | Описание |
|--------------------|----------|
| `gemini`           | Gemini 2.5 Flash Lite |
| `gpt-5-nano`       | OpenAI GPT-5 Nano |
| `mistral`          | Mistral Small 3.1 24B |
| `nova-fast`        | Amazon Nova Micro |
| `openai`           | Псевдоним для `gpt-5-nano` |
| `openai-fast`      | OpenAI GPT-4.1 Nano |
| `qwen-coder`       | Qwen 2.5 Coder 32B |
| `bidara`           | Biomimetic Designer and Research Assistant от NASA |
| `midijourney`      | MIDIjourney |

---

## 💡 Примеры использования

### 🧪 Генерация с потоковой передачей

```python
from akgpt.main import AKGPT

client = AKGPT()

prompt = "Расскажи историю о космосе"
result = client.query(prompt, stream=True)

for chunk in result:
    print(chunk, end='', flush=True)
```

---

### 🔐 Приватный запрос

```python
from akgpt.main import AKGPT

client = AKGPT()

prompt = "Секретный вопрос"
result = client.query(prompt, private=True)

if result:
    print("Ответ (приватный):", result)
```

---

### 🧠 Использование системного промпта

```python
from akgpt.main import AKGPT

client = AKGPT()

prompt = "Объясни квантовую физику"
system = "Ты учёный-физик"

result = client.query(prompt, system=system)

if result:
    print("Объяснение:", result)
```

---

## 📄 Лицензия

Эта библиотека распространяется под лицензией **MIT**. Подробности см. в файле [LICENSE](https://github.com/TETRIX8/akgpt/blob/main/LICENSE).

---

## 📎 Полезные ссылки

- 🌐 [API модели](https://fullai.vercel.app/models/)
- 📘 [Документация](https://github.com/TETRIX8/akgpt)
- 🐱 [GitHub репозиторий](https://github.com/TETRIX8/akgpt)

---

## 🔖 SEO Keywords
```
AI text generation, Python AI library, text-to-text API, machine learning models, natural language processing, AI models, Gemini API, Mistral AI, OpenAI GPT-5, Qwen Coder, AI poetry generator, AI assistant, Python NLP, AI streaming, AI private requests, AI system prompts
```

---

---

## 🇺🇸 English Version | [🇷🇺 Русская версия](#-akgpt---multilingual-readme)

# 🚀 AKGPT

**AKGPT** is a simple and easy-to-use Python library for interacting with the [Text-to-Text API](https://fullai.vercel.app/models/) from [fullai.vercel.app](https://fullai.vercel.app). It allows you to easily generate text using various language models with flexible configuration parameters.

---

## 📦 Installation

Install the library via pip:

```bash
pip install akgpt
```

---

## 🚀 Usage

### 📌 Basic Request

```python
from akgpt.main import AKGPT

client = AKGPT()

prompt = "What is artificial intelligence?"
result = client.query(prompt)

if result:
    print("API Response:", result)
```

---

### ⚙️ Request with Additional Parameters

You can customize the generation behavior with various parameters:

```python
from akgpt.main import AKGPT

client = AKGPT()

prompt = "Write a short poem about robots"
model = "mistral"
seed = 123
system_prompt = "You are a poet"

result_poem = client.query(
    prompt,
    model=model,
    seed=seed,
    system=system_prompt
)

if result_poem:
    print("API Response:", result_poem)
```

---

### 📥 Getting JSON Response

To get the response in JSON format, set `json_response=True`:

```python
import json
from akgpt.main import AKGPT

client = AKGPT()

prompt = "What is AI?"
result_json = client.query(prompt, json_response=True)

if result_json:
    print("API Response (JSON):")
    print(json.dumps(result_json, indent=2))
```

---

## 🧠 Available `query` Method Parameters

| Parameter           | Type      | Description |
|--------------------|----------|-------------|
| `prompt` *(required)* | `str` | Input text prompt |
| `model` *(optional)* | `str` | Model for generation (see list below) |
| `seed` *(optional)* | `int` | Seed for reproducible results |
| `temperature` *(optional)* | `float` | Controls randomness (0.0 - 3.0) |
| `top_p` *(optional)* | `float` | Nucleus sampling (0.0 - 1.0) |
| `presence_penalty` *(optional)* | `float` | Penalizes tokens based on presence (-2.0 to 2.0) |
| `frequency_penalty` *(optional)* | `float` | Penalizes tokens based on frequency (-2.0 to 2.0) |
| `json_response` *(optional)* | `bool` | Return response in JSON format |
| `system` *(optional)* | `str` | System prompt |
| `stream` *(optional)* | `bool` | Streaming response (SSE) |
| `private` *(optional)* | `bool` | Don't show in public feed |
| `referrer` *(optional)* | `str` | Referrer URL/identifier |

---

## 🤖 Available Models

| Model Code         | Description |
|--------------------|-------------|
| `gemini`           | Gemini 2.5 Flash Lite |
| `gpt-5-nano`       | OpenAI GPT-5 Nano |
| `mistral`          | Mistral Small 3.1 24B |
| `nova-fast`        | Amazon Nova Micro |
| `openai`           | Alias for `gpt-5-nano` |
| `openai-fast`      | OpenAI GPT-4.1 Nano |
| `qwen-coder`       | Qwen 2.5 Coder 32B |
| `bidara`           | Biomimetic Designer and Research Assistant by NASA |
| `midijourney`      | MIDIjourney |

---

## 💡 Usage Examples

### 🧪 Streaming Generation

```python
from akgpt.main import AKGPT

client = AKGPT()

prompt = "Tell a story about space"
result = client.query(prompt, stream=True)

for chunk in result:
    print(chunk, end='', flush=True)
```

---

### 🔐 Private Request

```python
from akgpt.main import AKGPT

client = AKGPT()

prompt = "Secret question"
result = client.query(prompt, private=True)

if result:
    print("Response (private):", result)
```

---

### 🧠 Using System Prompt

```python
from akgpt.main import AKGPT

client = AKGPT()

prompt = "Explain quantum physics"
system = "You are a physicist"

result = client.query(prompt, system=system)

if result:
    print("Explanation:", result)
```

---

## 📄 License

This library is distributed under the **MIT** license. See the [LICENSE](https://github.com/TETRIX8/akgpt/blob/main/LICENSE) file for details.

---

## 📎 Useful Links

- 🌐 [API Models](https://fullai.vercel.app/models/)
- 📘 [Documentation](https://github.com/TETRIX8/akgpt)
- 🐱 [GitHub Repository](https://github.com/TETRIX8/akgpt)

---

## 🔖 SEO Keywords
```
AI text generation, Python AI library, text-to-text API, machine learning models, natural language processing, AI models, Gemini API, Mistral AI, OpenAI GPT-5, Qwen Coder, AI poetry generator, AI assistant, Python NLP, AI streaming, AI private requests, AI system prompts
```

---

🌟 Made with ❤️ by [TETRIX8](https://github.com/TETRIX8)

---

## 🔍 SEO Meta Tags для HTML (если нужно)

```html
<meta name="description" content="AKGPT - Simple Python library for AI text generation with multiple models. Supports Gemini, Mistral, OpenAI GPT-5, and more. Easy to use text-to-text API integration.">
<meta name="keywords" content="AI text generation, Python AI library, text-to-text API, machine learning models, natural language processing, AI models, Gemini API, Mistral AI, OpenAI GPT-5, Qwen Coder, AI poetry generator, AI assistant, Python NLP, AI streaming, AI private requests, AI system prompts">
<meta name="author" content="TETRIX8">
<meta name="robots" content="index, follow">
<meta property="og:title" content="AKGPT - Python AI Text Generation Library">
<meta property="og:description" content="Simple Python library for AI text generation with multiple models. Supports Gemini, Mistral, OpenAI GPT-5, and more.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://github.com/TETRIX8/akgpt">
```

