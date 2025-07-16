"""
Setup do Compilador Pascal
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pascal-compiler",
    version="1.0.0",
    author="Lucas Guimarães Borges (lcsgborges)",
    author_email="lcsgborges@gmail.com",
    description="Um compilador/interpretador de Pascal implementado em Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/pascal-compiler",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "pascal-compiler=compiler:main",
        ],
    },
)
