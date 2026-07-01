from flask import Flask, render_template, send_from_directory
import os
from config import Config
from jinja2 import ChoiceLoader, FileSystemLoader

# Import blueprints will be registered after app creation using factory below

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def create_app():
    app = Flask(
        __name__,
        static_folder=os.path.join(BASE_DIR, 'Frontend'),
        static_url_path='/static',
        template_folder=BASE_DIR
    )

    # Tambahkan loader untuk root dan Frontend
    app.jinja_loader = ChoiceLoader([
        FileSystemLoader(BASE_DIR),
        FileSystemLoader(os.path.join(BASE_DIR, 'Frontend'))
    ])

    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
    app.secret_key = Config.SECRET_KEY

    # Secure cookies di production
    if Config.FLASK_ENV == 'production':
        app.config.update(SESSION_COOKIE_SECURE=True, SESSION_COOKIE_SAMESITE='Lax')

    # Register blueprints (importing here to avoid circular imports at module load)
    from Backend.utama.utama import utama_bp
    from Backend.admin.login import login_bp
    from Backend.admin.dashboard import dashboard_bp
    from Backend.admin.profiles import profiles_bp
    from Backend.admin.skills import skills_bp
    from Backend.admin.experience import experience_bp
    from Backend.admin.projects import projects_bp
    from Backend.admin.upload import upload_bp
    from Backend.admin.contact import contact_bp

    app.register_blueprint(utama_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(profiles_bp)
    app.register_blueprint(skills_bp)
    app.register_blueprint(experience_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(upload_bp)
    app.register_blueprint(contact_bp)

    # Favicon
    @app.route('/favicon.ico')
    def favicon():
        favicon_path = os.path.join(BASE_DIR, 'favicon.ico')
        if os.path.exists(favicon_path):
            return send_from_directory(BASE_DIR, 'favicon.ico', mimetype='image/vnd.microsoft.icon')
        else:
            return '', 204

    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return {"error": "Not found"}, 404

    @app.errorhandler(500)
    def internal_error(error):
        print(f"Internal server error: {error}")
        return {"error": "Internal server error"}, 500

    return app


# Expose WSGI/ASGI app for hosting platforms (Vercel expects a top-level `app` object)
app = create_app()


if __name__ == '__main__':
    try:
        from model import init_db
        init_db()
        print("✅ Database tables initialized.")
    except Exception as e:
        print(f"⚠️  Database init error: {e}")
    app.run(debug=True, host='0.0.0.0', port=5000)
