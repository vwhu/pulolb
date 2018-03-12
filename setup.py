import os
from setuptools import setup, find_packages
PACKAGES = find_packages()

# Get version and release info, which is all stored in shablona/version.py
#ver_file = os.path.join('shablona', 'version.py')
#with open(ver_file) as f:
#    exec(f.read())

opts = dict(name='pulolb',
            maintainer='Victor Hu, Yusong Liu, Rossana Scavone, Maitri Uppaluri',
            maintainer_email='vwhu@uw.edu,',
            description='Predicting remaining usable lifetime of lithium-ion batteries',
            url='https://github.com/vwhu/PULOLB',
            download_url='DOWNLOAD_URL',
            license='MIT License',
            classifiers='3 - Alpha',
            author='Victor Hu, Yusong Liu, Rossana Scavone, Maitri Uppaluri',
            author_email='vwhu@uw.edu,',
            platforms='PLATFORMS',
            version='0.0.1',
            packages=find_packages(),
            package_data='PACKAGE_DATA',
            install_requires=['numpy', 'pandas', 'h5py', 'hdf5storage', 'fastdtw' ,'scipy', 'matplotlib'],
            requires='REQUIRES')


if __name__ == '__main__':
    setup(**opts)
