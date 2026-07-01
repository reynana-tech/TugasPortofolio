import os
from flask import Flask, render_template, send_from_directory
from config import Config
from model import get_profiles, get_skills, get_projects, get_experience
from jinja2 import ChoiceLoader, FileSystemLoader

# Get the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit untuk upload
app.secret_key = Config.SECRET_KEY

# Halaman utama (public portfolio)
@app.route("/")
def home():
    try:
        profiles    = get_profiles() if get_profiles() else []
        skills      = get_skills() if get_skills() else []
        projects    = get_projects() if get_projects() else []
        experience  = get_experience() if get_experience() else []
        return render_template("index.html",
            profiles=profiles,
            skills=skills,
            projects=projects,
            experience=experience
        )
    except Exception as e:
        print(f"❌ Error in home route: {e}")
        return render_template("index.html",
            profiles=[],
            skills=[],
            projects=[],
            experience=[]
        ), 200  # Return 200 even if there's an error to avoid 500

# Register blueprints untuk admin
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
        return '', 204  # No Content

# Initialize database on first request (for Vercel cold starts)
_db_initialized = False

@app.before_request
def init_db_on_startup():
    global _db_initialized
    if not _db_initialized:
        try:
            from model import init_db
            init_db()
            _db_initialized = True
            print("✅ Database tables initialized.")
        except Exception as e:
            print(f"⚠️  Database init error: {e}")
            # Don't fail the request, just log the error

# Global error handlers
@app.errorhandler(404)
def not_found(error):
    return {"error": "Not found"}, 404

@app.errorhandler(500)
def internal_error(error):
    print(f"Internal server error: {error}")
    return {"error": "Internal server error"}, 500

if __name__ == '__main__':
    try:
        from model import init_db
        init_db()
        print("✅ Database tables initialized.")
    except Exception as e:
        print(f"⚠️  Database init error: {e}")

    app.run(debug=True, host='0.0.0.0', port=5000)

