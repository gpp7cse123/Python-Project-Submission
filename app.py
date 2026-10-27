import os
import re
import uuid
import base64
from pathlib import PurePosixPath
from urllib.parse import quote

import requests
from flask import Flask, request, render_template_string, jsonify

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

<title>Python Project Submission Portal</title>

<style>
:root {
    --primary: #3157D5;
    --primary-dark: #1A3476;
    --text: #17213A;
    --muted: #596783;
    --border: #DCE4F7;
    --page: #F4F6FB;
    --green: #16A34A;
}

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Inter, "Segoe UI", Arial, sans-serif;
    background: var(--page);
    color: var(--text);
}

.topbar {
    background: #3157D5;
    color: white;
    padding: 17px clamp(18px, 5vw, 68px);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 18px;
    box-shadow: 0 6px 24px rgba(12, 25, 70, .12);
}

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 17px;
    font-weight: 800;
}

.logo {
    width: 42px;
    height: 42px;
    border-radius: 13px;
    display: grid;
    place-items: center;
    background: rgba(255, 255, 255, .16);
    border: 1px solid rgba(255, 255, 255, .3);
    font-size: 23px;
}

.top-tag {
    padding: 9px 13px;
    border-radius: 30px;
    border: 1px solid rgba(255, 255, 255, .35);
    background: rgba(255, 255, 255, .1);
    font-size: 11px;
    font-weight: 750;
    letter-spacing: .5px;
}

.hero {
    position: relative;
    overflow: hidden;
    padding: clamp(38px, 6vw, 76px) clamp(18px, 7vw, 100px) 46px;
    background: linear-gradient(
        115deg,
        #E9EEFF 0%,
        #F5F7FC 58%,
        #F0EFFF 100%
    );
}

.hero::after {
    content: "";
    position: absolute;
    width: 270px;
    height: 270px;
    right: 4%;
    top: -105px;
    border-radius: 50%;
    border: 42px solid rgba(49, 87, 213, .07);
    pointer-events: none;
}

.hero::before {
    content: "";
    position: absolute;
    width: 170px;
    height: 170px;
    right: 23%;
    bottom: -125px;
    border-radius: 50%;
    background: rgba(114, 151, 255, .12);
    pointer-events: none;
}

.eyebrow {
    position: relative;
    z-index: 1;
    color: #3157D5;
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1.7px;
    margin-bottom: 15px;
}

h1 {
    position: relative;
    z-index: 1;
    max-width: 700px;
    margin: 0;
    font-size: clamp(36px, 5.2vw, 58px);
    line-height: 1.08;
    letter-spacing: -2px;
    color: #17213A;
}

.hero-description {
    position: relative;
    z-index: 1;
    max-width: 630px;
    color: #5D6780;
    line-height: 1.8;
    font-size: 15px;
    margin: 18px 0 0;
}

.hero-pills {
    position: relative;
    z-index: 1;
    display: flex;
    flex-wrap: wrap;
    gap: 9px;
    margin-top: 23px;
}

.pill {
    background: white;
    border: 1px solid #DDE4FA;
    color: #34456F;
    padding: 9px 13px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 700;
}

main {
    max-width: 1240px;
    margin: auto;
    padding: 0 clamp(16px, 4vw, 48px) 55px;
}

.stats {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 15px;
    padding: 25px 0 28px;
}

.stat {
    background: white;
    border: 1px solid #E4E8F2;
    border-radius: 17px;
    padding: 18px;
    display: flex;
    align-items: center;
    gap: 12px;
    box-shadow: 0 8px 22px rgba(28, 45, 90, .035);
}

.stat-icon {
    width: 43px;
    height: 43px;
    flex-shrink: 0;
    border-radius: 13px;
    display: grid;
    place-items: center;
    background: #E0E7FF;
    color: #273B82;
    font-size: 20px;
}

.stat strong {
    display: block;
    font-size: 13px;
}

.stat span {
    display: block;
    color: #7B8498;
    font-size: 11px;
    margin-top: 5px;
}

.content-grid {
    display: grid;
    grid-template-columns: minmax(0, 1.45fr) minmax(280px, .8fr);
    gap: 23px;
    align-items: start;
}

.panel {
    background: white;
    border: 1px solid #E0E6F1;
    border-radius: 22px;
    padding: clamp(20px, 3vw, 30px);
    box-shadow: 0 12px 36px rgba(28, 45, 90, .065);
    min-width: 0;
}

