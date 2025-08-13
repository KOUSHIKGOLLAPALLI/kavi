from flask import Flask, render_template, request, redirect, url_for, jsonify
from kavi_brain import basic_chat
from kavi_commands import run_command

app = Flask(__name__)
users = [
    {'email': 'koushikgollapalli3@gmail.com', 'username': 'user', 'password': 'pass123'},
    {'email': 'admin@example.com', 'username': 'admin', 'password': 'adminpass'},
    {'email': 'alice@example.com', 'username': 'alice', 'password': 'alicepass'},
    {'email': 'bob@example.com', 'username': 'bob', 'password': 'bobpass'},
    {'email': 'charlie@example.com', 'username': 'charlie', 'password': 'charlie123'},
    {'email': 'dave@example.com', 'username': 'dave', 'password': 'dave321'},
    {'email': 'eve@example.com', 'username': 'eve', 'password': 'evepass'},
    {'email': 'rahul.sharma@example.com', 'username': 'rahul', 'password': 'rahul123'},
    {'email': 'neha.kapoor@example.com', 'username': 'neha', 'password': 'neha321'},
    {'email': 'arjun.patel@example.com', 'username': 'arjun', 'password': 'arjunpass'},
    {'email': 'priya.singh@example.com', 'username': 'priya', 'password': 'priya789'},
    {'email': 'vishal.kumar@example.com', 'username': 'vishal', 'password': 'vishal456'},
    {'email': 'sneha.desai@example.com', 'username': 'sneha', 'password': 'sneha123'},
    {'email': 'amit.mehta@example.com', 'username': 'amit', 'password': 'amitpass'},
    {'email': 'hlo@.com','username': 'hlo','password':'123'},
]


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form.get('email').strip()
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()

        if not email or not username or not password:
            error = "Please fill in all fields."
            return render_template('login.html', error=error)

        user = next((u for u in users if u['email'] == email and u['username'] == username and u['password'] == password), None)

        if user:
            return redirect(url_for('home'))
        else:
            error = "Invalid email, username, or password."

    return render_template('login.html', error=error)


@app.route('/')
def home():
    # Render main chat page (index.html)
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    query = request.json.get('query', '')

    if not query.strip():
        return jsonify({'response': "Please say something..."})

    if "exit" in query.lower() or "bye" in query.lower():
        return jsonify({'response': "Goodbye, Koushik.", 'exit': True})

    command_response = run_command(query)
    if command_response:
        return jsonify({'response': command_response})

    reply = basic_chat(query)

    if reply.lower() == "exit":
        return jsonify({'response': "Goodbye, Koushik.", 'exit': True})

    return jsonify({'response': reply})


if __name__ == '__main__':
    app.run(debug=True)
