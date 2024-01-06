from InstagramGrabber import Instagram
from utils import helper
from flask import jsonify, request
from dotenv import load_dotenv
import os
import json

load_dotenv()

class InstagramController:
    def __init__(self):
        self.username = os.environ.get("IG_USERNAME", None)
        password = os.environ.get("IG_PASSWORD", None)
        
        self.instagram = Instagram(username=self.username, password=password)

    def index(self):
        if request.is_json:
            data = request.get_json()
            target_url = data.get('target_url')
        else:
            target_url = request.form.get('target_url')
        if target_url is None:
            return jsonify({"status":False, "message": "target_url is required"}), 400
        if "instagram.com" not in target_url:
            return jsonify({"status":False, "message": f"invalid url '{target_url}'"}), 400
        try:
            check_login = self.instagram.login()
            if check_login['username'] != self.username:
                return jsonify({"status": False, "message": "something wen't wrong"}), 400
        except Exception as e:
            if "checkpoint" in str(e):
                return jsonify({"status":False, "message": f"checkpoint detected. please contact developers for information"}), 400
            return jsonify({"status": False, "message": "someting wen't wrong, please try again latter"}), 400
        try:
            url_type, data_url = helper.instagram_url_type(target_url)
            if url_type == "reel" or url_type == "post":
                response = self.instagram.get_post(url=f"https://www.instagram.com/p/{data_url}")
                user = response.user
                media = response.media
            elif url_type == "stories":
                user = self.instagram.get_user(data_url)
                media = user.get_stories().media
            else:
                return jsonify({"status":False, "message": f"invalid url '{target_url}'"}), 400
            if not media:
                media = None
            else:
                media = media.json
            result_data = {
                "user": {
                    "user id": int(user.user_id),
                    "username": user.username,
                    "full name": user.full_name,
                    "category name": user.category_name,
                    "biography": user.biography,
                    "jumlah following": user.following,
                    "jumlah followers": user.followers,
                    "jumlah responses": user.posts_count,
                    "profile picture": user.profile_picture,
                },
                "items": media
            }
            return jsonify({"status": True, "result": result_data}), 200
        except Exception as e:
            return jsonify({"status":False, "message": str(e)}), 400