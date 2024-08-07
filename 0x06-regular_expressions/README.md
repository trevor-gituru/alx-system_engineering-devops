# 0x06. Regular expression
## Background Context
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the `//`:
```bash
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```
## Tasks
### 0. Simply matching School
![regex](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/ec65557f0da1fbfbff6659413885e4d4822f5b1d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240731%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240731T110142Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cf8f70d36b3ea7164893ef6cec0bb1baf84fe9ee9c9dffd3b5b6897c4264c2cd)

**Requirements:**

- The regular expression must match `School`
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
Example:
```bash
sylvain@ubuntu$ ./0-simply_match_school.rb School | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "Best School" | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "School Best School" | cat -e
SchoolSchool$
sylvain@ubuntu$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
$
```
### 1. Repetition Token #0

![regex](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/e7db3c377d46453588fc84f3a975661d142fee91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240731%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240731T110142Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c88dbf0fe23b4e785d7c98d04a0c6678f81127c88b5a782eadc4ce05c88a89d8)

**Requirements:**

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
```bash
razaoul@ubuntu$ ./1-repetition_token_0.rb hbttn
hbttn
```

### 2. Repetition Token #1

![regex text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/c59ff11db195d5cf17d1790a5141ae2f234786d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240731%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240731T110142Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=be499b4d26684e60ec49568884f6bd0828eb6cbbb9e547b2fe5e045af76c5643)

**Requirements:**

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
```bash
razaoul@ubuntu$ ./2-repetition_token_1.rb hbtn htn
hbtn htn
```
### 3. Repetition Token #2

![regex text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/3b6bf4aeca6a0c2de584e7f5d68d11eef57ce205.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240731%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240731T110142Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f36ab45544df757621eb524b68eec460ff174efa30fb2f46ce25a9682de1b8ef)

**Requirements:**

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
```bash
razaoul@ubuntu$ ./3-repetition_token_2.rb hbn hbtn
hbtn
```

### 4. Repetition Token #3

![regex text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/f8dbcb9cf5ae569a8645027dc46e81cb372ce28e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240731%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240731T110142Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5a99742eaffe8b3be0e156b8323254ba1ac353782fa3dd2c7e58aa7c9b48240c)

**Requirements:**

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
- Your regex should not contain square brackets
```bash
razaoul@ubuntu$ ./4-repetition_token_3.rb hbtn hbon
hbtn
```
### 5. Not quite HBTN yet
**Requirements:**

- The regular expression must be exactly matching a string that starts with `h` ends with `n` and can have any single character in between
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
**Example:**
```bash
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
h8n$
sylvain@ubuntu$
$
```
### 6. Call me maybe
This task is brought to you by a professional advisor [Neha Jain](https://x.com/_nehajain), Senior Software Engineer at LinkedIn.

**Requirement:**

- The regular expression must match a 10 digit phone number
**Example:**
```bash
sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
$
sylvain@ubuntu$
```
### 7. OMG WHY ARE YOU SHOUTING?

![regex](https://intranet.alxswe.com/images/contents/sysadmin/projects/78/shouting.jpg)

**Requirement:**

- The regular expression must be only matching: capital letters
**Example:**
```bash
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
sylvain@ubuntu$
```
## Resources
- [Regular expressions - basics](https://www.slideshare.net/slideshow/introducing-regular-expressions/63676155#7)
- [Regular expressions - advanced](https://www.slideshare.net/slideshow/advanced-regular-expressions-80296518/80296518#3)
- [Rubular is your best friend](https://rubular.com/)
- [Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
- [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/lesson/introduction_abcs)
