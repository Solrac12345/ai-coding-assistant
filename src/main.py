from __future__ import annotations

from src.agents.analyzer import AnalyzerAgent
from src.agents.doc_agent import DocAgent
from src.agents.optimizer import OptimizerAgent
from src.state.state import State
from src.supervisor.controller import Supervisor


def read_multiline_input(prompt: str = "Enter your code (finish with empty line):") -> str:
    """
    Reads multi-line input from the user until a blank line is entered.
    This allows pasting full code blocks safely.
    """
    print(prompt)
    lines: list[str] = []

    while True:
        try:
            line = input()
        except EOFError:
            break

        if line.strip() == "":
            break

        lines.append(line)

    return "\n".join(lines)


def main() -> None:
    # Read multi-line code input
    code_input = read_multiline_input()

    # Initialize shared state
    state = State(code=code_input)

    # Build pipeline
    supervisor = Supervisor(
        [
            AnalyzerAgent(),
            OptimizerAgent(),
            DocAgent(),
        ]
    )

    # Run pipeline
    final_state = supervisor.run(state)

    # Display results
    print("\n=== Final Output ===")
    print("Analysis:", final_state.analysis)
    print("Optimized Code:", final_state.optimized_code)
    print("Documentation:", final_state.documentation)


if __name__ == "__main__":
    main()
