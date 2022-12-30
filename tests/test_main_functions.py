from main import input_number

from _pytest.monkeypatch import MonkeyPatch

# ``monkeypatch.setattr`` works by (temporarily) changing the object that a name points to with another one.
def test_input_number(monkeypatch: MonkeyPatch):
    monkeypatch.setattr("builtins.input", lambda _: 123)
    value = input_number("message")

    assert value == 123