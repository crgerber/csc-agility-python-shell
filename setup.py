import ez_setup
ez_setup.use_setuptools()
from setuptools import setup

setup(
    name='AgilityPythonShell',
    version='1.1.3',
    author='Shaady Dawood',
    author_email='shady.dawood@servicemesh.com',
    scripts=[],
    url='https://github.com/ServiceMesh/agility-python-shell',
    license='LICENSE.txt',
    description='Agility Python REST Client',
    long_description=open('README.txt').read(),
    install_requires=[
	"ipython",
        "python-dateutil >= 1.5",
        "beautifulsoup4 >= 4.0.0",
        "lxml >= 3.0.0",
    ],
)
