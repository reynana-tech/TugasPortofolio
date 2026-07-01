"""
WSGI entry point for Vercel
"""
import os
import sys

# Ensure the app module can be imported
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app

# Export the app for Vercel
application = app

@app.route('/api/health')
def health_check():
    return {'status': 'ok'}, 200

if __name__ == '__main__':
    app.run()
