# Brave Distro Framework

**Brave Distro Framework** i sa high-level Python web framework built with Django that encourages rapid development for project in MusicTech industry

## Table of Contents

- [Brave Distro](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Clone the Repository](#clone-the-repository)
    - [Virtual Environment Setup](#virtual-environment-setup)
    - [Install Dependencies](#install-dependencies)
    - [Database Setup](#database-setup)
    - [Running the Server](#running-the-server)
  - [Usage](#usage)
    - [Admin Interface](#admin-interface)
    - [User Interface](#user-interface)
  - [Running Tests](#running-tests)
  - [Deployment](#deployment)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- virtualenv (Recommended for virtual environment management)
- Git

### Clone the Repository

```bash
git clone https://github.com/bravelab/brave-distro.git
cd brave-distro
```

### Virtual Environment Setup

Create a virtual environment to manage dependencies:

```bash
virtualenv venv
```

Activate the virtual environment:

- On Windows:

  ```bash
  venv\Scripts\activate
  ```

- On macOS and Linux:

  ```bash
  source venv/bin/activate
  ```

### Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Database Setup

Apply migrations to set up your database:

```bash
python manage.py migrate
```
<!-- 
(Optional) Load initial data if available:

```bash
python manage.py loaddata initial_data.json
``` -->

### Running the Server

Start the Django development server:

```bash
export DEVELOPMENT_MODE=True
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your web browser to see the application running.

## Demo data
If you want to load demo data you can use this fixtures
```python manage.py loaddata labels.json artists.json tracks.json lyrics.json notifications.json participants.json participantsroles.json platforms.json links.json```

## Usage

### Admin Interface

To access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the superuser credentials. Then, log in to the admin interface at `http://127.0.0.1:8000/admin/`.

### User Interface

The main user interface is accessible at `http://127.0.0.1:8000/`. Detailed usage instructions can be added here based on the project specifics.

## Running Tests

To run the tests for this project:

```bash
python manage.py test
```

Ensure all tests pass successfully before making any contributions.

## Deployment

For deployment, refer to Django's official deployment documentation: [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)

Some typical steps include:

- Setting `DEBUG = False` in `settings.py`
- Configuring allowed hosts
- Setting up a production-ready web server (e.g., Gunicorn, Nginx)
- Using a production-ready database (e.g., PostgreSQL)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a new Pull Request

Please ensure your code adheres to the project's coding standards and passes all tests.

## License

This project is licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

<div align="center">
  Bravelab. Digital Commerce Solution For The Music Industry<br>
  <a href="https://www.bravelab.io/">Website</a>
  <span> | </span>
  <a href="https://linkedin.com/company/bravelab.io">LinkdedIn</a><span> | </span>
  <a href="mailto:office@bravelab.io">Let's talk</a><br>
  Crafted by https://www.bravelab.io
</div>

