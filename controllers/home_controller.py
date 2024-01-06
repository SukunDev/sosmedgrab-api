from flask import jsonify


class HomeController:
    def index(self):
        return jsonify({"status": True, "message": "ok"}), 200