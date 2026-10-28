
# 🎓 Student Project Submission Portal

A web-based application developed using Python and Flask that allows students to submit their academic projects online. The portal collects student details and project files, with submissions intended to be stored in a dedicated GitHub repository folder.

<p align="center">
  <strong>Academic Session: 2026–27</strong>
</p>

---

## 🌐 Live Website

**Visit the portal:**  
https://python-project-submission.onrender.com/

## 📌 About the Project

The Student Project Submission Portal is designed to make the process of collecting student projects more organised and convenient.

Students can enter their name, roll number, and project title, then select their project folder for submission. The application uses Flask for the web application and the GitHub API for storing submitted project files.

## ✨ Features

- Student name and roll number collection
- Project title submission
- Project folder upload
- Organised storage by academic session
- GitHub integration for project-file storage
- Online hosting through Render
- Simple web interface for students

> Note: Successful file storage depends on the live application's configuration and the submission completing successfully.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Web framework |
| HTML | Webpage structure |
| CSS | Styling and layout |
| JavaScript | Client-side interactions |
| GitHub API | Project-file storage |
| Render | Web application hosting |
| Gunicorn | Production application server |

## ⚙️ Project Structure

```text
Python-Project-Submission/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
└── Session-2026-27/
    └── Student_Submission_Folder/
        └── Project_Files/
```

*The `Session-2026-27` folder contains submitted projects when uploads are successfully saved there. The displayed structure is illustrative.*

## 🚀 Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/gpp7cse123/Python-Project-Submission.git
```

### 2. Open the Project Directory

```bash
cd Python-Project-Submission
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Configure the following variables in your local environment:

- `GH_OWNER` — GitHub repository owner
- `GH_REPO` — GitHub repository name
- `GH_TOKEN` — GitHub access token with the required repository permissions

Never put the actual token in this README or commit it to GitHub.

### 6. Start the Application

```bash
python app.py
```

Open the local address shown in the terminal. For a typical Flask development setup, this is:

http://127.0.0.1:5000/

## ☁️ Deployment on Render

The application is hosted on Render.

Typical deployment configuration:

- **Build command:** `pip install -r requirements.txt`
- **Start command:** `gunicorn app:app`

Configure the required environment variables in the Render dashboard. Keep all secret values private.

## 📂 Project Storage

Submitted project files are intended to be stored in the GitHub repository:

**Repository:**  
https://github.com/gpp7cse123/Python-Project-Submission

**Target directory:**  
`Session-2026-27/`

Each successful submission is intended to have its own uniquely named folder containing the submitted project files.

The Render service hosts the web application; GitHub is the intended storage location for submitted files.

## 🔒 Security and Usage Guidelines

- Submit only your own academic projects.
- Verify your name, roll number, and project title before submission.
- Do not upload passwords, API keys, access tokens, or confidential files.
- Keep the GitHub access token in environment variables.
- Check repository visibility before accepting real student submissions.
- Files stored in a public GitHub repository may be accessible to anyone.

## 🎯 Project Objectives

- Simplify the student project submission process.
- Keep submitted projects organised.
- Reduce the need to collect project files manually.
- Use Python web development and GitHub integration to manage submissions.

## 👨‍💻 Repository

**GitHub:**  
https://github.com/gpp7cse123/Python-Project-Submission

---

<p align="center">
  <strong>Student Project Submission Portal</strong><br>
  Academic Session 2026–27
</p>
