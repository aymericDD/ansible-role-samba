Ansible Role: Samba
=========

[![Build Status](https://travis-ci.com/aymericDD/ansible-role-samba.svg?branch=master)](https://travis-ci.com/aymericDD/ansible-role-samba)

Installs Samba client and server for Debian Stretch.

Requirements
------------

Samba requires ports 137, 138, 139, 445 to be open to function properly.

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`):

``` yaml
samba_global_workgroup: WORKGROUP
samba_home_browseable: no
samba_home_read_only: yes
samba_home_create_mask: 0700
samba_home_directory_mask: 0700
samba_home_valid_users: '%S'
samba_shares: [] # functionality to manage share directory
```

You can add unlimited shared directories. 
To add a shared directory, you can add variable like:
 
``` yaml
samba_shares:
  - name: example
    options: |
      create mask = 0777
      directory mask = 0777
```

Something along those lines (at a minimum), and it would output in `/etc/samba/smb.conf`:

``` yaml
[example]
   create mask = 0777
   directory mask = 0777
```

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: aymericdd.samba }

License
-------

BSD

Author Information
------------------

This role is based on samba role written by Jeff Geerling, author of Ansible for DevOps.

This role was created in 2019 by [AymericDD](https://github.com/aymericDD).