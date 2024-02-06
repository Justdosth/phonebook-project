# Django Phonebook Project

A simple phonebook application built with Django.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)

## Getting Started

### Prerequisites

- Python (version 3.x recommended)
- Django (install via `pip install django`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/justdosth/phonebook-project.git
   cd phonebook-project
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at `http://127.0.0.1:8000/phonebook/`.

## Usage

- Visit `http://127.0.0.1:8000/phonebook/contacts/` to view the contact list.
- Visit `http://127.0.0.1:8000/phonebook/add_contact/` to add a new contact.

## Folder Structure

- `phonebook_project/`: Django project root.
- `phonebook_app/`: Django app containing models, views, and templates.
- `templates/`: HTML templates.
- `static/`: Static files (CSS, JavaScript, images).

## Contributing

1. Fork the project.
2. Create a new branch (`git checkout -b feature/add-new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/add-new-feature`).
5. Open a pull request.
