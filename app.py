from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "dev-secret-key"  # change before production

# Sample dynamic data
posts = [
    {"title": "My First Post", "content": "This is my first blog post — built with Flask."},
    {"title": "Learning Flask", "content": "Today I learned about templates, static files and forms."}
]

projects_list = [
    {"title": "Flask Blog", "summary": "A simple blog built with Flask and SQLite (prototype)."},
    {"title": "Weather App", "summary": "Fetches weather using a public API and displays forecasts."},
    {"title": "Portfolio Site", "summary": "This portfolio website showcasing projects and skills."}
]

messages = []  # store contact form submissions in-memory for demo

@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html", projects=projects_list)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()
        if not name or not email or not message:
            flash("Please fill all fields.", "danger")
            return redirect(url_for("contact"))
        # Save message (in-memory). In real app save to DB or send email.
        messages.append({"name": name, "email": email, "message": message})
        flash("Thank you! Your message has been received.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
