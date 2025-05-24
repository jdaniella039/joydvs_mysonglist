from setuptools import setup, find_packages

requires = [
    'pyramid',
    'pyramid_jwt',
    'passlib',
    'waitress',
]

setup(
    name='mysonglist',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = mysonglist.__init__:main',
        ],
    },
)
