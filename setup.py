from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='mpu6050',
      version='1.2',
      description='A Python module for accessing the MPU-6050 digital accelerometer and gyroscope on a Raspberry Pi.',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Libraries',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Operating System :: POSIX :: Linux',
      ],
      keywords='mpu6050 raspberry',
      url='https://github.com/everylumi/mpu6050',
      author='LUMI',
      author_email='everylumi@gmail.com',
      license='MIT',
      packages=['mpu6050'],
      scripts=['example.py'],
      zip_safe=False,
      long_description=readme())
