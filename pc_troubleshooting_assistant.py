"""PC Troubleshooting Assistant.

A rule-based system that asks the user about common computer problems
and provides troubleshooting recommendations based on their answers.

Rules are implemented with if-elif-else conditionals:
- match_keywords() turns a typed description into a rule number by
  checking keyword groups in order (first match wins).
- get_recommendation() selects the recommendation for each rule and
  refines it with the answer to a follow-up question.
- The final else branch implements the "no recognized problem" rule.
"""

from typing import Optional

# Rules 1-6; these are the only valid menu choices.
VALID_CHOICES = ("1", "2", "3", "4", "5", "6")

MENU = [
    ("1", "The computer does not turn on"),
    ("2", "Computer is on but cannot connect to the internet"),
    ("3", "The computer is running slowly"),
    ("4", "A specific application is not working correctly"),
    ("5", "Unusual pop-ups or security warnings"),
    ("6", "None of these / something else"),
]

# One clarifying yes/no question per rule, asked before advising.
# The answer is passed to get_recommendation() to tailor the output.
FOLLOW_UP = {
    "1": "Do any lights come on or fans spin when you press the power button? (y/n)",
    "2": "Can other devices (like a phone) connect to the same network? (y/n)",
    "3": "Does the slowdown happen even after a restart? (y/n)",
    "4": "Did the problem start after an update or other recent change? (y/n)",
    "5": "Have you clicked a link or downloaded anything unfamiliar recently? (y/n)",
    "6": "Have you already tried restarting the computer? (y/n)",
}


def show_menu() -> None:
    """Display the list of possible problems to the user."""
    print("\n=== PC Troubleshooting Assistant ===")
    print("What problem are you experiencing? Enter the number,")
    print("or just describe the problem in your own words:")
    for number, problem in MENU:
        print(f"  {number}. {problem}")


def match_keywords(text: str) -> Optional[str]:
    """Map a free-form problem description to a rule number.

    Each if-elif branch checks the keywords associated with one rule.
    The first keyword group that appears in the text wins, so more
    specific descriptions are matched before generic ones. Returns None
    when no rule's keywords appear (i.e., no recognized problem).
    """
    text = text.lower()

    # Rule 1 keywords: the machine is dead / won't turn on.
    if any(word in text for word in ("power", "turn on", "turns on", "won't start",
                                     "wont start", "doesn't start", "does not start",
                                     "dead", "no lights")):
        return "1"
    # Rule 2 keywords: connectivity is down.
    elif any(word in text for word in ("internet", "wifi", "wi-fi", "network",
                                       "online", "ethernet", "connection")):
        return "2"
    # Rule 3 keywords: the machine is sluggish or freezing.
    elif any(word in text for word in ("slow", "sluggish", "lag", "freeze",
                                       "freezing", "frozen")):
        return "3"
    # Rule 4 keywords: a single app/program is misbehaving.
    elif any(word in text for word in ("app", "application", "program",
                                       "software", "crash", "crashing")):
        return "4"
    # Rule 5 keywords: malware-style symptoms.
    elif any(word in text for word in ("pop-up", "popup", "pop up", "virus",
                                       "malware", "warning", "scam", "security")):
        return "5"
    # No keywords matched: no rule applies, so the caller will treat
    # this as invalid input and ask again.
    else:
        return None


