# 0x02. Shell, I/O Redirections and filters
## Concepts learnt
### Commands
- `echo`
- `cat`
- `head`
- `tail`
- `find`
- `wc`
- `sort`
- `uniq`
- `grep`
- `tr`
- `rev`
- `cut`
- `passwd (5)` (i.e. `man 5 passwd`)
### Shell, I/O Redirection
- What do the commands `head`, `tail`, `find`, `wc`, `sort`, `uniq`, `grep`, `tr` do
- How to redirect standard output to a file
- How to get standard input from a file instead of the keyboard
- How to send the output from one program to the input of another program
- How to combine commands and filters with redirections
### Special Characters
- What are special characters
- Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them
### Other Man Pages
- How to display a line of text
- How to concatenate files and print on the standard output
- How to reverse a string
- How to remove sections from each line of files
- What is the `/etc/passwd` file and what is its format
- What is the `/etc/shadow` file and what is its format

## Tasks
### 0. Hello World
Write a script that prints “Hello, World”, followed by a new line to the standard output.
```bash
julien@ubuntu:/tmp/h$ ./0-hello_world 
Hello, World
julien@ubuntu:/tmp/h$ ./0-hello_world | cat -e
Hello, World$
julien@ubuntu:/tmp/h$ 
```
### 1. Confused smiley
Write a script that displays a confused smiley `"(Ôo)'`.
```bash
julien@ubuntu:/tmp/h$ ./1-confused_smiley 
"(Ôo)'
julien@ubuntu:/tmp/h$ 
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
### 
### 
### 
### 
### 
### 

## Resources
- [Shell, I/O Redirection](http://linuxcommand.org/lc3_lts0070.php)
- [Special Characters](https://mywiki.wooledge.org/BashGuide/SpecialCharacters)
