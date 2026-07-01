#!/usr/bin/env python3
"""Fix the Veeam Backup for Azure OpenAPI schema for openapi-python-client.

Usage:
  python fix_openapi_schema.py <input.json> <output.json>

The Veeam Backup for Azure spec uses `nullable: true` in three places that
openapi-python-client (0.28.x) cannot represent. Each is rewritten below; the
input file is left untouched and the corrected spec is written to <output>.

A. Nullable path parameters -> "None | str is not allowed in path".
   A URL path segment can never be None, so `nullable` is dropped from every
   `in: path` parameter (and its schema).

B. Nullable inline object schemas -> "Invalid property in union ...", which
   aborts generation entirely. A nullable object (`type: object` with
   `properties`) becomes a `<Name>_type_0` union that the generator fails to
   process when the object is nested inside another nullable schema (e.g.
   BackupWindowSettings.window). `nullable` is dropped from every object
   schema that declares `properties`; the field stays optional via `required`.

C. Nullable scalar request bodies -> invalid generated Python ("Expected a
   statement": a bare `else:` with no `if`). `nullable` is dropped from request
   body schemas whose type is a scalar (string/integer/number/boolean).
   Nullable array bodies generate fine and are left alone.
"""

import json
import sys
from typing import Any, cast

HTTP_METHODS = ("get", "post", "put", "delete", "patch", "options", "head", "trace")
SCALAR_TYPES = {"string", "integer", "number", "boolean"}


def _pop_nullable(node: Any) -> bool:
    """Remove a truthy `nullable` from a schema dict. Return True if removed."""
    if isinstance(node, dict) and node.get("nullable") is True:
        del cast("dict[str, Any]", node)["nullable"]
        return True
    return False


def strip_object_nullable(node: Any, counts: "dict[str, int]") -> None:
    """Rule B: recursively drop `nullable` from object schemas with properties."""
    if isinstance(node, dict):
        node_dict = cast("dict[str, Any]", node)
        if node_dict.get("type") == "object" and isinstance(
            node_dict.get("properties"), dict
        ):
            if _pop_nullable(node_dict):
                counts["objects"] += 1
        for value in node_dict.values():
            strip_object_nullable(value, counts)
    elif isinstance(node, list):
        for item in cast("list[Any]", node):
            strip_object_nullable(item, counts)


def fix_path_params(params: Any, counts: "dict[str, int]") -> None:
    """Rule A: drop `nullable` from `in: path` parameters and their schema."""
    if not isinstance(params, list):
        return
    for param in cast("list[Any]", params):
        if not isinstance(param, dict) or param.get("in") != "path":
            continue
        param_dict = cast("dict[str, Any]", param)
        if _pop_nullable(param_dict):
            counts["path_params"] += 1
        if _pop_nullable(param_dict.get("schema")):
            counts["path_params"] += 1


def fix_request_body(request_body: Any, counts: "dict[str, int]") -> None:
    """Rule C: drop `nullable` from scalar request body schemas."""
    if not isinstance(request_body, dict):
        return
    content = request_body.get("content")
    if not isinstance(content, dict):
        return
    for media in cast("dict[str, Any]", content).values():
        if not isinstance(media, dict):
            continue
        schema = media.get("schema")
        if isinstance(schema, dict) and schema.get("type") in SCALAR_TYPES:
            if _pop_nullable(schema):
                counts["scalar_bodies"] += 1


def fix(data: Any) -> "dict[str, int]":
    if not isinstance(data, dict):
        raise RuntimeError("OpenAPI root must be an object")

    counts = {"path_params": 0, "objects": 0, "scalar_bodies": 0}

    # Rule B spans the whole document (components + inline schemas).
    strip_object_nullable(data, counts)

    paths = data.get("paths")
    if isinstance(paths, dict):
        for path_item in cast("dict[str, Any]", paths).values():
            if not isinstance(path_item, dict):
                continue
            path_item_dict = cast("dict[str, Any]", path_item)
            fix_path_params(path_item_dict.get("parameters"), counts)
            for method in HTTP_METHODS:
                operation = path_item_dict.get(method)
                if isinstance(operation, dict):
                    op_dict = cast("dict[str, Any]", operation)
                    fix_path_params(op_dict.get("parameters"), counts)
                    fix_request_body(op_dict.get("requestBody"), counts)

    return counts


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python fix_openapi_schema.py <input.json> <output.json>")
        sys.exit(2)

    input_path, output_path = sys.argv[1], sys.argv[2]

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    counts = fix(data)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")

    print(f"Wrote {output_path}")
    print(f"  path parameters de-nullabled:   {counts['path_params']}")
    print(f"  object schemas de-nullabled:     {counts['objects']}")
    print(f"  scalar request bodies fixed:     {counts['scalar_bodies']}")


if __name__ == "__main__":
    main()
