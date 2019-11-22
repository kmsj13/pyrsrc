import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyrsrc",
    version="1.0.0",
    author="Kevin San Jose",
    author_email="kmsj13@gmail.com",
    description="A set of functions to get System Resource using python",
	license='',
    url="https://github.com/kmsj13/pyrsrc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2/3",
        "Operating System :: OS Independent",
    ],
)