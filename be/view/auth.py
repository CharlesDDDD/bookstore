from flask import Blueprint
from flask import request
from flask import jsonify
from be.model import user
from flask import render_template

bp_auth = Blueprint("auth", __name__, url_prefix="/auth")


@bp_auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        terminal = request.form['terminal']
        # user_id = request.json.get("user_id", "")
        # password = request.json.get("password", "")
        # terminal = request.json.get("terminal", "")
        u = user.Users()
        code, message, token = u.login(user_id=user_id, password=password, terminal=terminal)
        return jsonify({"message": message, "token": token}), code
    else:
        return render_template("login.html")


@bp_auth.route("/logout", methods=["POST"])
def logout():
    user_id: str = request.json.get("user_id")
    token: str = request.headers.get("token")
    u = user.Users()
    code, message = u.logout(user_id=user_id, token=token)
    return jsonify({"message": message}), code


@bp_auth.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        # user_id = request.json.get("user_id", "")
        # password = request.json.get("password", "")
        u = user.Users()
        code, message = u.register(user_id=user_id, password=password)
        print(message)
        return jsonify({"message": message}), code
    else:
        return render_template("register.html")


@bp_auth.route("/unregister", methods=["POST"])
def unregister():
    user_id = request.json.get("user_id", "")
    password = request.json.get("password", "")
    u = user.Users()
    code, message = u.unregister(user_id=user_id, password=password)
    return jsonify({"message": message}), code


@bp_auth.route("/password", methods=["POST"])
def change_password():
    user_id = request.json.get("user_id", "")
    old_password = request.json.get("oldPassword", "")
    new_password = request.json.get("newPassword", "")
    u = user.Users()
    code, message = u.change_password(user_id=user_id, old_password=old_password, new_password=new_password)
    return jsonify({"message": message}), code

