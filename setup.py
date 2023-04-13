import setuptools

setuptools.setup(
    name="cfrgan",
    version="1.0.2",
    author="",
    author_email="",
    description="CFR-GAN package",
    packages=setuptools.find_packages() + [".cfrgan"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

