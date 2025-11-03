# Redactify

**Redact private paths and strings from error logs before pasting into AI.**

A tiny, fast GTK app for Linux that helps you **scrub sensitive data** (like local file paths, usernames, API keys) from stack traces and logs — so you can **safely paste into AI tools** without leaking private info.

<img width="513" height="585" alt="Screenshot_redactify" src="https://github.com/user-attachments/assets/ca290c44-bfd3-42a9-878e-e748b037a765" />

---

## Why Redactify?

You're debugging. You copy a huge error stack.  
You want to ask an AI for help.  
But your home directory, project paths, or secrets are in there.

**Don't risk it.**  
**Don't manually edit 200 lines.**

Just:
1. Paste the log
2. Add/remove strings to strip
3. Click **Parse**
4. Copy clean output → paste safely

---

## Features

- **Simple GUI** (GTK3) – works great on Linux desktops
- **Live removal list** – edit and reuse your common redaction strings
- **One-click parsing** – replaces all matches instantly
- **Saves your removal list** to `removal_strings.txt` on each parse
- **Zero dependencies beyond GTK** (standard on most Linux distros)

---

## Run

```bash
python redactify.py
```

---

## Usage

1. **Paste your error log** into the top text box
2. **Edit the middle box** with strings to remove (one per line), e.g.:
   ```
   /home/alice/
   /projects/secret-app/
   my-secret-key
   ```
3. Click **Parse**
4. Copy the **clean output** from the bottom box
5. Paste safely into ChatGPT, Claude, etc.

Your `removal_strings.txt` is saved automatically.

---

## Example

**Before (Input):**
```python
Traceback (most recent call last):
  File "/home/bob/projects/myapp/main.py", line 42, in <module>
    load_config("/home/bob/.config/myapp/secret.json")
KeyError: 'API_KEY_12345_XYZ'
```

**Removal List:**
```
/home/bob
12345_XYZ
```

**After (Output):**
```python
Traceback (most recent call last):
  File "/projects/myapp/main.py", line 42, in <module>
    load_config("/.config/myapp/secret.json")
KeyError: 'API_KEY_'
```

Safe to share.

---

## Requirements

- Python 3
- PyGObject (`gi`)
- GTK+ 3

Install on Debian/Ubuntu:
```bash
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
```

On Fedora:
```bash
sudo dnf install python3-gobject gtk3
```

---

## License

**MIT License** – Free to use, modify, and distribute.

---

## Made For Developers, By a Developer

This tool started as a 15-minute script to stop me from leaking my `~/dev/` paths into AI chats.  
It’s small, it works, and now it’s yours.

**Star if it saves you time.**  
**Fork if you improve it.**

