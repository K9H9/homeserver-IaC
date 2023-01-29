## Homeserver IaC
This playbook sets up my homeserver with custom iso made with [ansible ubuntu-autoiso](https://github.com/K9H9/ubuntu-autoiso-ansible)

### System
Basic things are set up, installing wanted packages, modifying users and groups, and copying my neovim dotfiles. Most boring things to do after server installation.

### Services
I like to run my services as plain docker containers. 

### Storage
Playbook sets up mergrefs pool with all ssd's (currently three 1TB) that are currently attached to server, sets up samba share with users and permissions, sets 8TB hdd as snapraid parity and cron-automated parity syncs.

### Security
For security, default ssh port is changed, password authentication and root login disabled. It also uses ssh key based authentication that is set up in custom iso generation.
