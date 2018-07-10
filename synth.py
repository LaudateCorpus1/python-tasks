# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This script is used to synthesize generated parts of this library."""

import synthtool as s
import synthtool.gcp as gcp
import logging

logging.basicConfig(level=logging.DEBUG)

gapic = gcp.GAPICGenerator()
common = gcp.CommonTemplates()

# tasks has two product names, and a poorly named artman yaml
v2beta2_library = gapic.py_library(
    'tasks', 'v2beta2',
    config_path='artman_cloudtasks.yaml')

s.copy(v2beta2_library)

# Set Release Status
release_status = 'Development Status :: 3 - Alpha'
s.replace('setup.py',
          '(release_status = )(.*)$',
          f"\\1'{release_status}'")

# Add Dependencies
s.replace('setup.py',
          'dependencies = \[\n*(^.*,\n)+',
          "\\g<0>    'grpc-google-iam-v1<0.12dev,>=0.11.4',\n")

# Correct Naming of package
s.replace('**/*.rst',
          'google-cloud-cloud-tasks',
          'google-cloud-tasks')
s.replace('**/*.py',
          'google-cloud-cloud-tasks',
          'google-cloud-tasks')
s.replace('README.rst',
          '/cloud-tasks',
          '/tasks')

# Fix the enable API link
s.replace(
    'README.rst',
    r'.. _Enable the Cloud Tasks API.:  https://cloud.google.com/tasks',
    '.. _Enable the Cloud Tasks API.:  https://console.cloud.google.com/apis/'
    'library/cloudtasks.googleapis.com')
