from flask import Blueprint
from flask_file_routes import ModuleView


auth_blueprint = Blueprint("auth", __name__, template_folder="templates")

ModuleView("hyperflask_auth.pages.connect", "auth/connect.html", endpoint="connect").register(auth_blueprint, "/connect", methods=["GET", "POST"])
ModuleView("hyperflask_auth.pages.login", "auth/login.html", endpoint="login").register(auth_blueprint, "/login", methods=["GET", "POST"])
ModuleView("hyperflask_auth.pages.login_link", "auth/login_link.html", endpoint="login_link").register(auth_blueprint, "/login/link", methods=["GET", "POST"])
ModuleView("hyperflask_auth.pages.signup", "auth/signup.html", endpoint="signup").register(auth_blueprint, "/signup", methods=["GET", "POST"])
ModuleView("hyperflask_auth.pages.forgot_password", "auth/forgot_password.html", endpoint="forgot_password").register(auth_blueprint, "/login/forgot", methods=["GET", "POST"])
ModuleView("hyperflask_auth.pages.reset_password", "auth/reset_password.html", endpoint="reset_password").register(auth_blueprint, "/login/reset", methods=["GET", "POST"])
ModuleView("hyperflask_auth.pages.logout", None, endpoint="logout").register(auth_blueprint, "/logout", methods=["GET"])
