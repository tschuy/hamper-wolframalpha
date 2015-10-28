from distutils.core import setup

with open('requirements.txt') as f:
    requirements = [l.strip() for l in f]

setup(
    name='wolframbot',
    version='0.1',
    packages=['wolframbot'],
    author='Evan Tschuy',
    author_email='evantschuy@gmail.com',
    url='https://github.com/tschuy/hamper-wolframalpha',
    install_requires=requirements,
    package_data={'cah': ['requirements.txt', 'README.rst', 'LICENSE']},
    entry_points={
        'hamperbot.plugins': [
            'wolfram = wolframbot.wolfram:Wolfram'
        ],
    },
)
