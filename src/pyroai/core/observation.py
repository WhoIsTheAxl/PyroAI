"""Read-only snapshots of agent-visible environment information."""
from dataclasses import dataclass, field
from typing import Any, Mapping
from ._immutability import freeze_mapping, thaw_value

@dataclass(frozen=True, slots=True)
class Observation:
    """An immutable snapshot; never a reference to environment internals."""
    data: Mapping[str, Any] = field(default_factory=dict)
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        object.__setattr__(self, "data", freeze_mapping(self.data, "data"))
        object.__setattr__(self, "metadata", freeze_mapping(self.metadata, "metadata"))

    def mutable_copy(self):
        """Return a detached mutable copy of observation data."""
        return thaw_value(self.data)