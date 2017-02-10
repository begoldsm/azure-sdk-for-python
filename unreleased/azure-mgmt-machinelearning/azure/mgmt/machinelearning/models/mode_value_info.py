# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ModeValueInfo(Model):
    """Nested parameter definition.

    :param interface_string: The interface string name for the nested
     parameter.
    :type interface_string: str
    :param parameters: The definition of the parameter.
    :type parameters: list of :class:`ModuleAssetParameter
     <azure.mgmt.machinelearning.models.ModuleAssetParameter>`
    """

    _attribute_map = {
        'interface_string': {'key': 'interfaceString', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '[ModuleAssetParameter]'},
    }

    def __init__(self, interface_string=None, parameters=None):
        self.interface_string = interface_string
        self.parameters = parameters
