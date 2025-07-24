
---

# **URL Shortener Service**

A simple URL shortening service built with **Flask**.
It provides endpoints to shorten URLs, redirect using a short code, and view analytics (click count & creation timestamp).

---

## **Features**

✔️ Shorten long URLs into a 6-character short code

✔️ Redirect users to the original URL using the short code

✔️ Track click counts for each short URL

✔️ Return creation timestamp and original URL via analytics

✔️ In-memory storage (no database required)

✔️ Basic URL validation and error handling

✔️ Thread-safe click count updates

---

## **Tech Stack**

* **Backend:** Python (Flask)
* **Testing:** Pytest
* **Storage:** In-memory dictionary (thread-safe with Lock)

---

## **Setup Instructions**

### **1. Prerequisites**

* Python **3.8+** installed
* `pip` package manager

### **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3. Run the Flask App**

```bash
python -m flask --app app.main run
```

The API will be available at: **[http://localhost:5000](http://localhost:5000)**

### **4. Run Tests**

```bash
pytest
```

---

## **API Usage**

### ✅ **1. Shorten URL**

**POST** `/api/shorten`

```bash
curl -X POST http://localhost:5000/api/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.example.com/very/long/url"}'
```

**Response:**

```json
{
  "short_code": "abc123",
  "short_url": "http://localhost:5000/abc123"
}
```

---

### ✅ **2. Redirect to Original URL**

**GET** `/<short_code>`

```bash
curl -L http://localhost:5000/abc123
```

Redirects to: `https://www.example.com/very/long/url`

---

### ✅ **3. Analytics for a Short URL**

**GET** `/api/stats/<short_code>`

```bash
curl http://localhost:5000/api/stats/abc123
```

**Response:**

```json
{
  "url": "https://www.example.com/very/long/url",
  "clicks": 5,
  "created_at": "2025-07-24T10:00:00"
}
```

---

## **Project Structure**

```
url-shortener/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # Flask routes and logic
│   ├── models.py        # In-memory storage and helper functions
│   └── config.py        # Configuration (BASE_URL, etc.)
│
├── tests/
│   └── test_app.py      # Pytest test cases
│
├── requirements.txt
├── README.md
└── NOTES.md
```

---

## **AI Usage**

See **NOTES.md** for details on how AI assistance was used.

---

