from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Vercel looks for this
def handler(request, context):
    return app(request.environ, context.start_response)