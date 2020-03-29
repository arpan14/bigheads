from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='bigheads',
      version='0.1.1',
      author='Arpan Mishra',
      author_email='akmish3@gmail.com',
      description='Scrape topics from GeeksforGeeks and convert to PDF',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/arpan14/bigheads',
      license='GPL V3',
      packages=['bigheads'],
      entry_points={
          'console_scripts': ['bigheads=bigheads:main'],
      },
      classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Students',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GPL V3',
        # Operating Systems
        'Operating System :: OS Independent',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
      ],
      install_requires=[
          'bs4','httplib2','pdfkit'
      ],
      zip_safe=False)