.submit-area {
    position: relative;
    overflow: hidden;
    background: linear-gradient(145deg, #FFFFFF 0%, #F5F8FF 100%);
    border: 1px solid #DCE4F7;
    box-shadow: 0 18px 46px rgba(23, 37, 84, .09);
}

.submit-area::before {
    content: "";
    display: block;
    height: 4px;
    border-radius: 99px;
    background: linear-gradient(90deg, #172554, #5575E6, #9EB5FF);
    margin: -1px 0 25px;
}

.panel-head {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 24px;
}

.panel h2 {
    font-size: 21px;
    letter-spacing: -.5px;
    margin: 0;
    color: #172B50;
}

.sub {
    font-size: 13px;
    color: #536582;
    margin: 8px 0 0;
    line-height: 1.6;
}

.step-label {
    flex-shrink: 0;
    background: #E5ECFA;
    color: #273B82;
    border: 1px solid #D0DCF4;
    border-radius: 8px;
    padding: 8px 10px;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: .4px;
}

.two {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
}

.field {
    margin-bottom: 19px;
    min-width: 0;
}

.field > label {
    display: block;
    background: #E5ECFA;
    color: #24365B;
    border: 1px solid #D0DCF4;
    border-radius: 8px;
    padding: 9px 11px;
    margin-bottom: 9px;
    letter-spacing: .45px;
    font-size: 11px;
    font-weight: 800;
}

input {
    width: 100%;
    min-width: 0;
    background: #E8EDF6;
    color: #263653;
    border: 1px solid #C4CEDF;
    border-radius: 12px;
    padding: 14px 15px;
    font: inherit;
    font-size: 14px;
    outline: none;
    transition: .2s;
}

input::placeholder {
    color: #687791;
    opacity: 1;
}

input:focus {
    background: #F4F7FC;
    border-color: #6B86D9;
    box-shadow: 0 0 0 3px rgba(49, 87, 213, .12);
}

.dropzone {
    display: block;
    text-align: center;
    padding: 29px 16px;
    border: 1.5px dashed #B9C8F3;
    border-radius: 17px;
    background: #F8FAFF;
    cursor: pointer;
    transition: .2s;
}

.dropzone:hover,
.dropzone.drag {
    background: #EEF2FF;
    border-color: #3157D5;
}

.upload-icon {
    width: 54px;
    height: 54px;
    margin: 0 auto 13px;
    border-radius: 17px;
    background: #DDE8FF;
    color: #2446A0;
    display: grid;
    place-items: center;
    font-size: 27px;
}

.dropzone strong {
    display: block;
    color: #263653;
    font-size: 14px;
}

.dropzone p {
    color: #687791;
    font-size: 12px;
    line-height: 1.7;
    margin: 8px 0 0;
}

.choose {
    display: inline-block;
    margin-top: 15px;
    background: #3157D5;
    color: white;
    padding: 11px 16px;
    border-radius: 10px;
    font-size: 12px;
    font-weight: 800;
}

.file-list {
    margin-top: 14px;
    text-align: left;
    color: #52607B;
    font-size: 12px;
    line-height: 1.7;
    overflow-wrap: anywhere;
}

.submit {
    width: 100%;
    margin-top: 7px;
    padding: 16px;
    border: 0;
    border-radius: 12px;
    background: #16A34A;
    color: white;
    font: inherit;
    font-size: 14px;
    font-weight: 800;
    cursor: pointer;
    box-shadow: 0 8px 20px rgba(22, 163, 74, .24);
    transition: .2s;
}

.submit:hover {
    background: #15803D;
    transform: translateY(-1px);
}

.submit:disabled {
    background: #8CA89A;
    cursor: wait;
    transform: none;
}

.fine {
    color: #687791;
    font-size: 11px;
    line-height: 1.7;
    text-align: center;
    margin: 14px 0 0;
}

.side-stack {
    display: grid;
    gap: 18px;
}

.side-stack > .panel:first-child {
    background: linear-gradient(145deg, #E2E9F5 0%, #D5DFEF 100%);
    border-color: #C4D0E3;
    box-shadow: 0 12px 30px rgba(37, 60, 110, .08);
}

.side-stack > .panel:first-child .sub {
    color: #4D5D78;
}

.info-row {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    margin: 19px 0;
}

.info-row:last-child {
    margin-bottom: 0;
}

.info-icon {
    width: 36px;
    height: 36px;
    flex-shrink: 0;
    border-radius: 11px;
    background: #C6D5EE;
    color: #24418A;
    display: grid;
    place-items: center;
    font-size: 12px;
    font-weight: 800;
}

.info-row strong {
    display: block;
    color: #233858;
    font-size: 13px;
}

.info-row p {
    color: #465773;
    font-size: 12px;
    line-height: 1.65;
    margin: 5px 0 0;
}

.notice {
    background: linear-gradient(145deg, #172554, #243F8F);
    color: white;
    border: 0;
}

.notice h2 {
    color: white;
}

.notice .sub {
    color: #D3DDF7;
}

.notice .info-icon {
    background: rgba(255, 255, 255, .15);
    color: white;
}

.notice ul {
    padding-left: 19px;
    margin-bottom: 0;
    color: #E6EBFF;
    font-size: 12px;
    line-height: 1.9;
}

.message {
    display: none;
    margin-top: 16px;
    padding: 14px;
    border-radius: 11px;
    font-size: 13px;
    line-height: 1.7;
    overflow-wrap: anywhere;
}

.message.show {
    display: block;
}

.message.success {
    background: #E7F8EF;
    color: #17653B;
    border: 1px solid #B7E7CB;
}

.message.error {
    background: #FFF0F0;
    color: #A61B1B;
    border: 1px solid #F2CACA;
}

.footer {
    text-align: center;
    color: #7B8498;
    font-size: 11px;
    padding: 0 16px 25px;
}

@media (max-width: 850px) {
    .content-grid {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 600px) {
    .topbar {
        padding: 14px 18px;
    }

    .brand {
        font-size: 14px;
    }

    .logo {
        width: 37px;
        height: 37px;
    }

    .top-tag {
        display: none;
    }

    .hero {
        padding-top: 38px;
        padding-bottom: 38px;
    }

    h1 {
        font-size: clamp(34px, 9vw, 46px);
        letter-spacing: -1.4px;
    }

    .stats {
        grid-template-columns: 1fr;
        gap: 10px;
    }

    .stat {
        padding: 14px;
    }

    .two {
        grid-template-columns: 1fr;
        gap: 0;
    }

    .panel {
        padding: 19px;
        border-radius: 18px;
    }

    .panel-head {
        flex-wrap: wrap;
    }

    .step-label {
        margin-top: 3px;
    }
}
</style>
</head>

<body>

<div id="app">

<header class="topbar">
    <div class="brand">
        <div class="logo">✦</div>
        <span>Student Project Portal</span>
    </div>
    <div class="top-tag">ACADEMIC SESSION 2026–27</div>
</header>

<section class="hero">
    <div class="eyebrow">
        STUDENT WORKSPACE / PROJECT SUBMISSION
    </div>

    <h1>Make your Python Microproject<br>count.</h1>

    <p class="hero-description">
        A simple, organised way to submit your Python project for
        academic review. Add your details, select the complete project
        folder, and keep everything ready for evaluation.
    </p>

    <div class="hero-pills">
        <span class="pill">✓ Easy submission</span>
        <span class="pill">⌘ Folder structure preserved</span>
        <span class="pill">↗ Repository-ready</span>
    </div>
</section>

<main>

   

    <div class="content-grid">

        <section class="panel submit-area">

            <div class="panel-head">
                <div>
                    <h2>Submit your project</h2>
                    <p class="sub">
                        Enter your information and upload your project folder.
                    </p>
                </div>
                <span class="step-label">PROJECT FORM</span>
            </div>

            <form id="submissionForm"
                  method="POST"
                  enctype="multipart/form-data">

                <div class="two">
                    <div class="field">
                        <label for="student">STUDENT NAME</label>
                        <input
                            id="student"
                            name="student"
                            type="text"
                            placeholder="Enter your Name"
                            maxlength="80"
                            autocomplete="name"
                            required
                        >
                    </div>

                    <div class="field">
                        <label for="roll">ROLL NUMBER</label>
                        <input
                            id="roll"
                            name="roll"
                            type="text"
                            placeholder="Enter your Roll No."
                            maxlength="30"
                            required
                        >
                    </div>
                </div>

                <div class="field">
                    <label for="title">PROJECT NAME</label>
                    <input
                        id="title"
                        name="title"
                        type="text"
                        placeholder="Enter your Project Name"
                        maxlength="100"
                        required
                    >
                </div>

                <div class="field">
                    <label for="folder">PROJECT FOLDER</label>

                    <label class="dropzone" id="dropzone" for="folder">
                        <div class="upload-icon">⇧</div>

                        <strong>Choose your project folder</strong>

                        <p>
                            Select your complete project folder.<br>
                            Your folder structure will be preserved.
                        </p>

                        <span class="choose">Browse folder</span>

                        <input
                            id="folder"
                            type="file"
                            webkitdirectory
                            directory
                            multiple
                            hidden
                        >

                        <div id="fileList" class="file-list"></div>
                    </label>
                </div>

                <button id="submitBtn" class="submit" type="submit">
                    Submit Project &nbsp; →
                </button>

                <div id="status" class="message" role="status"
                     aria-live="polite"></div>

                <p class="fine">
                    Please review your files before submitting.
                    Do not include passwords, API keys, or private credentials.
                </p>

            </form>
        </section>

        <aside class="side-stack">

            <section class="panel">
                <div class="panel-head">
                    <div>
                        <h2>Before you submit</h2>
                        <p class="sub">
                            A quick checklist for a smooth submission.
                        </p>
                    </div>
                </div>

                <div class="info-row">
                    <div class="info-icon">01</div>
                    <div>
                        <strong>Check your project</strong>
                        <p>
                            Include your main Python file and all required
                            supporting files.
                        </p>
                    </div>
                </div>

                <div class="info-row">
                    <div class="info-icon">02</div>
                    <div>
                        <strong>Keep it organised</strong>
                        <p>
                            Remove temporary files and folders you do not need.
                        </p>
                    </div>
                </div>

                <div class="info-row">
                    <div class="info-icon">03</div>
                    <div>
                        <strong>Review your details</strong>
                        <p>
                            Make sure your name, roll number and project
                            name are correct.
                        </p>
                    </div>
                </div>
            </section>

            <section class="panel notice">
                <div class="panel-head">
                    <div>
                        <h2>Important notice</h2>
                        <p class="sub">Please read before uploading.</p>
                    </div>
                    <div class="info-icon">!</div>
                </div>

                <ul>
                    <li>Upload only your own academic project.</li>
                    <li>Do not upload passwords or secret tokens.</li>
                    <li>Files are submitted to the configured GitHub repository.</li>
                    <li>Wait for the submission confirmation.</li>
                </ul>
            </section>

        </aside>
    </div>
</main>

<footer class="footer">
    Student Project Portal · Academic Session 2026–27
</footer>

</div>

<script>
const form = document.getElementById("submissionForm");
const folderInput = document.getElementById("folder");
const fileList = document.getElementById("fileList");
const dropzone = document.getElementById("dropzone");
const submitBtn = document.getElementById("submitBtn");
const statusBox = document.getElementById("status");

function showStatus(message, type) {
    statusBox.textContent = message;
    statusBox.className = "message show " + type;
}

folderInput.addEventListener("change", () => {
    const files = Array.from(folderInput.files);

    if (!files.length) {
        fileList.textContent = "";
        return;
    }

    const preview = files
        .slice(0, 4)
        .map(file => file.webkitRelativePath || file.name)
        .join(" · ");

    fileList.textContent =
        files.length + " file(s) selected · " + preview +
        (files.length > 4 ? " · …" : "");

    statusBox.className = "message";
});

["dragenter", "dragover"].forEach(eventName => {
    dropzone.addEventListener(eventName, event => {
        event.preventDefault();
        dropzone.classList.add("drag");
    });
});

["dragleave", "drop"].forEach(eventName => {
    dropzone.addEventListener(eventName, event => {
        event.preventDefault();
        dropzone.classList.remove("drag");
    });
});

form.addEventListener("submit", async event => {
    event.preventDefault();

    const files = Array.from(folderInput.files);

    if (!files.length) {
        showStatus("Please select your complete project folder.", "error");
        return;
    }

    if (files.length > 100) {
        showStatus(
            "Maximum 100 files are allowed in one submission.",
            "error"
        );
        return;
    }

    const data = new FormData(form);

    // Preserve each file's relative folder path.
    for (const file of files) {
        data.append("files", file, file.webkitRelativePath);
    }

    submitBtn.disabled = true;
    submitBtn.textContent = "Uploading your project...";
    showStatus(
        "Please wait while your project is uploaded. Do not close this page.",
        "success"
    );

    try {
        const response = await fetch("/", {
            method: "POST",
            body: data
        });

        const result = await response.json();

        if (!response.ok || !result.success) {
            showStatus(
                result.message || "Submission failed. Please try again.",
                "error"
            );
            return;
        }

        showStatus(result.message, "success");
        form.reset();
        fileList.textContent = "";

    } catch (error) {
        showStatus(
            "Connection problem. Please check your internet and try again.",
            "error"
        );
    } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = "Submit Project →";
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
    return jsonify({
        "success": success,
        "message": message
    }), status


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template_string(HTML)

    if not all([GITHUB_OWNER, GITHUB_REPO, GITHUB_TOKEN]):
        return json_message(
            "Server configuration is incomplete.",
            status=500
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

    prepared = []
    total_size = 0

    skipped = {
        ".git",
        ".venv",
        "venv",
        "__pycache__",
        "node_modules",
        ".idea",
        ".vscode"
    }

    # Validate files before uploading.
    for uploaded in files:
        original_path = (uploaded.filename or "").replace("\\", "/")
        path = PurePosixPath(original_path)

        if (
            not original_path
            or path.is_absolute()
            or ".." in path.parts
            or not path.parts
        ):
            return json_message("An invalid file path was detected.")

        # Skip development and version-control folders.
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

        # Preserve relative folder structure and sanitise each component.
        safe_parts = [
            re.sub(r"[^A-Za-z0-9._ -]", "_", part)
            for part in path.parts
        ]

        if any(
            part in ("", ".", "..")
            for part in safe_parts
        ):
            return json_message(
                "An invalid folder structure was found."
            )

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
                url,
                headers=headers,
                json=payload,
                timeout=30
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
