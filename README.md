Ansible Role: Samba
=========

[![Build Status](https://travis-ci.com/aymericDD/ansible-role-samba.svg?branch=master)](https://travis-ci.com/aymericDD/ansible-role-samba)

Installs Samba client and server for Debian Stretch.

Requirements
------------

Samba requires ports 137, 138, 139, 445 to be open to function properly.

Role Variables
--------------

None.

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

This role was created in 2019 by [AymericDD](https://github.com/aymericDD).