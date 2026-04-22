from src.state.state import State


class OptimizerAgent:
    """
    EN:
        OptimizerAgent is responsible for improving or refactoring the input code.
        In Phase 2, this implementation is intentionally simple and deterministic.
        It prepares the structure for later integration with formatting tools
        (e.g., Black) and more advanced optimization strategies.

    FR:
        OptimizerAgent est responsable d'améliorer ou de refactoriser le code d'entrée.
        En Phase 2, cette implémentation est volontairement simple et déterministe.
        Elle prépare la structure pour une intégration ultérieure avec des outils
        de formatage (par ex. Black) et des stratégies d'optimisation plus avancées.
    """

    def run(self, state: State) -> State:
        """
        EN:
            Main entry point for the OptimizerAgent.
            It reads the raw code and the analysis, then produces a slightly
            improved version of the code. For Phase 2, we only apply a minimal,
            safe transformation.

        FR:
            Point d'entrée principal pour l'OptimizerAgent.
            Il lit le code brut et l'analyse, puis produit une version légèrement
            améliorée du code. Pour la Phase 2, nous appliquons seulement une
            transformation minimale et sûre.
        """

        original_code = state.code_input

        # EN:
        #   Phase 2 placeholder:
        #   - Strip trailing whitespace
        #   - Ensure file ends with a newline
        #
        # FR:
        #   Bouchon pour la Phase 2 :
        #   - Supprimer les espaces en fin de ligne
        #   - S'assurer que le fichier se termine par une nouvelle ligne

        lines = original_code.splitlines()
        cleaned_lines = [line.rstrip() for line in lines]
        optimized = "\n".join(cleaned_lines)

        if not optimized.endswith("\n") and optimized != "":
            optimized += "\n"

        state.optimized_code = optimized or original_code
        return state
