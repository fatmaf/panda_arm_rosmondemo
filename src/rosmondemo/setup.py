import os
from glob import glob
from setuptools import setup

package_name = 'rosmondemo'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name),glob('launch/*launch.[pxy][yma]*')),
        (os.path.join('share',package_name),glob('launch/*.launch')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robotlab',
    maintainer_email='ffaruq@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'monitor_verdict_visualiser = rosmondemo.monitor_verdict_visualiser:main',
            'listener = rosmondemo.meh:main',
        ],
    },
)
