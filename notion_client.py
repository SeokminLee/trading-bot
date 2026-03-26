import os
import requests

NOTION_KEY = os.environ.get('NOTION_API_KEY')
# Use the database_id (not the data_source_id) for creating pages.
DATABASE_ID = '311d4cb3-702d-8132-9582-cbb4a940088e'

HEADERS = {
    'Authorization': f'Bearer {NOTION_KEY}',
    'Notion-Version': '2025-09-03',
    'Content-Type': 'application/json'
}


def append_trade(name, profit, position, win, lose, date):
    # Make sure the integration is shared with this database in Notion.
    url = 'https://api.notion.com/v1/pages'
    payload = {
        'parent': {'database_id': DATABASE_ID},
        'properties': {
            '매매 복기': {'title': [{'text': {'content': name}}]},
            '수익금': {'number': profit},
            '포지션': {'select': {'name': position}},
            '승': {'checkbox': win},
            '패': {'checkbox': lose},
            '날짜': {'date': {'start': date}}
        }
    }
    r = requests.post(url, headers=HEADERS, json=payload)
    return r.status_code, r.text
