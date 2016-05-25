import ez_setup
ez_setup.use_setuptools()
from setuptools import setup as supersetup

def main():
    name = 'agilityshell'
    version = '2.0'
    author = 'Shaady Dawood'
    author_email='cgerber4@csc.com',
    scripts = []
    url = 'https://github.com/csc/csc-agility-python-shell'
    license = 'LICENSE.txt'
    description = 'Agility Shell is a command line web service client built on Python v3.4.4.  Tested and approved for use with Agility Platform REST API v3.3'
    long_description = open('README.md').read()
        
    supersetup(name=name, version=version, author=author, author_email=author_email, scripts=scripts, url=url, license=license, description=description, long_description=long_description, install_requires=["ipython == 4.0.0"])
    supersetup(name=name, version=version, install_requires=["lxml == 3.6.0"])
    supersetup(name=name, version=version, install_requires=["beautifulsoup4 == 4.4.1"])
    supersetup(name=name, version=version, install_requires=["path.py == 7.7.1"])
    supersetup(name=name, version=version, install_requires=["testpath == 0.1"])
    supersetup(name=name, version=version, install_requires=["python-dateutil == 2.5.3"])
    supersetup(name=name, version=version, install_requires=["pyreadline == 2.1"])
    supersetup(name=name, version=version, install_requires=["gnureadline == 6.3.3"])
    supersetup(name=name, version=version, install_requires=["docopt == 0.6.2"])
    supersetup(name=name, version=version, install_requires=["nose == 1.3.7"])
    supersetup(name=name, version=version, install_requires=["requests == 2.10.0"])
    supersetup(name=name, version=version, install_requires=["python-gssapi == 0.6.4"])
    supersetup(name=name, version=version, install_requires=["pycrypto == 2.6.0"])
    supersetup(name=name, version=version, install_requires=["paramiko == 1.17"])
    supersetup(name=name, version=version, install_requires=["pycurl == 7.43.0"])

if __name__ == '__main__':
    main()