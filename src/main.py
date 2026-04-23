from src.agents.analyzer import AnalyzerAgent
from src.agents.doc_agent import DocAgent
from src.agents.optimizer import OptimizerAgent
from src.state.state import State
from src.supervisor.controller import Supervisor


def main():
    """
    EN:
        Entry point of the AI Coding Assistant (Phase 2).
        This function builds an initial State with sample code, runs the
        Supervisor pipeline (Analyzer → Optimizer → DocAgent), and prints
        the results to the console.

    FR:
        Point d'entrée de l'assistant IA (Phase 2).
        Cette fonction construit un état initial avec du code d'exemple,
        exécute le pipeline du Superviseur (Analyzer → Optimizer → DocAgent)
        et affiche les résultats dans la console.
    """

    sample_code = """
def add(a, b):
    # TODO: handle type checking
    print(a + b)
"""

    # EN: Build initial state.
    # FR: Construire l'état initial.
    state = State(code_input=sample_code)

    # EN: Create the Supervisor with the three agents.
    # FR: Créer le Superviseur avec les trois agents.
    supervisor = Supervisor(
        analyzer_cls=AnalyzerAgent,
        optimizer_cls=OptimizerAgent,
        doc_agent_cls=DocAgent,
    )

    # EN: Run the full pipeline.
    # FR: Exécuter le pipeline complet.
    final_state = supervisor.run(state)

    # EN: Display results.
    # FR: Afficher les résultats.
    print("=== ANALYSIS ===")
    print(final_state.analysis or "<no analysis>")

    print("\n=== OPTIMIZED CODE ===")
    print(final_state.optimized_code or "<no optimized code>")

    print("\n=== DOCUMENTATION ===")
    print(final_state.documentation or "<no documentation>")


if __name__ == "__main__":
    main()
