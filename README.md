# PC Troubleshooting Assistant

A rule-based command-line assistant that asks about common computer problems
and recommends troubleshooting steps based on the user's answers.

## Rules

| # | Problem | Recommendation |
|---|---------|----------------|
| 1 | Computer does not turn on | Check power cable, outlet, and power button |
| 2 | No internet connection | Check network connection, restart router/modem, reconnect to Wi-Fi/Ethernet |
| 3 | Slow performance | Close unnecessary programs, check storage, restart the computer |
| 4 | Application not working | Restart the app, check for updates, restart the computer |
| 5 | Unusual pop-ups / security warnings | Run an antivirus scan, avoid unknown links and downloads |
| 6 | None of the above | Restart the computer and check for OS/driver updates |

## Running

```bash
python pc_troubleshooting_assistant.py
```

Requires Python 3.8+. No external packages needed (see `requirements.txt`).
