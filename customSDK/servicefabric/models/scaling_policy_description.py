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


class ScalingPolicyDescription(Model):
    """Describes how the scaling should be performed.

    :param scaling_trigger: Specifies the trigger associated with this scaling
     policy
    :type scaling_trigger:
     ~azure.servicefabric.models.ScalingTriggerDescription
    :param scaling_mechanism: Specifies the mechanism associated with this
     scaling policy
    :type scaling_mechanism:
     ~azure.servicefabric.models.ScalingMechanismDescription
    """

    _validation = {
        'scaling_trigger': {'required': True},
        'scaling_mechanism': {'required': True},
    }

    _attribute_map = {
        'scaling_trigger': {'key': 'ScalingTrigger', 'type': 'ScalingTriggerDescription'},
        'scaling_mechanism': {'key': 'ScalingMechanism', 'type': 'ScalingMechanismDescription'},
    }

    def __init__(self, scaling_trigger, scaling_mechanism):
        super(ScalingPolicyDescription, self).__init__()
        self.scaling_trigger = scaling_trigger
        self.scaling_mechanism = scaling_mechanism