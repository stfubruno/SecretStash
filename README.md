# 🤫 SecretStash: A Simple CLI Secret Manager

![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A lightweight, command-line tool to securely store and manage your secrets, API keys, or any sensitive strings locally. Never hardcode your secrets again!

## 📜 Description

**SecretStash** provides a simple and intuitive command-line interface to manage a `secret.json` file. You can easily add new secrets, view all your stored secrets, and securely delete the entire stash when needed. It's built with standard Python libraries, requiring no external dependencies.

## ✨ Features

* **Read Secrets:** View a list of all your stored secrets in a clean format.
* **Write Secrets:** Easily add new secrets with a descriptive callback name and a value.
* **Persistent Storage:** Secrets are saved locally in a `secret.json` file, making them persistent across sessions.
* **Secure Deletion:** A special command to completely wipe the `secret.json` file.
* **Zero Dependencies:** Runs on a standard Python installation. No `pip install` needed!
* **User-Friendly CLI:** An interactive menu guides you through the available options.

## 🚀 Getting Started

Getting started with SecretStash is as simple as running the script.

### Prerequisites

* Python 3.6 or higher.

### Installation & Usage

1.  **Clone the repository or download the script:**
    ```bash
    git clone [https://github.com/your-username/SecretStash.git](https://github.com/your-username/SecretStash.git)
    cd SecretStash
    ```
    *(Or simply download `SecretStash.py`)*

2.  **Run the script from your terminal:**
    ```bash
    python SecretStash.py
    ```

3.  **Follow the on-screen menu:**
    * Choose `1` to read all secrets.
    * Choose `2` to add a new secret.
    * Choose `3` to exit the program.
    * Use `**` to delete the `secret.json` file.

## 📁 File Structure

The script will automatically create and manage a `secret.json` file in the same directory. This file stores your secrets in the following JSON format:

```json
[
    {
        "id": 1,
        "callback": "GitHub API Key",
        "string": "ghp_123abc456def789ghi"
    },
    {
        "id": 2,
        "callback": "Database Password",
        "string": "S3cureP@ssw0rd!"
    }
]
```

> **⚠️ Warning:** The `**` command will permanently delete this file and all its contents. This action cannot be undone.

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to fork the repository and submit a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📝 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Made with ❤️ and Python.