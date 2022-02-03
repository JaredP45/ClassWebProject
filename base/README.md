# Butler Capstone Website

Author: Jared Paubel

**Note**: This is assuming you are using Unix/Linux terminals; use Git Bash software to follow the commands below unless you are familiar with windows terminal.

## Pulling Down for First Time:
For initial setup follow these steps.
1. Copy remote repository link https://github.com/JaredP45/ClassWebProject/  and get .env file from me (I'll find a way to share keys).


2. In terminal, type ```git clone https://github.com/JaredP45/ClassWebProject/```
   * Terminal will clone the repository in your desired location (recommend /Desktop for testing).
   * This respository includes the venv (virtual environment) which allows access to python.


3. ```cd base/``` to access manage.py and use ```ll``` or ```ls -l``` to observe directory.
   * (```base``` is project parent which has ```manage.py```, where ```base/base``` has config files like settings.)


4. Enter ```python manage.py runserver``` to run server, and check on ```http://127.0.0.1:8000/```
   * If you get a django page that says "The install worked successfully! Congratulations!" you did it!

## Updating:
If there is an update on the remote repository (GitHub), follow these steps to update your local copy. 

1. ```git status``` to check what's been staged or changed.


2. ```git pull origin master``` to pull down what you don't have (i.e. update your copy)


3. Inside ClassWebProject/base/, run localhost server ```python manage.py runserver``` and check if it runs without issue.


## Sending Your Local Update:
If you added, changed, or removed anything, follow these steps:
1. ```git status``` and look for red lines (this indicates that the changes have not been staged).


3. ```git add .``` or ```git add *``` or ```git add /path/to/file``` to add your changes.


4. ```git status``` and look for green lines (this indicates that the changes have been added and are ready for committing).


5. ```git commit -m "your message here"``` or ```git commit``` to open vim/nano and make custom message.


6. ```git status``` and you should see no green or red lines unless you intentionally left out certain files to be ignored.
   * To see how many commits you've made, you should see "Your local repository is ahead by x commits" or you can use ```git log``` to see the commit history.


7. Set your git config ```git config --global user.name "YOUR-GITHUB-USER-NAME"``` and ```git config --global user.password "YOUR-GITHUB-PASSWORD"```


8. ```git push origin master``` to finally push up your changes.
   * This will then ask for your github user name and password. Github recently deprecated the use of user passwords for pushing, so you will need a repository key from Jared and enter it for the password.

   
📧 Imagine this process like sending a letter. 
* 🧾 You write your letter (make changes). 
* 📩 You put the letter in the envelope (add/remove changes).
* 📨 Seal the letter with the proper markings on it (committing changes).
* 📮 Then you take it to the post office for shipping (pushing up your changes.)