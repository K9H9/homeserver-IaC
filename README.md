## Homeserver IaC
This playbook sets up my homeserver with custom iso made with [ansible ubuntu-autoiso](https://github.com/K9H9/ubuntu-autoiso-ansible)

### System
Basic things are set up, installing wanted packages, modifying users and groups, and copying my neovim dotfiles. Most boring things to do after server installation.

### Services
I like to run my services as plain docker containers. Currently used services:
  - [Authelia](https://github.com/authelia/authelia) for authentication.
  - [Nginx Proxy Manager](https://github.com/NginxProxyManager/nginx-proxy-manager) for reverse proxy.
  - [Pihole](https://pi-hole.net/) for local dns(+unbound for recursive dns resolving).
  - [Nextxloud](https://nextcloud.com/) for data, calendar, contacs and backups.
  - [Homer](https://github.com/bastienwirtz/homer) for nice homepage for all applications.
  - [Uptime Kuma](https://github.com/louislam/uptime-kuma) for uptime monitoring.
  - [Octoprint](https://octoprint.org/) for managing 3d-printer.
  - [Vaultwarden](https://github.com/dani-garcia/vaultwarden) for password manager.
  - [Baserow](https://github.com/bram2w/baserow) for data managing/sheets replacement.

### Storage
Playbook sets up mergrefs pool with all ssd's (currently three 1TB) that are currently attached to server, sets up samba share with users and permissions, sets 8TB hdd as snapraid parity and cron-automated parity syncs.

### Security
For security, default ssh port is changed, password authentication and root login disabled. It also uses ssh key based authentication that is set up in custom iso generation. Every service is set up behind reverse proxy and also every application has 2fa for enhanced security.
