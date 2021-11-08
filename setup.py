import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gwx",
    version="1.0",
    author="RaphGL",
    author_email="raphfl.dev@gmail.com",
    description="Get weather information on your terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RaphGL/gwx",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD 2-clause Simplified License",
        "Operating System :: OS Independent",
    ],
    python_requires=">= 3.7",
    install_requires=[
        "requests",
        "beautifulsoup4",
    ]
)
