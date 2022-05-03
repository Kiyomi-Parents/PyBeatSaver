import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Requirements
requirements = []
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements += f.read().splitlines()

extras_require = {
    'test': [
        'coverage',
        'pytest',
        'pytest-asyncio',
        'pytest-cov'
    ]
}

setuptools.setup(
    name="PyBeatSaver",
    version="0.1.9",
    author="LuCkEr-",
    author_email="lucker@lucker.xyz",
    description="Beat Saver API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kiyomi-Parents/PyBeatSaver",
    project_urls={
        "Bug Tracker": "https://github.com/Kiyomi-Parents/PyBeatSaver/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require=extras_require,
)
