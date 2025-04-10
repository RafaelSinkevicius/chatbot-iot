import json
from datetime import datetime
from dateutil.parser import parse

def load_data():
    try:
        with open('data/operations.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao carregar dados: {e}")
        return []

def parse_date(message):
    try:
        if 'hoje' in message:
            return datetime.now().strftime('%Y-%m-%d')
        for part in message.split():
            if '-' in part and len(part) == 10:
                return datetime.strptime(part, '%Y-%m-%d').strftime('%Y-%m-%d')
        return None
    except ValueError:
        return None