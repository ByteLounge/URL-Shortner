import threading
from datetime import datetime

url_store = {}
lock = threading.Lock()


def save_url(short_code, original_url):
    """Save the URL with thread safety."""
    with lock:
        url_store[short_code] = {
            "url": original_url,
            "clicks": 0,
            "created_at": datetime.utcnow().isoformat()
        }


def get_url(short_code):
    """Return URL details or None if not found."""
    return url_store.get(short_code)


def increment_click(short_code):
    """Increment click count if short code exists."""
    with lock:
        if short_code in url_store:
            url_store[short_code]["clicks"] += 1
