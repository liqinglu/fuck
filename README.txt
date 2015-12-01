PURPOSE:
This project used in linux environment.

Sometimes, we may type wrong command, at this moment, we think it's better to get help from system: "Oh, your should type this correct command", so "fuck" borns.
In this case, your should type "fuck", it will tell you that you probably are going to find the command with the most nearest similarity.

PREREQUSTITY:
python installed
create '.fuck' directory in $HOME directory

USAGE:
Before usage, add one alias in SHELL source file(.bashrc etc...):

	alias fuck = "history >~/.fuck/historycmd; python <abspath>/getfuck.py"
	
activate this source file or relogin into shell

when type wrong command, you can type "fuck" to get command which is most similarity with the last command