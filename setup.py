from setuptools import setup, find_packages
from setuptools.command.install import install
import logging

class CustomInstallCommand(install):
    """Custom installation to create directories before installation."""
    
    def run(self):
        # Call the standard install process first
        install.run(self)
        
        # Custom actions after standard install
        self.create_file()

    def create_file(self):
        logging.info("Creating file")
        with open("/tmp/pwn", "w") as file:
            file.write("Hello, pwned!")


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="filecreation",
    version="0.1.0",
    author="Lorenzo Susini",
    author_email="your.email@example.com",
    description="A short description of your package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your-repo",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    cmdclass={
        'install': CustomInstallCommand,
    },
)

