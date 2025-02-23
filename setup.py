from setuptools import setup, find_packages

setup(
    name = 'KeyManagement',
    version = '0.1',
    description = 'A simple key management package using encryption and pass keys',
    long_description = open('README.md').read(),
    long_description_content_type='text/markdown',
    author = 'Michael Hanson',
    author_email='michael.hanson@atelier-therapeutics.com',
    url = 'https://github.com/mhanson2019/KeyManagement',
    packages = find_packages(),
    install_requires=[
        'cryptography',
    ],
    entry_points = {
        'console_scripts': [
            'setKeys = KeyManagement.setKeys:main',
            'getKeys = KeyManagement.getKeys:main',
        ],
    },
    python_requires='>=3.6'
    
)
