# app.py
# Error Handling
from app import app
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/handle_error')
def handle_error():
    try:
        # Code that might raise an error
        pass  # Placeholder for your code
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return render_template('error.html', error_message=str(e)), 500
