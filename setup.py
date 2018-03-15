from setuptools import setup, find_packages

setup(
    name='flask-heroku-example',
    packages=find_packages(),
    version='0.1',
    description='A example practice heroku flask application.',
    author='Justin Beall',
    author_email='jus.beall@gmail.com',
    keywords=['dev3l', 'python', 'flask',],
    install_requires=[
        'flask',
        'flask-runner',
        'flask-wtf',
        'gunicorn',
        # tests / ci
        'bandit',
        'coverage',
        'coveralls',
        'pylint',
        'pytest'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)
