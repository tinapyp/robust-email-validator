from setuptools import setup, find_packages

setup(
    name="RobustEmailValidator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pydantic",
        "dnspython",
        "requests",
    ],
    description="A simple email validation library",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/tinapyp/RobustEmailValidator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
