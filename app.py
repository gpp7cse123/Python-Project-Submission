import os
import re
import uuid
import base64
from pathlib import PurePosixPath
from urllib.parse import quote

import requests
from flask import Flask, request, render_template_string

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 25 * 1024 * 1024

GITHUB_OWNER = os.environ.get("GH_OWNER")
GITHUB_REPO = os.environ.get("GH_REPO")
GITHUB_TOKEN = os.environ.get("GH_TOKEN")

MAX_TOTAL_SIZE = 20 * 1024 * 1024
MAX_FILE_SIZE = 5 * 1024 * 1024
MAX_FILES = 100

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Python Project Submission</title>

<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f1f5f9;
    color: #172033;
}

.card {
    max-width: 600px;
    margin: 45px auto;
    padding: 30px;
    background: white;
    border-radius: 18px;
    box-shadow: 0 10px 35px #00000012;
}

h1 { margin-bottom: 8px; }

p {
    color: #64748b;
    line-height: 1.6;
}

label {
    display: block;
    margin: 18px 0 7px;
    font-weight: bold;
}

input {
    width: 100%;
    padding: 12px;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
}

.folder-box {
    padding: 18px;
    border: 2px dashed #94a3b8;
    border-radius: 12px;
    background: #f8fafc;
}

button {
    width: 100%;
    margin-top: 22px;
    padding: 14px;
    background: #2563eb;
    color: white;
    border: 0;
    border-radius: 9px;
    font-size: 16px;
    cursor: pointer;
}

button:disabled {
    background: #94a3b8;
    cursor: wait;
}

.message {
    margin-top: 20px;
    overflow-wrap: anywhere;
}

