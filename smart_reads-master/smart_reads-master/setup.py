from setuptools import setup, find_packages
SRC_REPO='src'
setup(
    name='smart_reads',               
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'numpy',
        'pandas',
        'scikit-learn',
        'pickle-mixin',  # Add this
    ],
    entry_points={
        'console_scripts': [
            # Optional: if you add a main() function in app.py, this enables CLI run as `run-app`
            'run-app = app:main',
        ],
    },
    author='Syamala',                             
    author_email='yasarapusyamala@gmail.com',     
    description='A Great Reads Starts From Single Suggestions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Syam2005/smart_reads', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Streamlit',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
