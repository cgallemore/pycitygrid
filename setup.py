from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

requires = ['requests']

setup(
    name='pycitygrid',
    version='0.0.1',
    description='Python wrapper for CityGrid API',
    long_description=readme,
    author='Chad Gallemore',
    author_email='cgallemore@gmail.com',
    url='https://github.com/cgallemore/pycitygrid',
    license=license,
    install_requires=requires,
    packages=find_packages(exclude=('tests', 'docs', 'venv',))
)
