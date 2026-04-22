from src.state.state import State
from src.agents.analyzer import AnalyzerAgent
from src.agents.optimizer import OptimizerAgent
from src.agents.doc_agent import DocAgent


def test_analyzer_agent():
    state = State(code_input="print('hello')")
    agent = AnalyzerAgent()
    new_state = agent.run(state)
    assert new_state.analysis is not None


def test_optimizer_agent():
    state = State(code_input="print('hello')")
    agent = OptimizerAgent()
    new_state = agent.run(state)
    assert new_state.optimized_code is not None


def test_doc_agent():
    state = State(code_input="print('hello')")
    state.analysis = "Test analysis"
    state.optimized_code = "print('hello')\n"
    agent = DocAgent()
    new_state = agent.run(state)
    assert new_state.documentation is not None
