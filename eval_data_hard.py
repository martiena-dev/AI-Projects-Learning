# Harder test cases against the 13-doc knowledge base in rag_hard.py
# doc indexes: 0=MongoDB 1=PostgreSQL 2=Redis 3=SQLite 4=FastAPI 5=Flask
# 6=Django 7=MQTT 8=HTTP 9=WebSocket 10=virtualenv 11=Docker 12=Git

test_cases = [
    {"question": "What in-memory store is used for caching?", "correct_doc": 2},
    {"question": "Which database uses SQL and tables?", "correct_doc": 1},
    {"question": "What is a lightweight file-based database?", "correct_doc": 3},
    {"question": "Which framework has a built-in admin panel?", "correct_doc": 6},
    {"question": "What protocol gives real-time two-way communication?", "correct_doc": 9},
    {"question": "How do I package an app to run anywhere?", "correct_doc": 11},
    {"question": "What is used for messaging on IoT devices?", "correct_doc": 7},
    {"question": "Which Python framework is simple and flexible?", "correct_doc": 5},
    {"question": "What should I use to store data quickly?", "correct_doc": 2},
    {"question": "How do I build a web app in Python?", "correct_doc": 5},
    {"question": "What helps my app run the same everywhere?", "correct_doc": 11}
]