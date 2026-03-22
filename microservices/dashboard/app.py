from flask import Flask, render_template_string, jsonify
import os
import subprocess

app = Flask(__name__)

# Simple in-memory "results" (in real demo, read from files/volumes)
scan_results = "No scan yet"
ai_results = "No AI run yet"

@app.route('/')
def dashboard():
    html = """
    <html>
    <head><title>AppSec Resilience Dashboard</title>
    <style>
        body { font-family: Arial; background: #f0f4f8; padding: 20px; }
        h1 { color: #2c3e50; }
        .status { padding: 15px; margin: 10px; border-radius: 8px; }
        .green { background: #d4edda; color: #155724; }
        .red { background: #f8d7da; color: #721c24; }
        button { padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
    </style>
    </head>
    <body>
        <h1>AppSec Resilience Demo Dashboard</h1>

        <div class="status green">
            <h2>Service Status</h2>
            <p>User Service: <strong>OK</strong></p>
            <p>Payment Service: <strong>OK</strong></p>
            <p>Frontend: <strong>OK</strong></p>
        </div>

        <div class="status">
            <h2>Pipeline Security Scan Results</h2>
            <pre>{{ scan_results }}</pre>
        </div>

        <div class="status">
            <h2>AI Anomaly Detection</h2>
            <pre>{{ ai_results }}</pre>
            <button onclick="location.href='/run-ai'">Run AI Demo Now</button>
        </div>

        <p><a href="https://github.com/yourusername/appsec-resilience-demo">View Source on GitHub</a></p>
    </body>
    </html>
    """
    return render_template_string(html, scan_results=scan_results, ai_results=ai_results)

@app.route('/run-ai')
def run_ai():
    global ai_results
    try:
        result = subprocess.check_output(['python', '/app/anomaly_demo.py'], text=True)
        ai_results = result
    except Exception as e:
        ai_results = f"Error: {str(e)}"
    return dashboard()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)