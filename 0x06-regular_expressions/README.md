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
### 
### 
### 
### 
### 
### 
## Resources
- [Regular expressions - basics](https://www.slideshare.net/slideshow/introducing-regular-expressions/63676155#7)
- [Regular expressions - advanced](https://www.slideshare.net/slideshow/advanced-regular-expressions-80296518/80296518#3)
- [Rubular is your best friend](https://rubular.com/)
- [Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
- [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/lesson/introduction_abcs)
