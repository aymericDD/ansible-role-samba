import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_samba_is_installed(host):
    smbd = host.package("samba")
    assert smbd.is_installed


def test_samba_common_is_installed(host):
    smbd = host.package("samba-common")
    assert smbd.is_installed


def test_smbd_running_and_enabled(host):
    smbd = host.service("smbd")
    assert smbd.is_running
    assert smbd.is_enabled
