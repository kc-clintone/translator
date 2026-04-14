# Translatr

A simple full-stack Django application that translates text between English and Swahili using a small in-memory dictionary.

---

## Features

- Simple Django template frontend  
- Text input + language selector  
- POST API endpoint  
- In-memory translation dictionary  
- English → Swahili  
- Swahili → English  
- Clean minimal UI  

---

## API

### Endpoint

```

POST /api/v1/translate-text

````

### Request

```json
{
  "text": "put stone",
  "targetLanguage": "sw"
}
````

### Response

```json
{
  "translatedText": "weka mawe"
}
```

---

## Project Structure

```
translator/
│
├── translator/
│   ├── views.py
│   ├── urls.py
│   └── translate.py
│
├── templates/
│   └── index.html
│
└── manage.py
```

---

## Requirements

* Python 3.10+
* Django

---

## Installation

Clone the repository:

```
git clone https://github.com/kc-clintone/translator.git
cd translatr
```

Create virtual environment:

```
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```
pip install django
```

---

## Run the App

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000
```