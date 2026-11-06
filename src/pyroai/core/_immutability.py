"""Internal recursive freeze/thaw helpers."""
from collections.abc import Mapping
from types import MappingProxyType

def freeze_value(value):
    """Copy supported values into recursively read-only containers."""
    if isinstance(value, Mapping):
        copied = {}
        for key, item in value.items():
            if not isinstance(key, str): raise TypeError("mapping keys must be strings")
            copied[key] = freeze_value(item)
        return MappingProxyType(copied)
    if isinstance(value, (list, tuple)): return tuple(freeze_value(v) for v in value)
    if isinstance(value, (set, frozenset)): return frozenset(freeze_value(v) for v in value)
    if value is None or isinstance(value, (str, bytes, int, float, complex, bool)): return value
    raise TypeError(f"unsupported value type: {type(value).__name__}")

def thaw_value(value):
    if isinstance(value, Mapping): return {k: thaw_value(v) for k, v in value.items()}
    if isinstance(value, tuple): return [thaw_value(v) for v in value]
    if isinstance(value, frozenset): return {thaw_value(v) for v in value}
    return value

def freeze_mapping(value, name):
    if not isinstance(value, Mapping): raise TypeError(f"{name} must be a mapping")
    return freeze_value(value)