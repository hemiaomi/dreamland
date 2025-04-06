from flask import Flask, request
from datetime import datetime
import os  

app = Flask(__name__)

@app.route("/phone")
def track():
    ip = request.remote_addr
    user_agent = request.headers.get("User-Agent")
    source = request.args.get("source", "unknown")
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.now()} | {ip} | {source} | {user_agent}\n")
    
    return """
    <h2 style='text-align:center; margin-top:30vh;'> phone number:  +39 320 187 2827
    <p style='text-align:center;'>Your access has been logged.</p>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
