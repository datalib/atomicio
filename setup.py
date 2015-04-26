from setuptools import setup


setup(
    name='atomicio',
    version='0.1.0',
    description='Atomic file writes for Python',
    long_description=open('README.rst').read(),

    author='Eeo Jun',
    author_email='packwolf58@gmail.com',
    url='https://github.com/datalib/atomicio',
    packages=['atomicio'],
    license='MIT',

    include_package_data=True,
    install_requires=[],
)
