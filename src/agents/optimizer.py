from __future__ import annotations

import ast
import textwrap

from src.logging.logger import Logger
from src.state.state import State


class _FStringRewriter(ast.NodeTransformer):
    """Rewrite simple string concatenations into f-strings."""

    def visit_BinOp(self, node: ast.BinOp) -> ast.AST:
        self.generic_visit(node)

        if not isinstance(node.op, ast.Add):
            return node

        # Only handle: "literal" + name  or  name + "literal"
        left, right = node.left, node.right

        if isinstance(left, ast.Constant) and isinstance(right, ast.Name):
            if isinstance(left.value, str):
                return ast.JoinedStr(
                    values=[
                        ast.Constant(value=left.value.replace("{}", "{{}}")),
                        ast.FormattedValue(value=right, conversion=-1),
                    ]
                )

        if isinstance(left, ast.Name) and isinstance(right, ast.Constant):
            if isinstance(right.value, str):
                return ast.JoinedStr(
                    values=[
                        ast.FormattedValue(value=left, conversion=-1),
                        ast.Constant(value=right.value.replace("{}", "{{}}")),
                    ]
                )

        return node


class OptimizerAgent:
    """Optimize code formatting and simple patterns."""

    def run(self, state: State) -> State:
        Logger.info("Optimizing code", agent="OptimizerAgent")

        code = state.code

        # 1) Normalize indentation / trailing spaces
        normalized = textwrap.dedent(code).strip() + "\n"

        try:
            tree = ast.parse(normalized)
        except SyntaxError as exc:
            msg = f"Syntax error during optimization: {exc}"
            Logger.error(msg, agent="OptimizerAgent")
            state.errors.append(msg)
            # Fallback: keep original code
            state.optimized_code = code
            return state

        # 2) Apply simple AST-based optimizations (f-strings)
        tree = _FStringRewriter().visit(tree)
        ast.fix_missing_locations(tree)

        # 3) Convert back to source
        try:
            optimized = ast.unparse(tree)
        except Exception as exc:  # pragma: no cover (very rare)
            msg = f"Failed to unparse optimized code: {exc}"
            Logger.error(msg, agent="OptimizerAgent")
            state.errors.append(msg)
            state.optimized_code = normalized
            return state

        state.optimized_code = optimized.strip() + "\n"

        Logger.info(
            f"Optimized {len(code)} -> {len(state.optimized_code)} characters",
            agent="OptimizerAgent",
        )
        return state
