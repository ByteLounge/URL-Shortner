

---

## **Project Overview**

This is a simple URL Shortener service built using **Flask**.
It provides three core API endpoints:

1. **Shorten URL** (`POST /api/shorten`)
2. **Redirect to Original URL** (`GET /<short_code>`)
3. **Analytics** (`GET /api/stats/<short_code>`)

The application uses an **in-memory dictionary** for storing URL mappings and supports basic analytics (click count + creation timestamp).

---

## **Design Choices**

### **1. In-Memory Storage**

* **Why?** Requirement explicitly states "don’t use external databases."
* **Data Structure:** Python `dict` (`url_store`) with the following structure:

  ```python
  {
      "abc123": {
          "url": "https://example.com",
          "clicks": 5,
          "created_at": "2025-07-24T10:00:00"
      }
  }
  ```
* **Thread Safety:** Uses `threading.Lock()` to handle concurrent updates (especially click count).

---

### **2. Short Code Generation**

* 6-character **alphanumeric** string generated using:

  ```python
  ''.join(random.choices(string.ascii_letters + string.digits, k=6))
  ```
* This ensures randomness and minimal collision risk for small-scale use.

---

### **3. URL Validation**

* Simple **regex** ensures the URL is valid:

  ```python
  r'^(https?://)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(/.*)?$'
  ```
* If the URL is invalid, returns HTTP `400`.

---

### **4. Analytics**

* Clicks are incremented every time a redirect occurs (`GET /<short_code>`).
* Timestamp is stored in **ISO 8601** format for easier readability.

---

### **5. Configurable Base URL**

* **`config.py`** contains:

  ```python
  class Config:
      BASE_URL = "http://localhost:5000"
  ```
* This allows easy change to a production domain in the future.

---

### **6. Testing**

* **5 Tests** (`tests/test_app.py`) cover:

  * URL shortening success
  * Invalid URL error
  * Redirect + click increment
  * Stats retrieval
  * Non-existent short code error

Run tests with:

```bash
pytest
```

---

### **7. AI Usage Policy**

* **ChatGPT** was used to:

  * Suggest best practices
  * Improve code quality and structure
  * Generate initial test cases

All code was manually reviewed and updated for clarity and correctness.

---

## **Limitations**

* Data is **not persistent** (reset on app restart).
* No collision detection (low probability but possible).
* Not production-ready (only for learning/demo purposes).

---

## **Future Improvements**

* Use a database (SQLite, Redis, etc.) for persistence.
* Add collision detection for short codes.
* Support custom short codes.
* Add rate limiting and authentication for production use.

---


