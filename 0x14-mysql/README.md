# 0x14. MySQL

![Mysql](/images/14_1.png)

## Concepts learnt
### General
- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- What operation should you regularly perform to make sure that your database backup strategy actually works

### Commands
- `mysqldump`

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck` (version 0.3.7-5~ubuntu16.04.1 via `apt-get`) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Servers

![Servers](/0x0F-load_balancer/images/image.png)

## Tasks
### 0. Install MySQL
First things first, let’s get MySQL installed on both your `web-01` and `web-02` servers.

- MySQL distribution must be 5.7.x
- Make sure that [task #3](/0x0B-ssh/3-add_ssh_key) of your [SSH project](/0x0B-ssh/) is completed for `web-01` and `web-02`. The checker will connect to your servers to check MySQL status
- Please make sure you have your `README.md` pushed to GitHub.

**Example:**
```bash
ubuntu@229-web-01:~$ mysql --version
mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
ubuntu@229-web-01:~$
```
### 1. Let us in!
In order for us to verify that your servers are properly configured, we need you to create a user and password for both MySQL databases which will allow the checker access to them.

- Create a MySQL user named `holberton_user` on both `web-01` and `web-02` with the host name set to `localhost` and the password `projectcorrection280hbtn`. This will allow us to access the replication status on both servers.
- Make sure that `holberton_user` has permission to check the primary/replica status of your databases.
- In addition to that, Make sure that [task #3](/0x0B-ssh/3-add_ssh_key) of your [SSH project](/0x0B-ssh/) is completed for `web-01` and `web-02`. **You will likely need to add the public key to `web-02` as you only added it to `web-01` for this project.** The checker will connect to your servers to check MySQL status

**Example:**
```bash
ubuntu@229-web-01:~$  cat 1-create_user.sql | mysql -u root -p
Enter password: 
Grants for holberton_user@localhost
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost'
ubuntu@229-web-01:~$
```
### 2. If only you could see what I've seen with your eyes
In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (`web-01`) to replicate from.

- Create a database named `tyrell_corp`.
- Within the `tyrell_corp` database create a table named `nexus6` and add at least one entry to it.
- Make sure that `holberton_user` has SELECT permissions on your table so that we can check that the table exists and is not empty.
```bash
ubuntu@229-web-01:~$  cat 2-create_table.sql | mysql -u root
id	name
1	Leon
2	Leon
3	Leon

ubuntu@229-web-01:~$
```
### 3. Quite an experience to live in fear, isn't it?
Before you get started with your primary-replica synchronization, you need one more thing in place. On your **primary** MySQL server (`web-01`), create a new user for the replica server.

- The name of the new user should be `replica_user`, with the host name set to `%`, and can have whatever password you’d like.
- `replica_user` must have the appropriate permissions to replicate your primary MySQL server.
- `holberton_user` will need `SELECT` privileges on the `mysql.user` table in order to check that `replica_user` was created with the correct permissions.
```bash
ubuntu@229-web-01:~$  cat 3-create_replica_user.sql | mysql -u root
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user'
+------------------+-----------------+
| user             | Repl_slave_priv |
+------------------+-----------------+
| root             | Y               |
| mysql.session    | N               |
| mysql.sys        | N               |
| debian-sys-maint | Y               |
| holberton_user   | N               |
| replica_user     | Y               |
+------------------+-----------------+
ubuntu@229-web-01:~$
```
### 
### 
## Resources
- [[How to : ] Fresh Reset and Install mysql 5.7](https://docs.google.com/document/d/1btVRofXP75Cj90_xq2x8AmzuMPOKq6D_Dt_SCDD6GrU/edit)
- [What is a database](https://www.techtarget.com/searchdatamanagement/definition/database)
- [What is a database primary/replicate cluster](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication)