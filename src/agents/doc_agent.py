from src.state.state import State


class DocAgent:
    """
    EN:
        DocAgent is responsible for generating human-readable documentation
        based on the input code and the analysis produced by previous agents.
        In Phase 2, it creates a simple textual summary.

    FR:
        DocAgent est responsable de générer une documentation lisible
        à partir du code d'entrée et de l'analyse produite par les agents précédents.
        En Phase 2, il crée un résumé textuel simple.
    """

    def run(self, state: State) -> State:
        """
        EN:
            Main entry point for the DocAgent.
            It reads `code`, `analysis`, and `optimized_code` from the state
            and produces a short documentation block.

        FR:
            Point d'entrée principal pour le DocAgent.
            Il lit `code`, `analysis` et `optimized_code` depuis l'état
            et produit un court bloc de documentation.
        """

        # FIX: Changed state.code_input to state.code
        code_preview = state.code.strip()
        if len(code_preview) > 200:
            code_preview = code_preview[:200] + " ..."

        analysis = state.analysis or "No analysis available."
        optimized_present = bool(state.optimized_code)

        doc_lines = [
            "AI Coding Assistant — Documentation Summary",
            "",
            "Original code preview:",
            code_preview or "<empty code>",
            "",
            "Analysis:",
            analysis,
            "",
            "Optimized code generated: " + ("yes" if optimized_present else "no"),
        ]

        state.documentation = "\n".join(doc_lines)
        return state
