from setuptools import setup, find_packages

setup(
    name="prosen-pythonlib",
    version="0.1.1",  # Make sure to increment this from the previous version
    packages=find_packages(),
    author="Prosenjit Mondol",
    author_email="ug2102049@cse.pstu.ac.bd",  # ✅ Matching GitHub email
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
