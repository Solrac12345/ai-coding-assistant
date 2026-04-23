from src.agents.analyzer import AnalyzerAgent
from src.agents.doc_agent import DocAgent
from src.agents.optimizer import OptimizerAgent
from src.state.state import State
from src.supervisor.controller import Supervisor


def test_supervisor_pipeline_runs():
    state = State(code="print('hello')")

    # Updated to match your new Supervisor(agents=[...]) signature
    supervisor = Supervisor(
        agents=[
            AnalyzerAgent(),
            OptimizerAgent(),
            DocAgent(),
        ]
    )

    final_state = supervisor.run(state)

    assert final_state.analysis is not None
    assert final_state.optimized_code is not None
    assert final_state.documentation is not None
