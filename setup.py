from setuptools import setup, find_packages

setup(
    name='owais4u',
    version='1.0',
    description='A short description of your package',
    long_description='A longer description of your package',
    author_email='ahmadowais2@gmail.com',
    url='https://github.com/ahmadOwais/owais4u/tree/main/assignment1',
    packages=find_packages(),  # Automatically find and include all Python packages
    install_requires=[
        # List your package dependencies here
        'numpy>=1.18.0',
        'requests>=2.24.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
