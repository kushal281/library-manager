from setuptools import setup

setup(
    name='library-manager',
    version='1.0.0',
    py_modules=['library_manager'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'library-manager=library_manager:main',
        ],
    },
    author='Kushal Agarwal',
    description='A simple CLI to manage Python packages via pip',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
)