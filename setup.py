from setuptools import setup

setup(
    name='flask-shell',
    author='Junnplus',
    author_email='junnplus@gmail.com',
    description='Flask extension to improve shell command for the Flask CLI.',
    url='https://github.com/Junnplus/flask-shell',
    version='0.1.7',
    py_modules=['flask_shell'],
    install_requires=[
        'Flask>=1.0.0'
    ],
    extras_require={
        'ipython': ['ipython'],
        'bpython': ['bpython'],
        'ptpython': ['ptpython'],
        'ptipython': ['ptipython'],
    },
    entry_points={
        'flask.commands': [
            'shell=flask_shell:shell_command',
        ],
    },
)
