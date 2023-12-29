from setuptools import setup, find_packages

setup(
    name='econkit',  # Ensure this matches with your PyPI package name
    version='0.0.1',
    packages=find_packages(),
    description='Advanced Econometric Analysis Tools',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Stefanos Stavrianos',
    author_email='contact@stefanstavrianos.eu',  # Verify this email
    url='https://github.com/stefanstavrianos/econkit',  # Replace with your actual URL
    install_requires=[
        'numpy',
        'pandas',
        'scipy'
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD 3-Clause License',  # Correct the license here
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Science/Research',
        'Topic :: Office/Business :: Financial',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ]
)
