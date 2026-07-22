# Expense Tracker

A web application built with Python and Django that helps users track, manage, and organize their personal expenses.

## Features

- 🔐 **User Authentication** — Sign up, log in, and manage personal accounts
- 💰 **Expense Tracking** — Add, edit, and delete expense entries
- 📊 **Expense Overview** — View spending history in an organized format
- 🖼️ **Media Handling** — Support for uploaded images (e.g., receipts)
- 💻 **Admin Panel** — Manage users and records via Django admin

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite
- **Frontend:** HTML, CSS
- **Deployment:** Render

## Project Structure

```
mysite/
├── manage.py
├── mysite/          # Project settings, URLs, WSGI/ASGI config
└── myapp/           # Core expense tracking logic
```

## Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation

1. Clone the repository
```bash
git clone https://github.com/addy-1922/Expense-Tracker.git
cd Expense-Tracker/mysite
```

2. Create and activate a virtual environment
```bash
python -m venv env
source env/Scripts/activate   # On Windows (Git Bash)
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Start the development server
```bash
python manage.py runserver
```

6. Visit `http://127.0.0.1:8000/` in your browser

## Live Demo

🔗 [Live Site](#) *(add your Render deployment link here)*

## Screenshots

*(Add screenshots of your dashboard, add-expense form, and summary view here)*

## Future Improvements

- Monthly/yearly spending charts and analytics
- Category-wise expense filtering
- Budget limits and alerts
- Export expenses to CSV/PDF

## Author

**Aditya Naik**
- GitHub: [@addy-1922](https://github.com/addy-1922)

## License

This project is open source and available for learning purposes.
