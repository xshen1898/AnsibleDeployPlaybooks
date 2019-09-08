#!/usr/bin/env python3

import os, sys, argparse, subprocess, getpass


def get_args():
    parser = argparse.ArgumentParser(prog='provision.py', description='Deploy playbooks.')
    parser.add_argument(
        '--auth',
        '-a',
        action='store_true',
        required=False,
        help='Ask for connection user and password'
    )
    parser.add_argument(
        '--sudo',
        '-s',
        action='store_true',
        required=False,
        help='Run operations with sudo'
    )
    args = parser.parse_args()
    return args


def ask_user_pass():
    user = input('Please enter remote user: ')
    password = getpass.getpass(prompt='Please enter password: ')
    return user, password


def main():
    args = get_args()
    extra_vars = {}

    extra_vars['ansible_ssh_common_args'] = '-o StrictHostKeyChecking=no'
    if args.auth or args.sudo:
        user, password = ask_user_pass()
        if args.auth:
            extra_vars['ansible_ssh_user'] = user
            extra_vars['ansible_ssh_pass'] = password
        if args.sudo:
            extra_vars['ansible_become'] = 'yes'
            extra_vars['ansible_become_pass'] = password

    cmd = 'ansible-playbook -i hosts.py site.yml -e "{}"'.format(extra_vars)
    subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    main()
