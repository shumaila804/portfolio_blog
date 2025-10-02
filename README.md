# Portfolio Blog (Flask) - Assessment Project

This is a simple portfolio/blog demo built with Flask. It's prepared as a complete submission for a web developer assessment (10-day project).  
It includes templates, static CSS, dynamic content and a contact form.

## Structure

```
portfolio_blog_full/
├── app.py
├── requirements.txt
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── about.html
│   ├── projects.html
│   └── contact.html
└── static/
    └── style.css
```

## How to run (Windows)

1. Open Command Prompt.
2. Navigate to the project folder:
   ```
   cd %USERPROFILE%\Desktop\portfolio_blog_full
   ```
3. Create & activate venv:
   ```
   python -m venv venv
   venv\Scripts\activate.bat
   ```
4. Install requirements:
   ```
   pip install -r requirements.txt
   ```
5. Run:
   ```
   python app.py
   ```
6. Open browser: http://127.0.0.1:5000/

## What I learned
- Using Flask templates (Jinja2) to reuse a base layout.
- Serving static files (CSS) with `url_for('static', ...)`.
- Passing Python data structures (lists/dicts) to templates and rendering with loops.
- Handling simple form submissions with `request.form`.

## Challenges & Solutions
- **File extensions issue on Windows**: Notepad sometimes saved files as `.txt`. Solution: use Save As → All Files and include the `.html` extension or use VS Code.
- **Template linking**: Ensured `templates/` folder is sibling to `app.py` so Flask can locate templates.
- **Form handling**: For the assessment we store submissions in-memory; in production you'd connect to a DB or send emails.


