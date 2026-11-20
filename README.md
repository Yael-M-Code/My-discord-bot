# My-discord-bot
## Tutorial
### Make the bot join your server
Link to the sample section: [https://discord.com/oauth2/authorize?client_id=1573044252684849242&permissions=8&integration_type=0&scope=bot+applications.commands](#make-the-bot-join-your-server).

## Documentation The Ring
> [!WARNING]
> First, the bot must stay at the top of most roles in order to doing action such as ban or kick on it.

list of all commands: <br>
```/presentation```; displays a small presentation of the bot. <br>
```/moderation ban```; ban a member of the server. <br>
```/moderation unban```; unban someone that's been banned. <br>
```/moderation mute```; mute a member for x minutes. <br>
```/moderation unmute```; unmute a member that's been muted. <br>
```/moderation kick```; kick a member of the server, out of the server. <br>
```/moderation delete```; delete x number of the most recent message in the actual channel, don't work for 14 days more message due to discord limitations. <br>
```/ban_log```; shows log of all the person banned (since the last start of the bot). <br>
```/info avatar```; shows the avatar of the user. <br>
```/info user```; displays infos about the user. <br>
```/info server```; displays infos about the server. <br>
```/info pong```; shows the ping. <br>

list of the events:
>When the bot log, it shows the ping in a dedicated channel

>When someone says hi/how are you in the most common variant, the bot will detect and respond "Hi (ping the player)" or "I'm doing great, thanks for asking!, what about you?"

>If someone says a bad word like ass or cock, the bot will delete the message and DM the user.
