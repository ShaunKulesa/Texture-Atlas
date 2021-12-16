from setuptools import setup

with open("README.rst") as file:
    readme = file.read()

setup(
  name = 'Texture_Atlas',
  packages = ['Texture_Atlas'],
  version = '0.3.1',
  license='MIT',
  description = 'Create a texture dynamic texture atlas you can constantly change.',
  author = 'Shaun Kulesa',
  author_email = 'shaunkulesa@gmail.com',
  url = 'https://github.com/ShaunKulesa/Texture-Atlas',
  download_url = 'https://github.com/ShaunKulesa/Texture-Atlas',
  keywords = ['Texture Atlas'],
  install_requires=[
          'pillow',
          'rectpack',
      ],
  long_description = readme,
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.5',
  ],
)