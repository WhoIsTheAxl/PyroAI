"""Immutable action descriptors."""
from dataclasses import dataclass, field
from typing import Any, Mapping
from ._immutability import freeze_mapping, thaw_value

@dataclass(frozen=True, slots=True)
class Action:
    """Describe an intended operation; execution belongs to the environment."""
    type: str
    parameters: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not isinstance(self.type, str) or not self.type.strip(): raise ValueError("action type must be a non-empty string")
        object.__setattr__(self, "parameters", freeze_mapping(self.parameters, "parameters"))

    def mutable_copy(self):
        """Return detached, mutable action parameters."""
        return thaw_value(self.parameters)