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


class JobReleaseTaskExecutionInformation(Model):
    """
    Contains information about the execution of a Job Release task on a
    compute node.

    :param start_time: Gets or sets the time at which the Job Release task
     started running.
    :type start_time: datetime
    :param end_time: Gets or sets the time at which the Job Release task
     completed. This property is set only if the task is in the Completed
     state.
    :type end_time: datetime
    :param state: Gets or sets the current running state of the Job Release
     task on the compute node. Possible values include: 'running', 'completed'
    :type state: str
    :param task_root_directory: Gets or sets the root directory of the Job
     Release task on the compute node.
    :type task_root_directory: str
    :param task_root_directory_url: Gets or sets the URL to the root
     directory of the Job Release task on the compute node.
    :type task_root_directory_url: str
    :param exit_code: Gets or sets the exit code of the Job Release task.
     This property is set only if the task is in the Completed state.
    :type exit_code: int
    :param scheduling_error: Gets or sets any error starting the Job Release
     task.
    :type scheduling_error: :class:`TaskSchedulingError
     <azure.batch.models.TaskSchedulingError>`
    """ 

    _validation = {
        'start_time': {'required': True},
        'state': {'required': True},
    }

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'JobReleaseTaskState'},
        'task_root_directory': {'key': 'taskRootDirectory', 'type': 'str'},
        'task_root_directory_url': {'key': 'taskRootDirectoryUrl', 'type': 'str'},
        'exit_code': {'key': 'exitCode', 'type': 'int'},
        'scheduling_error': {'key': 'schedulingError', 'type': 'TaskSchedulingError'},
    }

    def __init__(self, start_time, state, end_time=None, task_root_directory=None, task_root_directory_url=None, exit_code=None, scheduling_error=None, **kwargs):
        self.start_time = start_time
        self.end_time = end_time
        self.state = state
        self.task_root_directory = task_root_directory
        self.task_root_directory_url = task_root_directory_url
        self.exit_code = exit_code
        self.scheduling_error = scheduling_error