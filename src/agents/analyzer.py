from src.state.state import State


class AnalyzerAgent:
    """
    EN:
        AnalyzerAgent is responsible for inspecting the input code and producing
        a human-readable analysis. In Phase 2, this is a simple static analysis
        placeholder that can be extended later (e.g., with LLMs or advanced tools).

    FR:
        AnalyzerAgent est responsable d'inspecter le code d'entrée et de produire
        une analyse lisible. En Phase 2, il s'agit d'un analyseur statique simple
        qui pourra être étendu plus tard (par exemple avec des LLMs ou des outils avancés).
    """

    def run(self, state: State) -> State:
        """
        EN:
            Main entry point for the AnalyzerAgent.
            It reads the raw code from the state and updates the `analysis` field.

        FR:
            Point d'entrée principal pour l'AnalyzerAgent.
            Il lit le code brut depuis l'état et met à jour le champ `analysis`.
        """

        code = state.code_input

        # EN: Very simple placeholder analysis for Phase 2.
        # FR: Analyse très simple de base pour la Phase 2.
        issues = []

        if not code.strip():
            issues.append("Code appears to be empty.")
        if "print(" in code:
            issues.append("Uses print statements (consider using logging in larger projects).")
        if "TODO" in code:
            issues.append("Contains TODO comments (incomplete work indicated).")

        if issues:
            analysis_text = "Basic static analysis:\n- " + "\n- ".join(issues)
        else:
            analysis_text = "Basic static analysis: no obvious issues detected."

        state.analysis = analysis_text
        return state
