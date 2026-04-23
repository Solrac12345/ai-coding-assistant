from src.state.state import State


def test_state_initialization():
    # 1. Use 'code=' instead of 'code_input='
    state = State(code="print('hello')")

    # 2. Update assertions to match new defaults ("")
    assert state.code == "print('hello')"
    assert state.analysis == ""
    assert state.optimized_code == ""
    assert state.documentation == ""

    # 3. Check the new attributes
    assert state.language == "unknown"
    assert state.complexity == "unknown"
    assert isinstance(state.tags, list)
    assert isinstance(state.errors, list)
    assert isinstance(state.warnings, list)

    # 4. Check the dictionary attribute
    assert isinstance(state.metadata, dict)
