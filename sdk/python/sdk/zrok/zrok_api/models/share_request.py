# coding: utf-8

"""
    zrok

    zrok client access  # noqa: E501

    OpenAPI spec version: 0.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ShareRequest(object):
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
        'env_zid': 'str',
        'share_mode': 'str',
        'frontend_selection': 'list[str]',
        'backend_mode': 'str',
        'backend_proxy_endpoint': 'str',
        'auth_scheme': 'str',
        'auth_users': 'list[AuthUser]',
        'oauth_provider': 'str',
        'oauth_email_address_patterns': 'list[str]',
        'oauth_authorization_check_interval': 'str',
        'reserved': 'bool',
        'unique_name': 'str'
    }

    attribute_map = {
        'env_zid': 'envZId',
        'share_mode': 'shareMode',
        'frontend_selection': 'frontendSelection',
        'backend_mode': 'backendMode',
        'backend_proxy_endpoint': 'backendProxyEndpoint',
        'auth_scheme': 'authScheme',
        'auth_users': 'authUsers',
        'oauth_provider': 'oauthProvider',
        'oauth_email_address_patterns': 'oauthEmailAddressPatterns',
        'oauth_authorization_check_interval': 'oauthAuthorizationCheckInterval',
        'reserved': 'reserved',
        'unique_name': 'uniqueName'
    }

    def __init__(self, env_zid=None, share_mode=None, frontend_selection=None, backend_mode=None, backend_proxy_endpoint=None, auth_scheme=None, auth_users=None, oauth_provider=None, oauth_email_address_patterns=None, oauth_authorization_check_interval=None, reserved=None, unique_name=None):  # noqa: E501
        """ShareRequest - a model defined in Swagger"""  # noqa: E501
        self._env_zid = None
        self._share_mode = None
        self._frontend_selection = None
        self._backend_mode = None
        self._backend_proxy_endpoint = None
        self._auth_scheme = None
        self._auth_users = None
        self._oauth_provider = None
        self._oauth_email_address_patterns = None
        self._oauth_authorization_check_interval = None
        self._reserved = None
        self._unique_name = None
        self.discriminator = None
        if env_zid is not None:
            self.env_zid = env_zid
        if share_mode is not None:
            self.share_mode = share_mode
        if frontend_selection is not None:
            self.frontend_selection = frontend_selection
        if backend_mode is not None:
            self.backend_mode = backend_mode
        if backend_proxy_endpoint is not None:
            self.backend_proxy_endpoint = backend_proxy_endpoint
        if auth_scheme is not None:
            self.auth_scheme = auth_scheme
        if auth_users is not None:
            self.auth_users = auth_users
        if oauth_provider is not None:
            self.oauth_provider = oauth_provider
        if oauth_email_address_patterns is not None:
            self.oauth_email_address_patterns = oauth_email_address_patterns
        if oauth_authorization_check_interval is not None:
            self.oauth_authorization_check_interval = oauth_authorization_check_interval
        if reserved is not None:
            self.reserved = reserved
        if unique_name is not None:
            self.unique_name = unique_name

    @property
    def env_zid(self):
        """Gets the env_zid of this ShareRequest.  # noqa: E501


        :return: The env_zid of this ShareRequest.  # noqa: E501
        :rtype: str
        """
        return self._env_zid

    @env_zid.setter
    def env_zid(self, env_zid):
        """Sets the env_zid of this ShareRequest.


        :param env_zid: The env_zid of this ShareRequest.  # noqa: E501
        :type: str
        """

        self._env_zid = env_zid

    @property
    def share_mode(self):
        """Gets the share_mode of this ShareRequest.  # noqa: E501


        :return: The share_mode of this ShareRequest.  # noqa: E501
        :rtype: str
        """
        return self._share_mode

    @share_mode.setter
    def share_mode(self, share_mode):
        """Sets the share_mode of this ShareRequest.


        :param share_mode: The share_mode of this ShareRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["public", "private"]  # noqa: E501
        if share_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `share_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(share_mode, allowed_values)
            )

        self._share_mode = share_mode

    @property
    def frontend_selection(self):
        """Gets the frontend_selection of this ShareRequest.  # noqa: E501


        :return: The frontend_selection of this ShareRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._frontend_selection

    @frontend_selection.setter
    def frontend_selection(self, frontend_selection):
        """Sets the frontend_selection of this ShareRequest.


        :param frontend_selection: The frontend_selection of this ShareRequest.  # noqa: E501
        :type: list[str]
        """

        self._frontend_selection = frontend_selection

    @property
    def backend_mode(self):
        """Gets the backend_mode of this ShareRequest.  # noqa: E501


        :return: The backend_mode of this ShareRequest.  # noqa: E501
        :rtype: str
        """
        return self._backend_mode

    @backend_mode.setter
    def backend_mode(self, backend_mode):
        """Sets the backend_mode of this ShareRequest.


        :param backend_mode: The backend_mode of this ShareRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["proxy", "web", "tcpTunnel", "udpTunnel", "caddy", "drive", "socks"]  # noqa: E501
        if backend_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `backend_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(backend_mode, allowed_values)
            )

        self._backend_mode = backend_mode

    @property
    def backend_proxy_endpoint(self):
        """Gets the backend_proxy_endpoint of this ShareRequest.  # noqa: E501


        :return: The backend_proxy_endpoint of this ShareRequest.  # noqa: E501
        :rtype: str
        """
        return self._backend_proxy_endpoint

    @backend_proxy_endpoint.setter
    def backend_proxy_endpoint(self, backend_proxy_endpoint):
        """Sets the backend_proxy_endpoint of this ShareRequest.


        :param backend_proxy_endpoint: The backend_proxy_endpoint of this ShareRequest.  # noqa: E501
        :type: str
        """

        self._backend_proxy_endpoint = backend_proxy_endpoint

    @property
    def auth_scheme(self):
        """Gets the auth_scheme of this ShareRequest.  # noqa: E501


        :return: The auth_scheme of this ShareRequest.  # noqa: E501
        :rtype: str
        """
        return self._auth_scheme

    @auth_scheme.setter
    def auth_scheme(self, auth_scheme):
        """Sets the auth_scheme of this ShareRequest.


        :param auth_scheme: The auth_scheme of this ShareRequest.  # noqa: E501
        :type: str
        """

        self._auth_scheme = auth_scheme

    @property
    def auth_users(self):
        """Gets the auth_users of this ShareRequest.  # noqa: E501


        :return: The auth_users of this ShareRequest.  # noqa: E501
        :rtype: list[AuthUser]
        """
        return self._auth_users

    @auth_users.setter
    def auth_users(self, auth_users):
        """Sets the auth_users of this ShareRequest.


        :param auth_users: The auth_users of this ShareRequest.  # noqa: E501
        :type: list[AuthUser]
        """

        self._auth_users = auth_users

    @property
    def oauth_provider(self):
        """Gets the oauth_provider of this ShareRequest.  # noqa: E501


        :return: The oauth_provider of this ShareRequest.  # noqa: E501
        :rtype: str
        """
        return self._oauth_provider

    @oauth_provider.setter
    def oauth_provider(self, oauth_provider):
        """Sets the oauth_provider of this ShareRequest.


        :param oauth_provider: The oauth_provider of this ShareRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["github", "google"]  # noqa: E501
        if oauth_provider not in allowed_values:
            raise ValueError(
                "Invalid value for `oauth_provider` ({0}), must be one of {1}"  # noqa: E501
                .format(oauth_provider, allowed_values)
            )

        self._oauth_provider = oauth_provider

    @property
    def oauth_email_address_patterns(self):
        """Gets the oauth_email_address_patterns of this ShareRequest.  # noqa: E501


        :return: The oauth_email_address_patterns of this ShareRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._oauth_email_address_patterns

    @oauth_email_address_patterns.setter
    def oauth_email_address_patterns(self, oauth_email_address_patterns):
        """Sets the oauth_email_address_patterns of this ShareRequest.


        :param oauth_email_address_patterns: The oauth_email_address_patterns of this ShareRequest.  # noqa: E501
        :type: list[str]
        """

        self._oauth_email_address_patterns = oauth_email_address_patterns

    @property
    def oauth_authorization_check_interval(self):
        """Gets the oauth_authorization_check_interval of this ShareRequest.  # noqa: E501


        :return: The oauth_authorization_check_interval of this ShareRequest.  # noqa: E501
        :rtype: str
        """
        return self._oauth_authorization_check_interval

    @oauth_authorization_check_interval.setter
    def oauth_authorization_check_interval(self, oauth_authorization_check_interval):
        """Sets the oauth_authorization_check_interval of this ShareRequest.


        :param oauth_authorization_check_interval: The oauth_authorization_check_interval of this ShareRequest.  # noqa: E501
        :type: str
        """

        self._oauth_authorization_check_interval = oauth_authorization_check_interval

    @property
    def reserved(self):
        """Gets the reserved of this ShareRequest.  # noqa: E501


        :return: The reserved of this ShareRequest.  # noqa: E501
        :rtype: bool
        """
        return self._reserved

    @reserved.setter
    def reserved(self, reserved):
        """Sets the reserved of this ShareRequest.


        :param reserved: The reserved of this ShareRequest.  # noqa: E501
        :type: bool
        """

        self._reserved = reserved

    @property
    def unique_name(self):
        """Gets the unique_name of this ShareRequest.  # noqa: E501


        :return: The unique_name of this ShareRequest.  # noqa: E501
        :rtype: str
        """
        return self._unique_name

    @unique_name.setter
    def unique_name(self, unique_name):
        """Sets the unique_name of this ShareRequest.


        :param unique_name: The unique_name of this ShareRequest.  # noqa: E501
        :type: str
        """

        self._unique_name = unique_name

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
        if issubclass(ShareRequest, dict):
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
        if not isinstance(other, ShareRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
