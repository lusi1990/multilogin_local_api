# coding: utf-8

"""
    Multilogin Local REST API

    Multilogin Local REST API can be used in order to start, stop, share, clone browser profile/-s. You can also check if the profile is already running on your machine by using checkProfileRunning endpoint and import cookies by using cookieImportJSON/cookieImportNetscape endpoint.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class CloneOkResonse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'status': 'str',
        'value': 'list[str]'
    }

    attribute_map = {
        'status': 'status',
        'value': 'value'
    }

    def __init__(self, status=None, value=None):  # noqa: E501
        """CloneOkResonse - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._value = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if value is not None:
            self.value = value

    @property
    def status(self):
        """Gets the status of this CloneOkResonse.  # noqa: E501


        :return: The status of this CloneOkResonse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CloneOkResonse.


        :param status: The status of this CloneOkResonse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def value(self):
        """Gets the value of this CloneOkResonse.  # noqa: E501


        :return: The value of this CloneOkResonse.  # noqa: E501
        :rtype: list[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CloneOkResonse.


        :param value: The value of this CloneOkResonse.  # noqa: E501
        :type: list[str]
        """

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CloneOkResonse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CloneOkResonse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
