from setuptools import setup

setup(
    name="qotd",
    version="0.1",
    url='https://github.atl.damballa/recursiveMake/',
    package_dir={'qotd': 'src/qotd'},
    packages=['qotd'],
    description="Quote-of-the-day app",
    install_requires=[
        'flask',
        'sqlalchemy'
    ],
    data_files=[
        ('/var/www/qotd', ['data/qotd.wsgi']),
        ('/etc/apache2/sites-available', ['data/qotd_host'])
    ]
)
