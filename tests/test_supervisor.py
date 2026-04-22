from src.state.state import State
from src.supervisor.controller import Supervisor
from src.agents.analyzer import AnalyzerAgent
from src.agents.optimizer import OptimizerAgent
from src.agents.doc_agent import DocAgent


def test_supervisor_pipeline_runs():
    state = State(code_input="print('hello')")
    supervisor = Supervisor(
        analyzer_cls=AnalyzerAgent,
        optimizer_cls=OptimizerAgent,
        doc_agent_cls=DocAgent,
    )

    final_state = supervisor.run(state)

    assert final_state.analysis is not None
    assert final_state.optimized_code is not None
    assert final_state.documentation is not None
