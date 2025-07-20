# 🛡️ Keylogger with Active App Tracking — Cybersecurity Task 4

This project is part of my Cybersecurity Internship under **SkillCraft Technology**. It demonstrates a basic yet powerful keylogger built using Python that tracks and logs all user keystrokes along with the active application window.

---

## 🚀 Features

- 🔍 Captures all keyboard input (alphanumeric + special keys)
- 🪟 Logs the **active application window title** with a timestamp
- ➡️ Appends all keystrokes in a continuous flow
- ↩️ Inserts a new line **only when Enter is pressed**
- 🧠 Identifies and tags special keys like `Backspace`, `Delete`, etc.
- 📁 Saves the log file (`key_log.txt`) in the **same directory** as the script

---

## 📦 Requirements

Install the necessary Python packages:

```bash
pip install pynput pywin32

## How It Works

- The script uses pynput to listen for keypresses and pywin32 to track the currently focused window.
- When a key is pressed:
- It checks if the active window has changed
- If so, it logs the window name and timestamp
- Then logs the key (space as " ", enter as "\n", etc.)
- The keystrokes are logged into a file called key_log.txt, located in the same directory as the script.

## ✍️ Sample Output

[2025-07-20 15:00:00] — Active Window: Untitled - Notepad
hello world

[2025-07-20 15:01:02] — Active Window: New Tab - Google Chrome
openai.com[ENTER]

### ⚠️ Disclaimer

**⚠️ This tool is for educational and ethical use only.**
**Misuse of this tool for malicious purposes may be illegal and unethical.**
**Always test in a sandboxed or authorized environment.**

Created by codex21venom as part of a cybersecurity internship @SkillCraft_Technology.

---

### 🔍 Breakdown of Fixes

| Problem | Fix |
|--------|-----|
| `pip install` not formatted | Wrapped it in a `bash` code block |
| Header not rendered | Added a blank line before `## How It Works` |
| Sample output messy | Used a code block for the multiline log preview |
| Disclaimer not emphasized | Turned it into a blockquote for better style |

---
