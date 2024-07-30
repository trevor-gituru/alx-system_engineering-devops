# 0x04. Loops, conditions and parsing
## Concepts learnt
### General
- How to create SSH keys
- What is the advantage of using `#!/usr/bin/env bash` over `#!/bin/bash`
- How to use `while`, `until` and `for` loops
- How to use `if`, `else`, `elif` and `case` condition statements
- How to use the `cut` command
- What are files and other comparison operators, and how to use them
### More info
[Shellcheck](https://github.com/koalaman/shellcheck) is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. `Shellcheck` is your friend! `All your Bash scripts must pass `Shellcheck` without any error or you will not get any points on the task`.

`Shellcheck` is available on the school’s computers. If you want to use it on your own computer, here is how to [install it](https://github.com/koalaman/shellcheck#installing).

**Examples**:

Not passing `Shellcheck`:

![Fail shellchekc](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/Vxotqyj.png)

Passing `Shellcheck`:

![Pass shellcheck](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/ubHWxDU.png)

For every feedback, Shellcheck will provide a code that you can use to get more information about the issue, for example for code SC2034, you can browse https://github.com/koalaman/shellcheck/wiki/SC2034.
## Tasks
### 0. Create a SSH RSA key pair
Read for this task:

- [Linux and Mac OS users](https://askubuntu.com/questions/61557/how-do-i-set-up-ssh-authentication-keys)
- [Windows users](https://docs.rackspace.com/docs/generating-rsa-keys-with-ssh-puttygen)
man: `ssh-keygen`

You will soon have to manage your own **servers** concept page hosted on remote [data centers](). We need to set them up with your RSA public key so that you can access them via SSH.

Create a RSA key pair.

**Requirements:**

- Share your public key in your answer file `0-RSA_public_key.pub`
- Fill the `SSH public key` field of your intranet profile with the public key you just generated
- **Keep the private key to yourself in a secure location**, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
- If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase
SSH and RSA keys will be covered in depth in a later project.
### 1. For Best School loop
Write a Bash script that displays `Best School` 10 times.

**Requirement:**

- You must use the `for` loop (`while` and `until` are forbidden)
```bash
sylvain@ubuntu$ head -n 2 1-for_best_school 
#!/usr/bin/env bash
# This script is displaying "Best School" 10 times
sylvain@ubuntu$ ./1-for_best_school 
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
```
**Note that:**

- The first line of my Bash script starts with `#!/usr/bin/env bash`
- The second line of my Bash scripts is a comment explaining what it is doing
### 2. While Best School loop
Write a Bash script that displays `Best School` 10 times.

**Requirements:**

- You must use the `while` loop (`for` and `until` are forbidden)
```bash
sylvain@ubuntu$ ./2-while_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
```
### 3. Until Best School loop
Write a Bash script that displays `Best School` 10 times.

**Requirements:**

- You must use the `until` loop (`for` and `while` are forbidden)
```bash
sylvain@ubuntu$ ./3-until_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
```
### 4. If 9, say Hi!
Write a Bash script that displays `Best School` 10 times, but for the 9th iteration, displays `Best School` and then `Hi` on a new line.

**Requirements:**

- You must use the `while` loop (`for` and `until` are forbidden)
- You must use the `if` statement
```bash
sylvain@ubuntu$ ./4-if_9_say_hi
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Hi
Best School
sylvain@ubuntu$ 
```
### 5. 4 bad luck, 8 is your chance
Write a Bash script that loops from `1` to `10` and:

- displays `bad luck` for the 4th loop iteration
- displays `good luck` for the 8th loop iteration
- displays `Best School` for the other iterations
**Requirements:**

- You must use the `while` loop (`for` and `until` are forbidden)
- You must use the `if`, `elif` and `else` statements
```bash
sylvain@ubuntu$ ./5-4_bad_luck_8_is_your_chance
Best School
Best School
Best School
bad luck
Best School
Best School
Best School
good luck
Best School
Best School
sylvain@ubuntu$ 
```
**For the most curious:**

- [8 in the Chinese culture](https://www.chcp.org/Chinese-Numerology)
- [4 in the Chinese culture](https://en.wikipedia.org/wiki/Chinese_numerology#Four)
### 
### 
### 
### 
### 
## Resources
- [Loops sample](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html)
- [Variable assignment and arithmetic](https://tldp.org/LDP/abs/html/ops.html)
- [Comparison operators](https://tldp.org/LDP/abs/html/comparison-ops.html)
- [File test operators](https://tldp.org/LDP/abs/html/fto.html)
- [Make your scripts portable](https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html)