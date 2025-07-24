import re
import string
import random
from flask import request, jsonify, redirect
from app import app
from app.models import save_url, get_url, increment_click
from config import Config


def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def validate_url(url):
    regex = re.compile(
        r'^(https?://)?'  # http:// or https://
        r'([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'  # domain
        r'(/.*)?$'
    )
    return re.match(regex, url)


@app.route("/api/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "Missing URL"}), 400

    original_url = data["url"].strip()
    if not validate_url(original_url):
        return jsonify({"error": "Invalid URL"}), 400

    short_code = generate_short_code()
    save_url(short_code, original_url)
    short_url = f"{Config.BASE_URL}/{short_code}"
    return jsonify({"short_code": short_code, "short_url": short_url}), 201


@app.route("/<short_code>", methods=["GET"])
def redirect_url(short_code):
    record = get_url(short_code)
    if not record:
        return jsonify({"error": "Short URL not found"}), 404
    increment_click(short_code)
    return redirect(record["url"], code=302)


@app.route("/api/stats/<short_code>", methods=["GET"])
def stats(short_code):
    record = get_url(short_code)
    if not record:
        return jsonify({"error": "Short URL not found"}), 404

    return jsonify({
        "url": record["url"],
        "clicks": record["clicks"],
        "created_at": record["created_at"]
    }), 200
