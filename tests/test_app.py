import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app

test_client = app.test_client()


def test_shorten_url():
    response = test_client.post('/api/shorten', json={"url": "https://example.com"})
    assert response.status_code == 201
    data = response.get_json()
    assert "short_code" in data
    assert data["short_url"].startswith("http://localhost:5000/")


def test_invalid_url():
    response = test_client.post('/api/shorten', json={"url": "invalid-url"})
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_redirect_and_click_count():
    res = test_client.post('/api/shorten', json={"url": "https://google.com"})
    short_code = res.get_json()["short_code"]

    redirect_res = test_client.get(f'/{short_code}')
    assert redirect_res.status_code == 302

    stats_res = test_client.get(f'/api/stats/{short_code}')
    stats_data = stats_res.get_json()
    assert stats_data["clicks"] == 1


def test_stats_returns_correct_data():
    res = test_client.post('/api/shorten', json={"url": "https://openai.com"})
    short_code = res.get_json()["short_code"]
    stats_res = test_client.get(f'/api/stats/{short_code}')
    data = stats_res.get_json()
    assert data["url"] == "https://openai.com"
    assert "created_at" in data
    assert data["clicks"] == 0


def test_non_existent_short_code():
    res = test_client.get('/api/stats/abcdef')
    assert res.status_code == 404
    assert "error" in res.get_json()
