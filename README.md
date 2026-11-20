# 🤖 The Ring Discord Moderation & Info Bot

A small multipurpose Discord bot built in Python using [Pycord](https://pycord.dev). Designed as a learning project to improve my Python, this bot provides essential server moderation tools and user/server information utilities.

## ✨ Features

- **Slash Commands**: Fully integrated with Discord's modern slash command UI and command groups (`/moderation` and `/info`).
- **Server Moderation**: Ban, unban, kick, timeout (mute/unmute), and delete messages with built-in Discord permission checks.
- **Server & User Insights**: Inspect user avatars, account creation dates, roles, bot latency, and detailed server statistics.

## 📜 Commands

### General

| Command | Description |
| :--- | :--- |
| `/presentation` | Displays an embed introducing the bot, its purpose, and its creator. |
| `/ban_log` | Displays the log of users banned during the current session. |

### Moderation (`/moderation`)

| Command | Options | Required Permission | Description |
| :--- | :--- | :--- | :--- |
| `/moderation ban` | `member`, `[reason]` | Ban Members | Bans a member from the server and records it in the ban log. |
| `/moderation unban` | `member_id`, `[reason]` | Ban Members | Unbans a user using their numeric Discord ID. |
| `/moderation kick` | `member`, `[reason]` | Kick Members | Kicks a member from the server. |
| `/moderation mute` | `member`, `time`, `[reason]` | Moderate Members | Times out a member for a specified duration (in minutes). |
| `/moderation unmute` | `member`, `[reason]` | Moderate Members | Removes an active timeout from a member. |
| `/moderation delete` | `number` | Manage Messages | Bulk-deletes a specified number of messages in the current channel. |

### Information (`/info`)

| Command | Options | Description |
| :--- | :--- | :--- |
| `/info avatar` | `[member]` | Displays your avatar or another member's avatar. |
| `/info pong` | *None* | Checks and displays the bot's current latency in milliseconds. |
| `/info server` | *None* | Displays server details (owner, creation date, ID, human/bot count, and channels). |
| `/info user` | `[member]` | Displays user details (ID, bot status, account creation date, and roles). |

## ⚠️ Notes

- **Temporary Ban Log**: The `banlog` dictionary stores data in memory. Restarting the bot will reset the ban log.

## 🙌 Acknowledgments

Built with ❤️ while learning Python and exploring bot development with **Hack Club**, this project is for *Crossroads* program.
