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


class FileStatusProperties(Model):
    """
    Data Lake Store file or directory information.

    :param access_time: Gets the last access time as ticks since the epoch.
    :type access_time: long
    :param block_size: Gets the block size for the file.
    :type block_size: long
    :param children_num: Gets the number of children in the directory.
    :type children_num: long
    :param group: Gets the group owner.
    :type group: str
    :param length: Gets the number of bytes in a file.
    :type length: long
    :param modification_time: Gets the modification time as ticks since the
     epoch.
    :type modification_time: long
    :param owner: Gets the user who is the owner.
    :type owner: str
    :param path_suffix: Gets the path suffix.
    :type path_suffix: str
    :param permission: Gets the permission represented as an string.
    :type permission: str
    :param type: Gets the type of the path object. Possible values include:
     'FILE', 'DIRECTORY'
    :type type: str
    """ 

    _attribute_map = {
        'access_time': {'key': 'accessTime', 'type': 'long'},
        'block_size': {'key': 'blockSize', 'type': 'long'},
        'children_num': {'key': 'childrenNum', 'type': 'long'},
        'group': {'key': 'group', 'type': 'str'},
        'length': {'key': 'length', 'type': 'long'},
        'modification_time': {'key': 'modificationTime', 'type': 'long'},
        'owner': {'key': 'owner', 'type': 'str'},
        'path_suffix': {'key': 'pathSuffix', 'type': 'str'},
        'permission': {'key': 'permission', 'type': 'str'},
        'type': {'key': 'type', 'type': 'FileType'},
    }

    def __init__(self, access_time=None, block_size=None, children_num=None, group=None, length=None, modification_time=None, owner=None, path_suffix=None, permission=None, type=None):
        self.access_time = access_time
        self.block_size = block_size
        self.children_num = children_num
        self.group = group
        self.length = length
        self.modification_time = modification_time
        self.owner = owner
        self.path_suffix = path_suffix
        self.permission = permission
        self.type = type