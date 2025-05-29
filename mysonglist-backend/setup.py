from setuptools import setup, find_packages

requires = [
    'pyramid',
    'pyramid_jwt',
    'passlib',
    'sqlalchemy',
    'psycopg2-binary',
    'waitress',
]

setup(
    name='mysonglist',
    version='1.0',
    description='MySongList Backend API',
    packages=find_packages(),  # WAJIB: untuk mengenali folder mysonglist/
    include_package_data=True,
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = mysonglist.__init__:main',
        ],
    },
    zip_safe=False,
)
