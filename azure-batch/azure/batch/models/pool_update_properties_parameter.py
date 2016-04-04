# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PoolUpdatePropertiesParameter(Model):
    """
    Parameters for a CloudPoolOperations.UpdateProperties request.

    :param start_task: Sets a task to run on each compute node as it joins
     the pool. If omitted, any existing start task is removed from the pool.
    :type start_task: :class:`StartTask <azure.batch.models.StartTask>`
    :param certificate_references: Sets a list of certificates to be
     installed on each compute node in the pool. If you specify an empty
     collection, any existing certificate references are removed from the
     pool.
    :type certificate_references: list of :class:`CertificateReference
     <azure.batch.models.CertificateReference>`
    :param application_package_references: Sets a list of application
     packages to be installed on each compute node in the pool. If you
     specify an empty collection, any existing application packages
     references are removed from the pool.
    :type application_package_references: list of
     :class:`ApplicationPackageReference
     <azure.batch.models.ApplicationPackageReference>`
    :param metadata: Sets a list of name-value pairs associated with the pool
     as metadata. If you specify an empty collection, any existing metadata
     is removed from the pool.
    :type metadata: list of :class:`MetadataItem
     <azure.batch.models.MetadataItem>`
    """ 

    _validation = {
        'certificate_references': {'required': True},
        'application_package_references': {'required': True},
        'metadata': {'required': True},
    }

    _attribute_map = {
        'start_task': {'key': 'startTask', 'type': 'StartTask'},
        'certificate_references': {'key': 'certificateReferences', 'type': '[CertificateReference]'},
        'application_package_references': {'key': 'applicationPackageReferences', 'type': '[ApplicationPackageReference]'},
        'metadata': {'key': 'metadata', 'type': '[MetadataItem]'},
    }

    def __init__(self, certificate_references, application_package_references, metadata, start_task=None, **kwargs):
        self.start_task = start_task
        self.certificate_references = certificate_references
        self.application_package_references = application_package_references
        self.metadata = metadata