from src.logging.logger import Logger
from src.state.state import State


class OptimizerAgent:
    """
    EN:
        Optimizer agent that improves the input code.
    FR:
        Agent optimiseur qui améliore le code d'entrée.
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

        # Changed from state.code_input to state.code
        original_code = state.code
        Logger.info("Optimizing code", agent="OptimizerAgent")

        # Simple optimization: ensure code ends with newline
        if not original_code.endswith("\n"):
            state.optimized_code = original_code + "\n"
        else:
            state.optimized_code = original_code

        Logger.info(f"Optimized {len(original_code)} characters", agent="OptimizerAgent")
        return state
