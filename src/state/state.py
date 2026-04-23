from dataclasses import dataclass, field
from typing import Any


@dataclass
class State:
    """Shared state passed between agents."""

    code: str = ""
    analysis: str = ""
    optimized_code: str = ""
    documentation: str = ""

    # Phase 3 metadata
    language: str = "unknown"
    complexity: str = "unknown"
    tags: list[str] = field(default_factory=list)

    # Error handling
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    # Extra metadata
    metadata: dict[str, Any] = field(default_factory=dict)
