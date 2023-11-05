from setuptools import setup, find_packages

setup(
    name='cli',
    packages=find_packages(),
    author='Sadiq Said',
    install_requires=[
        'click',
        'requests'
    ],
    version='0.0.1',
    entry_points='''
    [console_scripts]
    cli=cli:cli
    '''
)