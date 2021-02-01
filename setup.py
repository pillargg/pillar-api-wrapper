import setuptools

with open('README.md') as readme:
    long_desc = readme.read()

setuptools.setup(
    name='pillar-api-wrapper',
    version='0.0.1',
    author="PillarGG",
    author_email='opensource@pillar.gg',
    description='Python wrapper for our REST API.',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url='https://github.com/pillargg/pillar-api-wrapper',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.25.0'
    ]
)
