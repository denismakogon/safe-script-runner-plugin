#   Copyright 2015, Denis Makogon
#   All Rights Reserved.
#
#    Licensed under the GNU GENERAL PUBLIC LICENSE,
#    Version 2.0 (the "License"); you may not use this
#    file except in compliance with the License.
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from setuptools import setup

setup(
    name='safe_script_runner_plugin',
    version='1.2.0m1',
    author='Denis Makogon',
    author_email='lildee1991@gmail.com',
    packages=['safe_script_runner_plugin'],
    license='LICENSE',
    description='Plugin for remotely running fabric run_script task',
    install_requires=[
        'cloudify-plugins-common==3.2',
        'fabric==1.8.3',
        'six>=1.8.0',
    ]
)
