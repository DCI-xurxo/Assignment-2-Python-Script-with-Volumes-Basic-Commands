# Python Logger with Docker

# How it works
- The Python script (`logger.py`) appends a log entry to a file called `log.txt` every time the container runs.
- Each log entry contains:
  - The current date and time
  - A random motivational quote (chosen from a predefined list)
  - A line saying **"Container execution completed"**
  - A separator line for readability
- The file `log.txt` is written inside `/app/logs` in the container.  
  With a volume (or bind mount), this folder is mapped to the host, so logs are **preserved on the host** even after the container stops or is removed.

## Files
- `logger.py` → Python script that generates the log entry.
- `Dockerfile` → Instructions to build the image with Python installed and the script copied.
- `logs/` → Host directory where `log.txt` is stored (created automatically when you run with a volume).
- `README.md` → This file.

## Build the image
```bash
docker build -t python-logger:1.0 .