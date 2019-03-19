from setuptools import setup, find_packages

setup(
    name='recsort',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA python recursion and sorting package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/momolunar/mypackage',
    author='Monde Colephi',
    author_email='<mondelunar@gmail.com>'
)
