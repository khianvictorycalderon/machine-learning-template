from flask import Flask

# Initiate the app
app = Flask(__name__)

# Test
@app.route("/health")
def home():
    return {
        "status": "AI service healthy"
    }, 200

# Your AI inferencing here...
# You may create other files such as train.py, fine_tuning.py, etc... outside of this "api" folder.