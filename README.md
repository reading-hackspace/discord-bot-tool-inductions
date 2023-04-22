# Discord Bot Inductions
A bot to support induction requests for rLab

## Developing locally

- [ ] Follow step 1 of the [Discord developer docs - getting started](https://discord.com/developers/docs/getting-started)
to create and install an app with permissions
- [ ] In the [Discord application](https://discord.com/developers/applications) go to `Bot` and turn on the different 
`Privileged Gateway Intents`. These are needed for the Python library this bot uses to integrate with Discord. 
- [ ] Install [ngrok](https://ngrok.com/download) so that you can create a local tunnel 
- [ ] Run `ngrok http 8080` in the console
- [ ] On your [Discord application](https://discord.com/developers/applications) set the `General information -> 
interactions endpoint url` to `[ngrok forwarding url]/api/commands`

## Random spare links

- https://discordpy.readthedocs.io/en/stable/discord.html
