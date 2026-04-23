from __future__ import annotations

import ast
from collections import Counter

from src.logging.logger import Logger
from src.state.state import State


class AnalyzerAgent:
    """Analyze the input code and enrich the shared state."""

    def _detect_language(self, code: str) -> str:
        """Very simple heuristic language detection."""
        if "def " in code or "import " in code:
            return "python"
        if "#include" in code or "std::" in code:
            return "cpp"
        if "public static void main" in code:
            return "java"
        if "function " in code and "console.log" in code:
            return "javascript"
        return "unknown"

    def _estimate_complexity(self, tree: ast.AST) -> str:
        """Rough complexity bucket based on branching nodes."""
        branches = sum(
            isinstance(node, (ast.If, ast.For, ast.While, ast.Try, ast.With, ast.Match))
            for node in ast.walk(tree)
        )

        if branches == 0:
            return "trivial"
        if branches <= 3:
            return "simple"
        if branches <= 8:
            return "moderate"
        return "complex"

    def _extract_tags(self, tree: ast.AST) -> list[str]:
        """Infer simple tags from AST structure."""
        tags: list[str] = []

        has_functions = any(isinstance(n, ast.FunctionDef) for n in ast.walk(tree))
        has_classes = any(isinstance(n, ast.ClassDef) for n in ast.walk(tree))
        has_loops = any(isinstance(n, (ast.For, ast.While)) for n in ast.walk(tree))
        has_io = any(
            isinstance(n, ast.Call) and getattr(n.func, "id", "") == "print" for n in ast.walk(tree)
        )

        if has_functions:
            tags.append("functions")
        if has_classes:
            tags.append("classes")
        if has_loops:
            tags.append("loops")
        if has_io:
            tags.append("io")

        return tags

    def _summarize_top_names(self, tree: ast.AST) -> list[str]:
        """Return most common identifier names (variables, functions, classes)."""
        names: Counter[str] = Counter()

        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                names[node.id] += 1
            elif isinstance(node, ast.FunctionDef):
                names[node.name] += 1
            elif isinstance(node, ast.ClassDef):
                names[node.name] += 1

        return [name for name, _count in names.most_common(5)]

    def run(self, state: State) -> State:
        Logger.info("Analyzing code", agent="AnalyzerAgent")

        code = state.code
        language = self._detect_language(code)
        state.language = language

        try:
            tree = ast.parse(code)
        except SyntaxError as exc:
            msg = f"Syntax error during analysis: {exc}"
            Logger.error(msg, agent="AnalyzerAgent")
            state.errors.append(msg)
            state.analysis = "Syntax error: unable to analyze code."
            state.complexity = "unknown"
            return state

        complexity = self._estimate_complexity(tree)
        tags = self._extract_tags(tree)
        top_names = self._summarize_top_names(tree)

        state.complexity = complexity
        state.tags = tags

        state.metadata.setdefault("analysis", {})
        state.metadata["analysis"].update(
            {
                "top_names": top_names,
                "node_count": sum(1 for _ in ast.walk(tree)),
            }
        )

        # Human-readable analysis summary
        lines: list[str] = []
        lines.append(f"Detected language: {language}")
        lines.append(f"Estimated complexity: {complexity}")
        if tags:
            lines.append(f"Inferred tags: {', '.join(tags)}")
        if top_names:
            lines.append(f"Most common identifiers: {', '.join(top_names)}")

        state.analysis = "\n".join(lines)

        Logger.info("Completed analysis", agent="AnalyzerAgent")
        return state