def get_recommendation(choice: str, answer: str) -> str:
    """Apply the rules and return the recommendation for a rule number.

    Each rule is one branch of the if-elif-else chain:

    Rule 1 - Power problem: the computer does not turn on, so the advice
             focuses on the physical power supply (cable, outlet, button).
    Rule 2 - Internet connection: the computer is on but offline, so the
             advice covers the network path (connection, router, Wi-Fi).
    Rule 3 - Slow performance: the advice targets resource hogs
             (background programs, full storage, a reboot).
    Rule 4 - Application problem: only one app is affected, so the advice
             starts with that app (restart, updates) before a full reboot.
    Rule 5 - Pop-ups/warnings: likely malware or unsafe browsing habits,
             so the advice is a security scan plus safe-browsing habits.
    Rule 6 - No recognized problem (the final else): a generic recovery
             step of restarting and updating the OS/drivers.

    The follow-up answer (y/n) is used to append one extra line that
    narrows the advice for that specific situation.
    """
    yes = answer in ("y", "yes")

    if choice == "1":
        # Rule 1: Power problem -> check power cable, outlet, power button.
        rec = (
            "Recommendation (Power problem):\n"
            "  - Check that the power cable is firmly connected to the computer and the wall outlet.\n"
            "  - Test the outlet with another device (or try a different outlet).\n"
            "  - Make sure the power button is working (look for lights or fan noise)."
        )
        # Follow-up: any lights/fans mean part of the PC is receiving power.
        if yes:
            rec += ("\n  Follow-up: Since something powers on, check the monitor, "
                    "its video cable, and the outlet switch next.")
        else:
            rec += ("\n  Follow-up: With no sign of power at all, focus on the cable "
                    "and outlet first — the PSU or power button may have failed.")
    elif choice == "2":
        # Rule 2: Internet connection -> check network, restart router/modem, reconnect.
        rec = (
            "Recommendation (Internet connection):\n"
            "  - Check the network connection (Wi-Fi enabled or Ethernet cable plugged in).\n"
            "  - Restart the router/modem and wait for the lights to return to normal.\n"
            "  - Reconnect to your Wi-Fi network or try a different Ethernet port/cable."
        )
        # Follow-up: other devices working isolates the fault to this PC.
        if yes:
            rec += ("\n  Follow-up: Other devices connect fine, so the router is OK — "
                    "check this PC's Wi-Fi adapter and network drivers.")
        else:
            rec += ("\n  Follow-up: If no devices can connect, the problem is the "
                    "router/modem or the internet service itself.")
    elif choice == "3":
        # Rule 3: Slow performance -> close programs, check storage, restart.
        rec = (
            "Recommendation (Slow performance):\n"
            "  - Close unnecessary programs and startup items.\n"
            "  - Check available storage and free up space if the drive is nearly full.\n"
            "  - Restart the computer to clear memory and finish pending updates."
        )
        # Follow-up: still slow after reboot points beyond simple clutter.
        if yes:
            rec += ("\n  Follow-up: Still slow after a restart — check Task Manager "
                    "for heavy consumers and consider a drive or hardware check.")
        else:
            rec += ("\n  Follow-up: If a restart fixes it, look for a program that "
                    "re-opens itself at startup.")
    elif choice == "4":
        # Rule 4: Application problem -> restart app, check updates, restart PC.
        rec = (
            "Recommendation (Application problem):\n"
            "  - Restart the application completely (close all of its windows).\n"
            "  - Check for updates to the application and install any available version.\n"
            "  - Restart the computer and try the application again."
        )
        # Follow-up: started after a change means the change is the likely cause.
        if yes:
            rec += ("\n  Follow-up: A recent update likely caused it — reinstall the "
                    "app or check the update history for a rollback option.")
        else:
            rec += ("\n  Follow-up: With no recent change, a simple restart of the "
                    "app usually clears the problem.")
    elif choice == "5":
        # Rule 5: Pop-ups/warnings -> antivirus scan, avoid unknown links/downloads.
        rec = (
            "Recommendation (Pop-ups or security warnings):\n"
            "  - Run a full antivirus/security scan and remove anything it finds.\n"
            "  - Avoid clicking unknown links or pop-ups.\n"
            "  - Do not download unfamiliar files or programs."
        )
        # Follow-up: a recent click/download raises the chance of infection.
        if yes:
            rec += ("\n  Follow-up: Run the scan now and avoid entering passwords "
                    "until it finishes — a recent click may have installed malware.")
        else:
            rec += ("\n  Follow-up: Pop-ups without a recent click can come from "
                    "the browser — check for unwanted extensions and reset settings.")
    else:
        # Rule 6: No recognized problem (catch-all else) -> restart and update.
        rec = (
            "Recommendation (No recognized problem):\n"
            "  - Restart the computer.\n"
            "  - Check for operating system updates and install them.\n"
            "  - Check for driver updates (especially graphics and network drivers)."
        )
        # Follow-up: order the steps depending on whether a restart was tried.
        if yes:
            rec += ("\n  Follow-up: Since you already restarted, go straight to the "
                    "OS and driver update steps.")
        else:
            rec += ("\n  Follow-up: Start with the restart — it resolves many "
                    "temporary glitches on its own.")

    return rec


def main() -> None:
    """Run the assistant loop until the user chooses to quit."""
    print("Welcome to the PC Troubleshooting Assistant.")
    print("Answer with 1-6, describe the problem, or press Enter alone to quit.")

    while True:
        show_menu()
        raw = input("Your choice: ").strip().lower()

        # Allow the user to quit with an empty input or q/quit/exit.
        if raw in ("", "q", "quit", "exit"):
            print("Goodbye! Stay trouble-free.")
            break

        # Resolve the input to a rule number: direct menu choice first,
        # otherwise keyword matching on the typed description.
        if raw in VALID_CHOICES:
            choice = raw
        else:
            choice = match_keywords(raw)
            if choice is None:
                # Not a menu number and no rule's keywords matched, so
                # ask again instead of guessing a rule.
                print("Sorry, I didn't recognize that problem. "
                      "Pick a number 1-6 or try describing it differently.")
                continue

        # Ask the clarifying question for the matched rule, then apply
        # the if-elif-else chain in get_recommendation().
        answer = input(FOLLOW_UP[choice] + " ").strip().lower()
        print(get_recommendation(choice, answer))

        again = input("\nTroubleshoot another problem? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Goodbye! Stay trouble-free.")
            break


if __name__ == "__main__":
    main()
