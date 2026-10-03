# Mikhail Rapada — Personal Portfolio

A Django-based personal portfolio showcasing my projects, tutoring experience, and testimonials, with an admin-only dashboard for managing content.

**Live site:** [add PythonAnywhere URL here once deployed]

## Features

- Public portfolio pages: Home, Projects (list + detail), Tutoring (view only), About Me (view only), Testimonies (form + list + detail), Contact (form)
- Visitors can leave testimonials and send inquiries through the Contact page
- Admin-only sign-in (superuser accounts only — regular users cannot access it)
- Protected `/dashboard` for the site owner to:
  - View all Projects and Tech Stacks in table form
  - Add new Projects (with multiple tech stacks selectable via checkboxes)
  - Add new Tech Stacks
- New content added through the dashboard automatically appears on the public portfolio

## Tech Stack

- Python 3.9
- Django 4.2
- SQLite (local development database)
- python-dotenv (environment variable management)

## Setup Instructions

These steps will get the project running from a fresh clone, including an empty database that you'll need to set up yourself.

### 1. Clone the repository
`git clone https://github.com/mikhail-rapada2007/Portfolio.git`

`cd Portfolio`


### 2. Create and activate a virtual environment
`python -m venv .venv`

Windows:
`.venv\Scripts\activate`

macOS/Linux:
`source .venv/bin/activate`


### 3. Install dependencies
`pip install -r requirements.txt`


### 4. Set up environment variables
Duplicate the `.env.example` and rename it as a new file named `.env` in the project root.

Open `.env` and fill in the values:
`SECRET_KEY=your-generated-secret-key-here`
`DEBUG=True`
`ALLOWED_HOSTS=127.0.0.1,localhost`

To generate a SECRET_KEY, run:
`python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

Copy the printed value into `.env`.


### 5. Run migrations
The repository does not include a database file. This builds the required tables from scratch:
`python manage.py migrate`


### 6. Create a superuser (admin) account
This is required — without it, you cannot log into the admin dashboard, since only superuser accounts are permitted to sign in.
Run the following line in the terminal:

`python manage.py createsuperuser`

Follow the prompts to set a username, email (optional), and password.


### 7. Run the development server
run: `python manage.py runserver`

Then visit `http://127.0.0.1:8000/` in your browser.

## Important Notes

- **The database starts empty.** No projects, tech stacks, or testimonies will appear on the portfolio until you add some. You can add data two ways:
  - Through Django's built-in admin panel at `/admin/` (log in with your superuser account)
  - Through the custom dashboard at `/dashboard/` (after logging in via `/admin-login/`)
- **Add Tech Stacks First.** In the admin dashboard, an admin cannot create a project since tech stacks must exist first so that they may be selected.
- **The Admin Login is Hidden.** The admin login is hidden in the word 'tech' in the technology word of my short description.
- **Only superuser accounts can access the admin dashboard.** Regular registered users, even if created, cannot sign in through `/admin-login/`.
- **Tech Stack selection on the Create Project form uses checkboxes, not radio buttons.** This is intentional: a single project can use multiple tech stacks, and radio buttons only allow selecting one option at a time, so checkboxes were used to correctly support multiple selections.


## Key URLs

| URL | Description |
|---|---|
| `/` | Home page |
| `/projects/` | Project list |
| `/projects/<id>/` | Project detail |
| `/projects/add/` | Add a project (admin only) |
| `/tutoring/` | Tutoring page |
| `/about/` | About Me |
| `/testimonies/` | Testimony list |
| `/testimonies/<id>/` | Testimony detail |
| `/testimonies/add/` | Leave a testimony (public) |
| `/contact/` | Contact / inquiry form (public) |
| `/admin-login/` | Admin sign-in |
| `/admin-logout/` | Admin sign-out |
| `/dashboard/` | Admin dashboard (admin only) |
| `/dashboard/add-tech-stack/` | Add a tech stack (admin only) |
| `/admin/` | Django's built-in admin panel |

