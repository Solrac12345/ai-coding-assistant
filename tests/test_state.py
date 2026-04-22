from src.state.state import State


def test_state_initialization():
    state = State(code_input="print('hello')")
    assert state.code_input == "print('hello')"
    assert state.analysis is None
    assert state.optimized_code is None
    assert state.documentation is None
    assert isinstance(state.metadata, dict)
