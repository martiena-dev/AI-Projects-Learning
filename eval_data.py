# Each test case: a question + the index of the document that SHOULD be retrieved.
# (Document indexes match the `documents` list in rag.py: 0=MongoDB, 1=FastAPI,
#  2=MQTT, 3=virtualenv, 4=Git, 5=API key)

test_cases = [
    {"question": "How do I keep my project's Python packages separate?", "correct_doc": 3},
    {"question": "What tool tracks changes to my code?", "correct_doc": 4},
    {"question": "How do IoT devices send messages?", "correct_doc": 2},
    {"question": "What framework builds APIs fast in Python?", "correct_doc": 1},
    {"question": "How do I prove my identity to an external service?", "correct_doc": 5},
    {"question": "What database stores data as JSON-like documents?", "correct_doc": 0},
    {"question": "Where is data kept in a flexible document format?", "correct_doc": 0},
    {"question": "How can I build a web API quickly with Python?", "correct_doc": 1},
    {"question": "What protocol is lightweight for connected devices?", "correct_doc": 2},
    {"question": "How do I isolate dependencies between projects?", "correct_doc": 3},
]