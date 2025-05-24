from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jwt',
    'sqlalchemy',
    'psycopg2-binary',
    'passlib'
]

setup(
    name='mysonglist',
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = mysonglist:main'
        ],
    },
)
