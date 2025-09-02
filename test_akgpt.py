import json
from akgpt.main import AKGPT

client = AKGPT()

print("\n--- Тестовый запрос: Что такое искусственный интеллект? ---")
result = client.query("Что такое искусственный интеллект?")
if result:
    print("Ответ API:", result)

print("\n--- Тестовый запрос с параметрами: Короткое стихотворение о роботах ---")
result_poem = client.query("Напиши короткое стихотворение о роботах", model="mistral", seed=123, system="Ты поэт")
if result_poem:
    print("Ответ API:", result_poem)

print("\n--- Тестовый запрос с JSON ответом: Что такое AI? ---")
result_json = client.query("Что такое AI?", json_response=True)
if result_json:
    print("Ответ API (JSON):", json.dumps(result_json, indent=2, ensure_ascii=False))


