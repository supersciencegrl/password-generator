# password-generator
cmd-based password generator

## Use
I like to be able to type "password" in Windows cmd and have the script generate a password. For this, I save a separate batch file `password.bat` in a location pointed to by my PATH environment variable, which contains this text: 

```
@echo off
python "path\to\script\password.py"
```
replacing the path\to\script with the actual script path. 

Now, every time I type "password" in any cmd, I get a password randomly generated and copied to my clipboard. 

### Password management
There are many secure password managers available to deal with all these long random strings, such as [Bitwarden](https://www.bitwarden.com). 
