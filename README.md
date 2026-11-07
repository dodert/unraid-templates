# dodert's Unraid templates

Templates for Unraid's Community Applications.

| App | Description |
|---|---|
| [Accounts Balance Tracker](https://github.com/dodert/accounts-balance-tracker) | Self-hosted tracker of your accounts balances over time: bank, savings, investment, pension, crypto, cash and loans. |
| [Game Library Manager](https://github.com/dodert/game-library-manager) | Self-hosted video game collection manager (physical and digital, every console and PC) with cover art and metadata from IGDB, SteamGridDB, Steam and ScreenScraper. |

## Install

Unraid removed the "Template repositories" setting in 6.10, so each template is installed with one command
in the Unraid terminal (run it again to update the template). Then pick the app in **Docker → Add Container**.

**Accounts Balance Tracker**

```bash
mkdir -p /boot/config/plugins/dockerMan/templates-user && curl -fsSL https://raw.githubusercontent.com/dodert/unraid-templates/main/accounts-balance-tracker.xml -o /boot/config/plugins/dockerMan/templates-user/my-accounts-balance-tracker.xml
```

**Game Library Manager**

```bash
mkdir -p /boot/config/plugins/dockerMan/templates-user && curl -fsSL https://raw.githubusercontent.com/dodert/unraid-templates/main/game-library-manager.xml -o /boot/config/plugins/dockerMan/templates-user/my-game-library-manager.xml
```

To list them in **Apps → Private** (Community Applications) instead, download them to
`/boot/config/plugins/community.applications/private/dodert/`.

Each template and its icon are copied automatically from the app's repository (`unraid/` folder); change them there.
This README is rebuilt from the templates by the *Update README* workflow.
