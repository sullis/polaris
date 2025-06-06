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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from polaris.catalog.models.expression import Expression
from typing import Optional, Set
from typing_extensions import Self

class PlanTableScanRequest(BaseModel):
    """
    PlanTableScanRequest
    """ # noqa: E501
    snapshot_id: Optional[StrictInt] = Field(default=None, description="Identifier for the snapshot to scan in a point-in-time scan", alias="snapshot-id")
    select: Optional[List[StrictStr]] = Field(default=None, description="List of selected schema fields")
    filter: Optional[Expression] = Field(default=None, description="Expression used to filter the table data")
    case_sensitive: Optional[StrictBool] = Field(default=True, description="Enables case sensitive field matching for filter and select", alias="case-sensitive")
    use_snapshot_schema: Optional[StrictBool] = Field(default=False, description="Whether to use the schema at the time the snapshot was written. When time travelling, the snapshot schema should be used (true). When scanning a branch, the table schema should be used (false).", alias="use-snapshot-schema")
    start_snapshot_id: Optional[StrictInt] = Field(default=None, description="Starting snapshot ID for an incremental scan (exclusive)", alias="start-snapshot-id")
    end_snapshot_id: Optional[StrictInt] = Field(default=None, description="Ending snapshot ID for an incremental scan (inclusive). Required when start-snapshot-id is specified.", alias="end-snapshot-id")
    stats_fields: Optional[List[StrictStr]] = Field(default=None, description="List of fields for which the service should send column stats.", alias="stats-fields")
    __properties: ClassVar[List[str]] = ["snapshot-id", "select", "filter", "case-sensitive", "use-snapshot-schema", "start-snapshot-id", "end-snapshot-id", "stats-fields"]

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
        """Create an instance of PlanTableScanRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PlanTableScanRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "snapshot-id": obj.get("snapshot-id"),
            "select": obj.get("select"),
            "filter": Expression.from_dict(obj["filter"]) if obj.get("filter") is not None else None,
            "case-sensitive": obj.get("case-sensitive") if obj.get("case-sensitive") is not None else True,
            "use-snapshot-schema": obj.get("use-snapshot-schema") if obj.get("use-snapshot-schema") is not None else False,
            "start-snapshot-id": obj.get("start-snapshot-id"),
            "end-snapshot-id": obj.get("end-snapshot-id"),
            "stats-fields": obj.get("stats-fields")
        })
        return _obj


