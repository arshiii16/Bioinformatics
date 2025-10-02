from setuptools import setup, find_packages

setup(
    name='fasta-analyzer-gui',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'tkinter',  # or 'PyQt5' if using PyQt
        # Add other dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            'fasta-analyzer=fasta-analyzer-gui.main:main',  # Adjust based on your main function
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A GUI application for analyzing FASTA files and displaying symbol percentages.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/fasta-analyzer-gui',  # Replace with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Change if using a different license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)