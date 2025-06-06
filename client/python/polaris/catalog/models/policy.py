#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

# coding: utf-8

"""
    Apache Polaris and Apache Iceberg REST Catalog API

    Defines the specification for the Polaris Catalog API, which encompasses both the Iceberg REST Catalog API and Polaris-native API.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Policy(BaseModel):
    """
    A policy in Apache Polaris defines a set of rules for governing access, data usage, and operational consistency across various catalog resources.  Policies are stored within Polaris and can be attached to catalogs, namespaces, tables, or views. For example, they can be used for fine-grained control over who can perform specific actions on certain resources.  The policy object includes - **policy-type:** The type of the policy, which determines the expected format and semantics of the policy content. - **inheritable:** A boolean flag indicating whether the policy is inheritable.  - **name:**  A human-readable name for the policy, which must be unique within a given namespace. - **description:** Detailed description of the purpose and functionalities of the policy. - **content:** Policy content, which can be validated against predefined schemas of a policy type. - **version:** Indicates the current version of the policy. Versions increased monotonically, the default value is 0  Policies stored in Polaris serve as the persistent definition for access control and governance rules. 
    """ # noqa: E501
    policy_type: StrictStr = Field(alias="policy-type")
    inheritable: StrictBool
    name: Annotated[str, Field(strict=True)] = Field(description="A policy name. A valid policy name should only consist of uppercase and lowercase letters (A-Z, a-z), digits (0-9), hyphens (-), underscores (_).")
    description: Optional[StrictStr] = None
    content: Optional[StrictStr] = None
    version: StrictInt
    __properties: ClassVar[List[str]] = ["policy-type", "inheritable", "name", "description", "content", "version"]

    @field_validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[A-Za-z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z0-9\-_]+$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Policy from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Policy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "policy-type": obj.get("policy-type"),
            "inheritable": obj.get("inheritable"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "content": obj.get("content"),
            "version": obj.get("version")
        })
        return _obj


