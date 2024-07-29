# 0x03. Shell, init files, variables and expansions
## Concepts learnt
### Commands
- `printenv`
- `set`
- `unset`
- `export`
- `alias`
- `unalias`
- `.`
- `source`
- `printf`
### Shell Initialization Files
- What are the `/etc/profile` file and the ~/etc/profile.d~ directory
- What is the `~/.bashrc` file
###  Variables
- What is the difference between a local and a global variable
- What is a reserved variable
- How to create, update and delete shell variables
- What are the roles of the following reserved variables: `HOME`, `PATH`, `PS1`
- What are special parameters
- What is the special parameter `$?`?
###  Expansions
- What is expansion and how to use them
- What is the difference between single and double quotes and how to use them properly
- How to do command substitution with `$()` and backticks
###  Shell Arithmetic
- How to perform arithmetic operations with the shell
### The `alias` Command
- How to create an alias
- How to list aliases
- How to temporarily disable an alias
###  Other help pages
- How to execute commands from a file in the current shell
## Tasks
### 0. <o>
Create a script that creates an alias.

- Name: `ls`
- Value: `rm *`
```bash
julien@ubuntu:/tmp/0x03$ ls
0-alias  file1  file2
julien@ubuntu:/tmp/0x03$ source ./0-alias 
julien@ubuntu:/tmp/0x03$ ls
julien@ubuntu:/tmp/0x03$ \ls
julien@ubuntu:/tmp/0x03$ 
```
### 1. Hello you
Create a script that prints `hello user`, where `user` is the current Linux user.
```bash
julien@ubuntu:/tmp/0x03$ id
uid=1000(julien) gid=1000(julien) groups=1000(julien),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),113(lpadmin),128(sambashare)
julien@ubuntu:/tmp/0x03$ ./1-hello_you 
hello julien
julien@ubuntu:/tmp/0x03$ 
``` 
### 2. The path to success is to take massive, determined action
Add `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program.
```bash
julien@ubuntu:/tmp/0x03$ echo $PATH
/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
julien@ubuntu:/tmp/0x03$ source ./2-path 
julien@ubuntu:/tmp/0x03$ echo $PATH
/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/action
julien@ubuntu:/tmp/0x03$ 
```
### 3. If the path be beautiful, let us not ask where it leads
Create a script that counts the number of directories in the `PATH`.
```bash
julien@ubuntu:/tmp/0x03$ echo $PATH
/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
julien@ubuntu:/tmp/0x03$ . ./3-paths 
11
julien@ubuntu:/tmp/0x03$ PATH=/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:::::/hello
julien@ubuntu:/tmp/0x03$ . ./3-paths 
12
julien@ubuntu:/tmp/0x03$ 
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
- [Expansions](http://linuxcommand.org/lc3_lts0080.php)
- [Shell Arithmetic](https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html)
- [Variables](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html)
- [Shell initialization files](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html)
- [The alias Command](https://www.linfo.org/alias.html)
- [Technical Writing](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2021/6/9112669886fd446a2aa3113c31319d1f468dc160.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240729%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240729T063640Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3f2fd114f379fd9961f4858d72eef8c3a46e1ebed0e232f343c9bd91d353538b)
