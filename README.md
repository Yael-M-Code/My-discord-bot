# The Ring Discord bot

This is a small Discord bot using Python and Pycord library. The purpose of this project was to improve my python, it provides essentials moderation / informations commands

Here is the link to [use it](https://discord.com/oauth2/authorize?client_id=1573044252684849242&permissions=8&integration_type=0&scope=bot+applications.commands)

## Features

- Slash Commands: Every commands use `/` prefix, so you can enjoy the discord UI
- Moderation: (un)Mute, (un)Ban, kick nad even more...
- Server / User infos: Display avatar, roles, bot's ping, server statistics...

## Commands

### `/moderation`
-`/moderation ban`: Ban someone and record this action in ban_log (check warning)
-`/moderation unban`: Unban someone, you need his ID, for that check /ban_log
-`/moderation mute`: Mute someone for x minutes 
-`/moderation unmute`: Unmute someone
-`/moderation kick`: Remove a user from your server
-`/moderation delete`: Delete the number of messages you choose (message for more than 2 weeks wouldn't delete)

### `/info`
-`/info avatar`: Display the avatar of the person you choose (by default you)
-`/info user`: Display some infos (likeID, creation date..) of the person you choose (by default you)
-`/info pong`: Display bot's latency in ms
-`/info server`: Display some infos about the server you're in (owner, creation date, ID....)


### Other
-`presentation`: An embed about some cool infos of the bot
-`ban_log`: Shows the log of all users banned.

> [!WARNING]
> The command using banlog is been reset each time the bot crash.

> [!NOTE]
> The bot isn't host because I wait my HackClub verification in order to acces HackClub Nest

If you want to try it yourself: install library from `requirements.txt`, after that run your main.py with python3 main.py (the bot should work like that locally) 

## Extra
Thank you to use my bot at least one time hehe, it was really fun to build (and faster than I thought). My Python level is really different since the beginning of this project. Also it helps me learn basic for every project (remind me git, readme, .env file...)