from src.state.state import State


class Supervisor:
    """
    EN:
        The Supervisor orchestrates the entire workflow of the AI Coding Assistant.
        It receives the initial State, executes each agent in sequence, and returns
        the enriched final State. This class ensures a clean, predictable, and
        secure execution flow.

    FR:
        Le Superviseur orchestre tout le flux de travail de l'assistant IA.
        Il reçoit l'état initial, exécute chaque agent en séquence et renvoie
        l'état final enrichi. Cette classe garantit un flux d'exécution propre,
        prévisible et sécurisé.
    """

    def __init__(self, analyzer_cls: type, optimizer_cls: type, doc_agent_cls: type):
        """
        EN:
            The Supervisor receives the agent classes (not instances) so it can
            instantiate them cleanly. This improves testability and scalability.

        FR:
            Le Superviseur reçoit les classes des agents (pas les instances)
            afin de pouvoir les instancier proprement. Cela améliore la
            testabilité et la scalabilité.
        """
        self.analyzer_cls = analyzer_cls
        self.optimizer_cls = optimizer_cls
        self.doc_agent_cls = doc_agent_cls

    def run(self, state: State) -> State:
        """
        EN:
            Executes the full workflow:
                1. AnalyzerAgent → produces analysis
                2. OptimizerAgent → produces optimized code
                3. DocAgent → produces documentation

            Each agent receives the current State and returns an updated State.

        FR:
            Exécute le flux complet :
                1. AnalyzerAgent → produit l'analyse
                2. OptimizerAgent → produit le code optimisé
                3. DocAgent → produit la documentation

            Chaque agent reçoit l'état actuel et renvoie un état mis à jour.
        """

        # --- Step 1: Analyzer ---
        analyzer = self.analyzer_cls()
        state = analyzer.run(state)

        # --- Step 2: Optimizer ---
        optimizer = self.optimizer_cls()
        state = optimizer.run(state)

        # --- Step 3: Documentation Agent ---
        doc_agent = self.doc_agent_cls()
        state = doc_agent.run(state)

        return state
