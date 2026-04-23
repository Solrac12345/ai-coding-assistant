from __future__ import annotations

import textwrap
from typing import Any

from src.logging.logger import Logger
from src.state.state import State


class DocAgent:
    """Generate human-readable documentation from state."""

    def _format_section(self, title: str, body: str | None) -> str:
        if not body:
            return ""
        return f"### {title}\n{body.strip()}\n"

    def _build_summary(self, state: State) -> str:
        lines: list[str] = []

        if state.language:
            lines.append(f"- **Language:** {state.language}")
        if state.complexity:
            lines.append(f"- **Estimated complexity:** {state.complexity}")
        if state.tags:
            tags = ", ".join(state.tags)
            lines.append(f"- **Tags:** {tags}")

        analysis_meta: dict[str, Any] = state.metadata.get("analysis", {})
        top_names = analysis_meta.get("top_names") or []
        node_count = analysis_meta.get("node_count")

        if top_names:
            lines.append(f"- **Key identifiers:** {', '.join(top_names)}")
        if node_count is not None:
            lines.append(f"- **AST node count:** {node_count}")

        return "\n".join(lines)

    def run(self, state: State) -> State:
        Logger.info("Generating documentation", agent="DocAgent")

        original_preview = textwrap.shorten(
            state.code.replace("\n", " "), width=120, placeholder="..."
        )

        summary = self._build_summary(state)

        parts: list[str] = []

        parts.append("# AI Coding Assistant — Documentation\n")

        parts.append("## Overview\n")
        parts.append(f"Original code preview:\n```python\n{original_preview}\n```\n")

        if summary:
            parts.append("## Summary\n")
            parts.append(summary + "\n")

        if state.analysis:
            parts.append(self._format_section("Detailed Analysis", state.analysis))

        if state.optimized_code:
            parts.append("## Optimized Code\n")
            parts.append("```python\n" + state.optimized_code.strip() + "\n```\n")

        doc = "\n".join(p for p in parts if p.strip())

        state.documentation = doc
        Logger.info("Documentation generated", agent="DocAgent")
        return state
