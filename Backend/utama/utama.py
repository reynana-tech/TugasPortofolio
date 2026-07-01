from flask import Blueprint, render_template, jsonify
from model import get_db

utama_bp = Blueprint('utama', __name__)


@utama_bp.route('/health')
def health():
    try:
        conn = get_db()
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
        conn.close()
        return jsonify({'success': True, 'status': 'ok', 'database': 'connected'})
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return jsonify({'success': True, 'status': 'ok', 'database': 'disconnected'}), 200


@utama_bp.route('/api/profile')
def api_profile():
    try:
        conn = get_db()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM profiles ORDER BY id DESC LIMIT 1")
                profile = cur.fetchone()
            return jsonify({'success': True, 'data': profile})
        finally:
            conn.close()
    except Exception as e:
        print(f"❌ Error fetching profile: {e}")
        return jsonify({'success': False, 'error': str(e), 'data': None}), 500


@utama_bp.route('/api/skills')
def api_skills():
    try:
        conn = get_db()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM skills ORDER BY category, level DESC")
                skills = cur.fetchall()
            return jsonify({'success': True, 'data': skills if skills else []})
        finally:
            conn.close()
    except Exception as e:
        print(f"❌ Error fetching skills: {e}")
        return jsonify({'success': False, 'error': str(e), 'data': []}), 500


@utama_bp.route('/api/experiences')
def api_experiences():
    try:
        conn = get_db()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM experiences ORDER BY is_current DESC, id DESC")
                exps = cur.fetchall()
            return jsonify({'success': True, 'data': exps if exps else []})
        finally:
            conn.close()
    except Exception as e:
        print(f"❌ Error fetching experiences: {e}")
        return jsonify({'success': False, 'error': str(e), 'data': []}), 500


@utama_bp.route('/api/projects')
def api_projects():
    try:
        conn = get_db()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM projects ORDER BY is_featured DESC, id DESC")
                projects = cur.fetchall()
            return jsonify({'success': True, 'data': projects if projects else []})
        finally:
            conn.close()
    except Exception as e:
        print(f"❌ Error fetching projects: {e}")
        return jsonify({'success': False, 'error': str(e), 'data': []}), 500

