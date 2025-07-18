from setuptools import setup, find_packages

setup(
    name="prosen-pythonlib",  # Must be unique on PyPI
    version="0.1.0",
    packages=find_packages(),
    author="Prosenjit Mondol",
    description="A simple greeting package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
