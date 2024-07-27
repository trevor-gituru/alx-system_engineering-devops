# 0x01. Shell, permissions
## Concepts learnt
### Permissions
- What do the commands `chmod`, `sudo`, `su`, `chown`, `chgrp` do
- Linux file permissions
- How to represent each of the three sets of permissions (owner, group, and other) as a single digit
- How to change permissions, owner and group of a file
- Why can’t a normal user chown a file
- How to run a command with root privileges
- How to change user ID or become superuser
### Other Man Pages
- How to create a user
- How to create a group
- How to print real and effective user and group IDs
- How to print the groups a user is in
- How to print the effective userid
## Tasks
### 0. My name is Betty
Create a script that switches the current user to the user `betty`.

- You should use exactly 8 characters for your command (+1 character for the new line)
- You can assume that the user `betty` will exist when we will run your script
```bash
julien@ubuntu:/tmp/h$ tail -1 0-iam_betty | wc -c
9
julien@ubuntu:/tmp/h$
```
### 1. Who am I
Write a script that prints the effective username of the current user.
```bash
julien@ubuntu:/tmp/h$ 
julien
julien@ubuntu:/tmp/h$ 
```
### 2. Groups
Write a script that prints all the groups the current user is part of.
```bash
julien@ubuntu:/tmp/h$ ./2-groups
julien adm cdrom sudo dip plugdev lpadmin sambashare
julien@ubuntu:/tmp/h$ 
Note: depending on the user, you will get a different output.
```
### 
### 
### 
### 
### 
### 
### 
### 
### 
### 
### 
### 
### 
### 

## Resources
- [Permissions](http://linuxcommand.org/lc3_lts0090.php)