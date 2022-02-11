# adhoc commands

https://docs.ansible.com/ansible/latest/user_guide/intro_adhoc.html

```bash
ansible luna-01 -m ansible.builtin.shell -a 'echo $TERM' -i ./inventory/hosts --ask-pass --user someuser
```
