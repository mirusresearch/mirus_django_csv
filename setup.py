from setuptools import setup, find_packages

setup(
    name="mirus_django_csv",
    version="1.1.0.dev0",
    description="Takes a django queryset, or a list, or a generator and creates a csv from it",
    author="Mirus Research",
    author_email="frank@mirusresearch.com",
    packages=find_packages(),
    url='https://github.com/mirusresearch/mirus_django_csv',
    license='MIT license, see LICENSE',
    py_modules=["mirus_django_csv"],
    install_requires=[
        'six>=1.11.0',
    ],
)
