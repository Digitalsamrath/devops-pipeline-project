from flask import Flask, jsonify
from prometheus_client import Counter, make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

# A counter to track requests for monitoring
REQUEST_COUNTER = Counter('api_requests_total', 'Total number of API requests')

@app.route('/api/call')
def handle_call():
    REQUEST_COUNTER.inc()
    # This is our mock AI response
    return jsonify({
        "status": "ok",
        "version": "1.0",
        "response": "Namaste! This is a mock AI response."
    })

# Add Prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)