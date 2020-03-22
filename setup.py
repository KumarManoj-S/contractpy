from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='contractpy',
    packages=find_packages(),
    version='0.1.4',
    license='MIT',
    description='A tiny library for validating our data if its adhere the contract.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Manoj Kumar S',
    author_email='kumarmanoj1158@gmail.com',
    url='https://github.com/KumarManoj-S/contractpy',
    download_url='https://github.com/KumarManoj-S/contractpy/archive/0.1.4.tar.gz',
    keywords=['contract', 'contract testing', 'template', 'validate'],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