.success { color: #15803d; }
.error { color: #b91c1c; }

@media (max-width: 640px) {
    .card { margin: 18px; padding: 22px; }
}
</style>
</head>

<body>
<main class="card">
    <h1>Python Project Submission</h1>
    <p>Session 2026–27 · Upload your complete Python project folder.</p>

    <form id="submissionForm" method="POST"
          enctype="multipart/form-data">

        <label for="student">Student name</label>
        <input id="student" name="student"
               maxlength="80" required>

        <label for="roll">Roll number</label>
        <input id="roll" name="roll"
               maxlength="30" required>

        <label for="title">Project title</label>
        <input id="title" name="title"
               maxlength="100" required>

        <label for="folder">Select complete project folder</label>
        <div class="folder-box">
            <input id="folder" type="file"
                   webkitdirectory directory multiple required>
            <p id="fileInfo">Select your project folder. Its files and
            subfolders will be uploaded.</p>
        </div>

        <button id="submitBtn" type="submit">
            Submit Project
        </button>
    </form>

    <div id="status" class="message" role="status"></div>
</main>

<script>
const form = document.getElementById("submissionForm");
const folderInput = document.getElementById("folder");
const fileInfo = document.getElementById("fileInfo");
const submitBtn = document.getElementById("submitBtn");
const statusBox = document.getElementById("status");

folderInput.addEventListener("change", () => {
    const files = Array.from(folderInput.files);
    fileInfo.textContent = files.length
        ? files.length + " files selected"
        : "No folder selected";
});

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const files = Array.from(folderInput.files);

    if (!files.length) {
        statusBox.textContent = "Please select your project folder.";
        statusBox.className = "message error";
        return;
    }

    const data = new FormData(form);

    // Send every file with its relative folder path.
    for (const file of files) {
        data.append("files", file, file.webkitRelativePath);
    }

    submitBtn.disabled = true;
    submitBtn.textContent = "Uploading...";
    statusBox.textContent = "Please wait while your project is uploaded.";

    try {
        const response = await fetch("/", {
            method: "POST",
            body: data
        });

        const result = await response.json();

        statusBox.textContent = result.message;
        statusBox.className = "message " +
            (result.success ? "success" : "error");

        if (result.success) {
            form.reset();
            fileInfo.textContent = "Select your project folder.";
        }
    } catch (error) {
        statusBox.textContent =
            "Connection problem. Please try again.";
        statusBox.className = "message error";
    } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = "Submit Project";
    }
});
</script>
</body>
</html>
"""


def clean_name(value):
    value = re.sub(r"[^A-Za-z0-9_-]", "_", value.strip())
    return value[:60] or "student"


def json_message(message, success=False, status=400):
    from flask import jsonify
    return jsonify({"success": success, "message": message}), status


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template_string(HTML)

    if not all([GITHUB_OWNER, GITHUB_REPO, GITHUB_TOKEN]):
        return json_message(
            "Server configuration is incomplete.", status=500
        )

    student = request.form.get("student", "").strip()
    roll = request.form.get("roll", "").strip()
    title = request.form.get("title", "").strip()
    files = request.files.getlist("files")

    if not student or not roll or not title or not files:
        return json_message("Please complete all fields.")

    if len(student) > 80 or len(roll) > 30 or len(title) > 100:
        return json_message("One or more fields are too long.")

    if len(files) > MAX_FILES:
        return json_message(
            f"Maximum {MAX_FILES} files are allowed."
        )

    # Validate and prepare file paths before uploading anything.
    prepared = []
    total_size = 0
    skipped = {".git", ".venv", "venv", "__pycache__", "node_modules"}

    for uploaded in files:
        original_path = uploaded.filename.replace("\\", "/")
        path = PurePosixPath(original_path)

        if (
            not original_path
            or path.is_absolute()
            or ".." in path.parts
            or not path.parts
        ):
            return json_message("An invalid file path was detected.")

        # Ignore common environment/version-control folders.
        if any(part.lower() in skipped for part in path.parts):
            continue

        # Ignore empty directory entries.
        if original_path.endswith("/"):
            continue

        content = uploaded.read()
        size = len(content)

        if size > MAX_FILE_SIZE:
            return json_message(
                f"{path.name} exceeds the 5 MB per-file limit."
            )

        total_size += size

        if total_size > MAX_TOTAL_SIZE:
            return json_message(
                "Total project size must not exceed 20 MB."
            )

        # Keep the project's relative directory structure.
        safe_parts = [
            clean_name(part) if part in ("", ".", "..")
            else re.sub(r"[^A-Za-z0-9._ -]", "_", part)
            for part in path.parts
        ]

        if any(part in ("", ".", "..") for part in safe_parts):
            return json_message("An invalid folder structure was found.")

        prepared.append((safe_parts, content))

    if not prepared:
        return json_message("No project files were found to upload.")

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    submission_id = uuid.uuid4().hex[:8]
    root_folder = (
        "Session-2026-27/"
        + clean_name(roll) + "_"
        + clean_name(student) + "_"
        + submission_id
    )

    uploaded_count = 0

    try:
        for relative_parts, content in prepared:
            relative_path = "/".join(relative_parts)
            repo_path = f"{root_folder}/{relative_path}"

            url = (
                f"https://api.github.com/repos/{GITHUB_OWNER}/"
                f"{GITHUB_REPO}/contents/{quote(repo_path, safe='/')}"
            )

            payload = {
                "message": (
                    f"Project submission: {clean_name(title)} "
                    f"({uploaded_count + 1})"
                ),
                "content": base64.b64encode(content).decode("ascii")
            }

            response = requests.put(
                url, headers=headers, json=payload, timeout=30
            )

            if response.status_code not in (200, 201):
                app.logger.error(
                    "GitHub upload failed: %s %s",
                    response.status_code,
                    response.text[:500]
                )

                if uploaded_count:
                    return json_message(
                        f"{uploaded_count} files uploaded, but another "
                        "file failed. Contact the project coordinator.",
                        status=502
                    )

                return json_message(
                    "GitHub upload failed. Please contact the coordinator.",
                    status=502
                )

            uploaded_count += 1

        repo_url = (
            f"https://github.com/{GITHUB_OWNER}/"
            f"{GITHUB_REPO}/tree/HEAD/"
            f"{quote(root_folder, safe='/')}"
        )

        from flask import jsonify
        return jsonify({
            "success": True,
            "message": (
                f"Project submitted successfully! "
                f"{uploaded_count} files uploaded. "
                f"Open your project: {repo_url}"
            )
        })

    except requests.RequestException:
        app.logger.exception("GitHub request failed")
        return json_message(
            "Connection problem while uploading. Contact the coordinator.",
            status=502
        )


@app.errorhandler(413)
def too_large(error):
    return {
        "success": False,
        "message": "Upload is too large. Please reduce the project size."
    }, 413


if __name__ == "__main__":
    app.run(debug=False)