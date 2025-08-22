from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>🚀 Perfect Cloud Desktop</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                text-align: center;
            }}
            .container {{
                background: rgba(255,255,255,0.1);
                padding: 30px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255,255,255,0.2);
                max-width: 600px;
                margin: 0 auto;
            }}
            h1 {{ color: white; }}
            .status {{
                background: #48bb78;
                padding: 15px;
                border-radius: 8px;
                margin: 20px 0;
            }}
            .btn {{
                background: #4299e1;
                color: white;
                padding: 15px 30px;
                text-decoration: none;
                border-radius: 6px;
                display: inline-block;
                margin: 10px;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Cloud Desktop Active</h1>
            <div class="status">✅ System Online - Perfect Setup!</div>
            
            <p><strong>Computer:</strong> {socket.gethostname()}</p>
            <p><strong>Port:</strong> 8080</p>
            
            <a href="http://localhost:4040" class="btn" target="_blank">📊 Ngrok Dashboard</a>
            
            <div style="margin-top: 30px;">
                <p>Your cloud desktop is running perfectly! 🎉</p>
                <p>Accessible from anywhere in the world 🌍</p>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    print("✅ Perfect Cloud Desktop Starting...")
    print("📍 http://localhost:8080")
    app.run(host='0.0.0.0', port=8080, debug=False)
