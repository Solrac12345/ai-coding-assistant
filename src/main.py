from src.agents.analyzer import AnalyzerAgent
from src.agents.doc_agent import DocAgent
from src.agents.optimizer import OptimizerAgent
from src.state.state import State
from src.supervisor.controller import Supervisor


def main() -> None:
    """Entry point for the AI Coding Assistant CLI."""
    code_input = input("Enter your code:\n")

    state = State(code=code_input)

    agents = [
        AnalyzerAgent(),
        OptimizerAgent(),
        DocAgent(),
    ]

    supervisor = Supervisor(agents)
    final_state = supervisor.run(state)

    print("\n=== Final Output ===")
    print("Analysis:", final_state.analysis)
    print("Optimized Code:", final_state.optimized_code)
    print("Documentation:", final_state.documentation)


if __name__ == "__main__":
    main()
