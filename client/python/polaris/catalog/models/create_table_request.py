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
    Apache Iceberg REST Catalog API

    Defines the specification for the first version of the REST Catalog API. Implementations should ideally support both Iceberg table specs v1 and v2, with priority given to v2.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from polaris.catalog.models.model_schema import ModelSchema
from polaris.catalog.models.partition_spec import PartitionSpec
from polaris.catalog.models.sort_order import SortOrder
from typing import Optional, Set
from typing_extensions import Self

class CreateTableRequest(BaseModel):
    """
    CreateTableRequest
    """ # noqa: E501
    name: StrictStr
    location: Optional[StrictStr] = None
    var_schema: ModelSchema = Field(alias="schema")
    partition_spec: Optional[PartitionSpec] = Field(default=None, alias="partition-spec")
    write_order: Optional[SortOrder] = Field(default=None, alias="write-order")
    stage_create: Optional[StrictBool] = Field(default=None, alias="stage-create")
    properties: Optional[Dict[str, StrictStr]] = None
    __properties: ClassVar[List[str]] = ["name", "location", "schema", "partition-spec", "write-order", "stage-create", "properties"]

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
        """Create an instance of CreateTableRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of partition_spec
        if self.partition_spec:
            _dict['partition-spec'] = self.partition_spec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of write_order
        if self.write_order:
            _dict['write-order'] = self.write_order.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateTableRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "location": obj.get("location"),
            "schema": ModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "partition-spec": PartitionSpec.from_dict(obj["partition-spec"]) if obj.get("partition-spec") is not None else None,
            "write-order": SortOrder.from_dict(obj["write-order"]) if obj.get("write-order") is not None else None,
            "stage-create": obj.get("stage-create"),
            "properties": obj.get("properties")
        })
        return _obj


