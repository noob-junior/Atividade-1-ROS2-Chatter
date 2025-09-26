from setuptools import find_packages, setup

package_name = 'my_chatter_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Heitor Gavioli', 
    maintainer_email='heitor.gavioli.ufu@gmail.com',  
    description='', 
    license='Apache-2.0', 
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = my_chatter_pkg.talker:main',
            'listener = my_chatter_pkg.listener:main', 
        ],
    },
)
