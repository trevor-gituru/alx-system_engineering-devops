# 0x00. Shell, basics
## Concepts learnt
### What is the Shell
- What is the shell
- What is the difference between a terminal and a shell
- What is the shell prompt
- How to use the history (the basics)
### Navigation
- What do the commands or built-ins `cd`, `pwd`, `ls` do
- How to navigate the filesystem
- What are the `.` and `..` directories
- What is the working directory, how to print it and how to change it
- What is the root directory
- What is the home directory, and how to go there
- What is the difference between the root directory and the home directory of the user root
- What are the characteristics of hidden files and how to list them
- What does the command `cd -` do
### Looking Around
- What do the commands `ls`, `less`, `file` do
- How do you use options and arguments with commands
- Understand the ls long format and how to display it
- [A Guided Tour](http://linuxcommand.org/lc3_lts0040.php)
- What does the `ln` command do
- What do you find in the most common/important directories
- What is a symbolic link
- What is a hard link
- What is the difference between a hard link and a symbolic link
### Manipulating Files
- What do the commands `cp`, `mv`, `rm`, `mkdir` do
- What are wildcards and how do they work
- How to use wildcards
### Working with Commands
- What do `type`, `which`, `help`, `man` commands do
- What are the different kinds of commands
- What is an alias
- When do you use the command `help` instead of `man`
### Reading Man Pages
- How to read a `man` page
- What are `man` page sections
- What are the section numbers for User commands, System calls and Library functions
### Keyboard Shortcuts for Bash
- Common shortcuts for Bash
### LTS
- What does `LTS` mean?
## More Info
**Example of line count and first line**
```bash
julien@ubuntu:/tmp$ wc -l 12-file_type 
2 12-file_type
julien@ubuntu:/tmp$ head -n 1 12-file_type 
#!/bin/bash
julien@ubuntu:/tmp$ 
```
In order to test your scripts, you will need to use this command: `chmod u+x file`. We will see later what does `chmod` mean and do, but you can have a look at man `chmod` if you are curious.

**Example**
```bash
julien@ubuntu:/tmp$ ls
12-file_type
lll
julien@ubuntu:/tmp$ ls -la lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ cat lll
#!/bin/bash
ls
julien@ubuntu:/tmp$ ls -l lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ chmod u+x lll # you do not have to understand this yet
julien@ubuntu:/tmp$ ls -l lll
-rwxrw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ ./lll
12-file_type
lll
julien@ubuntu:/tmp$ 
```
## Tasks
### 0. Where am I?
Write a script that prints the absolute path name of the current working directory.

**Example:**
```bash
$ ./0-current_working_directory
/root/alx-system_engineering-devops/0x00-shell_basics
$
```
### 1. What’s in there?
Display the contents list of your current directory.

**Example:**
```bash
$ ./1-listit
Applications    Documents   Dropbox Movies Pictures
Desktop Downloads   Library Music Public
$
```
### 2. There is no place like home
Write a script that changes the working directory to the user’s home directory.

- You are not allowed to use any shell variables
```bash
julien@ubuntu:/tmp$ pwd
/tmp
julien@ubuntu:/tmp$ echo $HOME
/home/julien
julien@ubuntu:/tmp$ source ./2-bring_me_home
julien@ubuntu:~$ pwd
/home/julien
julien@ubuntu:~$ 
```
### 3. The long format
Display current directory contents in a long format

**Example:**
```bash
$ ./3-listfiles
total 32
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
$
```
### 4. Hidden files
Display current directory contents, including hidden files (starting with `.`). Use the long format.

**Example:**
```bash
$ ./4-listmorefiles
total 32
drwxr-xr-x@ 6 sylvain staff 204 Jan 25 00:29 .
drwxr-xr-x@ 43 sylvain staff 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:41 4-listmorefiles
$
```
### 5. I love numbers
Display current directory contents.

- Long format
- with user and group IDs displayed numerically
- And hidden files (starting with .)
**Example:**
```bash
$ ./5-listfilesdigitonly
total 32
drwxr-xr-x@ 6 501 20 204 Jan 25 00:29 .
drwxr-xr-x@ 43 501 20 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:23 1-listfiles
-rwxr-xr-x@ 1 501 20 19 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 501 20 20 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:41 4-listmorefiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:43 5-listfilesdigitonly
$
```
### 6. Welcome
Create a script that creates a directory named `my_first_directory` in the `/tmp/` directory.

**Example:**
```bash
$ ./6-firstdirectory
$ file /tmp/my_first_directory/
/tmp/my_first_directory/: directory
$
```
### 7. Betty in my first directory
Move the file betty from `/tmp/` to `/tmp/my_first_directory`.

**Example**:
```bash
$ ./7-movethatfile
$ ls /tmp/my_first_directory/
betty
$
```
### 8. Bye bye Betty
Delete the file `betty`.

The file `betty` is in `/tmp/my_first_directory`
**Example:**
```bash
$ ./8-firstdelete
$ ls /tmp/my_first_directory/
$
```
### 9. Bye bye My first directory
Delete the directory `my_first_directory` that is in the `/tmp` directory.

**Example:**
```bash
$ ./9-firstdirdeletion
$ file /tmp/my_first_directory
/tmp/my_first_directory: cannot open `/tmp/my_first_directory' (No such file or directory)
$
```
### 10. Back to the future
Write a script that changes the working directory to the previous one.
```bash
julien@ubuntu:/tmp$ pwd
/tmp
julien@ubuntu:/tmp$ cd /var
julien@ubuntu:/var$ pwd
/var
julien@ubuntu:/var$ source ./10-back
/tmp
julien@ubuntu:/tmp$ pwd
/tmp
```
### 11. Lists
Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
### 
### 
## Resources
- [What Is “The Shell”?](http://linuxcommand.org/lc3_lts0010.php)
- [Navigation](http://linuxcommand.org/lc3_lts0020.php)
- [Looking Around](https://linuxcommand.org/lc3_lts0030.php)
- [A Guided Tour](http://linuxcommand.org/lc3_lts0040.php)
- [Manipulating Files](http://linuxcommand.org/lc3_lts0050.php)
- [Working With Commands](http://linuxcommand.org/lc3_lts0060.php)
- [Reading Man pages](http://linuxcommand.org/lc3_man_pages/man1.html)
- [Keyboard shortcuts for Bash](https://www.howtogeek.com/181/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/)
- [LTS](https://wiki.ubuntu.com/LTS)
- [Shebang](https://en.wikipedia.org/wiki/Shebang_%28Unix%29)

