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


class JobErrorDetails(Model):
    """
    The Data Lake Analytics job error details.

    :param description: Gets the error message description
    :type description: str
    :param details: Gets the details of the error message.
    :type details: str
    :param end_offset: Gets the end offset in the job where the error was
     found.
    :type end_offset: int
    :param error_id: Gets the specific identifier for the type of error
     encountered in the job.
    :type error_id: str
    :param file_path: Gets the path to any supplemental error files, if any.
    :type file_path: str
    :param help_link: Gets the link to MSDN or Azure help for this type of
     error, if any.
    :type help_link: str
    :param internal_diagnostics: Gets the internal diagnostic stack trace if
     the user requesting the job error details has sufficient permissions it
     will be retrieved, otherwise it will be empty.
    :type internal_diagnostics: str
    :param line_number: Gets the specific line number in the job where the
     error occured.
    :type line_number: int
    :param message: Gets the user friendly error message for the failure.
    :type message: str
    :param resolution: Gets the recommended resolution for the failure, if
     any.
    :type resolution: str
    :param inner_error: Gets the inner error of this specific job error
     message, if any.
    :type inner_error: :class:`JobInnerError
     <azure.mgmt.datalake.analytics.job.models.JobInnerError>`
    :param severity: Gets the severity level of the failure. Possible values
     include: 'Warning', 'Error', 'Info'
    :type severity: str
    :param source: Gets the ultimate source of the failure (usually either
     SYSTEM or USER).
    :type source: str
    :param start_offset: Gets the start offset in the job where the error was
     found
    :type start_offset: int
    """ 

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'details': {'key': 'details', 'type': 'str'},
        'end_offset': {'key': 'endOffset', 'type': 'int'},
        'error_id': {'key': 'errorId', 'type': 'str'},
        'file_path': {'key': 'filePath', 'type': 'str'},
        'help_link': {'key': 'helpLink', 'type': 'str'},
        'internal_diagnostics': {'key': 'internalDiagnostics', 'type': 'str'},
        'line_number': {'key': 'lineNumber', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'resolution': {'key': 'resolution', 'type': 'str'},
        'inner_error': {'key': 'InnerError', 'type': 'JobInnerError'},
        'severity': {'key': 'severity', 'type': 'SeverityTypes'},
        'source': {'key': 'source', 'type': 'str'},
        'start_offset': {'key': 'startOffset', 'type': 'int'},
    }

    def __init__(self, description=None, details=None, end_offset=None, error_id=None, file_path=None, help_link=None, internal_diagnostics=None, line_number=None, message=None, resolution=None, inner_error=None, severity=None, source=None, start_offset=None):
        self.description = description
        self.details = details
        self.end_offset = end_offset
        self.error_id = error_id
        self.file_path = file_path
        self.help_link = help_link
        self.internal_diagnostics = internal_diagnostics
        self.line_number = line_number
        self.message = message
        self.resolution = resolution
        self.inner_error = inner_error
        self.severity = severity
        self.source = source
        self.start_offset = start_offset