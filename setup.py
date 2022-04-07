from setuptools import setup

setup(
    name='ovex_py',
    version='0.0.1',    
    description='A package to interact with OVEX API',
    url='https://github.com/Quirky-Fox/OVEX-py',
    author='Duncan Andrew',
    author_email='duncan@lumina-x.com',
    license='MIT',
    packages=['ovex_python'],
    install_requires=['requests'],
    keywords='OVEX cryptocurrency exchange API',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Office/Business :: Financial',
        'Topic :: Utilities',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
    ],
)