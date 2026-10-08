"""Automated tests for the PC Troubleshooting Assistant.

Feeds scripted answers into pc_troubleshooting_assistant.py through
stdin and checks that each rule, the keyword matcher, invalid input,
and the quit options all behave as expected.

Run with: python test_assistant.py
"""

import os
import subprocess
import sys

SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "pc_troubleshooting_assistant.py")


def run(inputs: str) -> str:
    """Run the assistant with the given stdin and return its stdout."""
    result = subprocess.run(
        [sys.executable, SCRIPT],
        input=inputs,
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 0, f"script crashed:\n{result.stderr}"
    return result.stdout


def test_all_rules() -> None:
    """Menu choices 1-6 each produce their rule's recommendation."""
    expectations = {
        "1": "Recommendation (Power problem)",
        "2": "Recommendation (Internet connection)",
        "3": "Recommendation (Slow performance)",
        "4": "Recommendation (Application problem)",
        "5": "Recommendation (Pop-ups or security warnings)",
        "6": "Recommendation (No recognized problem)",
    }
    for choice, expected in expectations.items():
        # answer the follow-up with 'y', then decline another round
        output = run(f"{choice}\ny\nn\n")
        assert expected in output, f"rule {choice}: '{expected}' not found"
    print("PASS: all six rules return the expected recommendation")


def test_follow_up_answers() -> None:
    """Both yes and no follow-up answers tailor the recommendation."""
    yes_out = run("1\ny\nn\n")
    no_out = run("1\nn\nn\n")
    assert "Since something powers on" in yes_out, "yes follow-up missing"
    assert "no sign of power at all" in no_out, "no follow-up missing"
    assert "Since something powers on" not in no_out, "yes follow-up leaked into 'no'"
    print("PASS: follow-up answers tailor the recommendation both ways")


def test_keyword_matching() -> None:
    """Free-form descriptions are matched to the correct rule."""
    expectations = {
        "my computer won't turn on": "Recommendation (Power problem)",
        "the internet is down": "Recommendation (Internet connection)",
        "everything has gotten really slow": "Recommendation (Slow performance)",
        "my web browser app keeps crashing": "Recommendation (Application problem)",
        "i'm seeing weird pop-ups and warnings": "Recommendation (Pop-ups or security warnings)",
    }
    for description, expected in expectations.items():
        output = run(f"{description}\ny\nn\n")
        assert expected in output, f"'{description}' did not match: expected {expected}"
    print("PASS: keyword matching maps descriptions to the right rules")


def test_invalid_input_reprompts() -> None:
    """Unrecognized text does not trigger rule 6; the user is asked again."""
    output = run("banana\n\n")
    assert "didn't recognize" in output, "invalid input message missing"
    assert "No recognized problem" not in output, "invalid input wrongly hit rule 6"
    print("PASS: invalid input re-prompts instead of firing rule 6")


def test_quit_options() -> None:
    """Empty input and 'q' both exit cleanly."""
    for quit_key in ("", "q"):
        output = run(f"{quit_key}\n")
        assert "Goodbye" in output, f"quit via {quit_key!r} failed"
    print("PASS: empty input and 'q' both quit")


if __name__ == "__main__":
    test_all_rules()
    test_follow_up_answers()
    test_keyword_matching()
    test_invalid_input_reprompts()
    test_quit_options()
    print("\nAll tests passed.")
