# HARMONY-NOTIFY

This project helps the A10 Harmony Controller send notifications to Telegram channel/group.

## Requirements

This project can run on Windows, Linux environment that installed [ Python3](https://www.python.org/downloads/).

### Packages needed:
- [Aiohttp](https://docs.aiohttp.org/en/stable/) - This package is used for building API Server

## Installation

This project requires [Python3](https://www.python.org/downloads/).

Instal needed packages from requirements.txt file

```sh
cd Harmony-Notify
pip install -r requirements.txt
```

## Run
Create ***config.py*** file with these information below:
```
TELEGRAM_BOT_TOKEN="your_bot_token"
TELEGRAM_CHAT_ID="your_channel/group_chat_id"
```

Then you can run with
```sh
python3 app.py
```
The default port is *8080*. You can change the port from ***config.py*** file. Add ```PORT=8000``` in ***config.py*** file to change the port.

## Run as daemon (Run on boot)

To run on boot, create ***harmony-notify.service*** in */etc/systemd/system/*

Replace **your_harmony-notify_directory** and **your_harmony-notify_app** as in your server.

For example:
    **your_harmony-notify_directory** -> /root/Harmony-Notify
    **your_harmony-notify_app** -> /root/Harmony-Notify/app.py
```sh
[Unit]
Description=Harmony Notify
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=your_harmony-notify
ExecStart=/usr/bin/python3 your_harmony-notify_app
Restart=always

[Install]
WantedBy=multi-user.target
```

Then run
```sh
sudo systemctl daemon-reload
sudo systemctl start harmony-notify
```