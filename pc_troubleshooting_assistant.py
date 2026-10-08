"""PC Troubleshooting Assistant.

A rule-based system that asks the user about common computer problems
and provides troubleshooting recommendations based on their answers.

Rules are implemented with if-elif-else conditionals: each menu choice
matches one rule, and the final else handles the "no recognized problem"
rule.
"""

MENU = [
    ("1", "The computer does not turn on"),
    ("2", "Computer is on but cannot connect to the internet"),
    ("3", "The computer is running slowly"),
    ("4", "A specific application is not working correctly"),
    ("5", "Unusual pop-ups or security warnings"),
    ("6", "None of these / something else"),
]


def show_menu() -> None:
    """Display the list of possible problems to the user."""
    print("\n=== PC Troubleshooting Assistant ===")
    print("What problem are you experiencing? Enter the number of your choice:")
    for number, problem in MENU:
        print(f"  {number}. {problem}")


def get_recommendation(choice: str) -> str:
    """Apply the rules and return the recommendation for a menu choice.

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
    """
    if choice == "1":
        # Rule 1: Power problem -> check power cable, outlet, power button.
        return (
            "Recommendation (Power problem):\n"
            "  - Check that the power cable is firmly connected to the computer and the wall outlet.\n"
            "  - Test the outlet with another device (or try a different outlet).\n"
            "  - Make sure the power button is working (look for lights or fan noise)."
        )
    elif choice == "2":
        # Rule 2: Internet connection -> check network, restart router/modem, reconnect.
        return (
            "Recommendation (Internet connection):\n"
            "  - Check the network connection (Wi-Fi enabled or Ethernet cable plugged in).\n"
            "  - Restart the router/modem and wait for the lights to return to normal.\n"
            "  - Reconnect to your Wi-Fi network or try a different Ethernet port/cable."
        )
    elif choice == "3":
        # Rule 3: Slow performance -> close programs, check storage, restart.
        return (
            "Recommendation (Slow performance):\n"
            "  - Close unnecessary programs and startup items.\n"
            "  - Check available storage and free up space if the drive is nearly full.\n"
            "  - Restart the computer to clear memory and finish pending updates."
        )
    elif choice == "4":
        # Rule 4: Application problem -> restart app, check updates, restart PC.
        return (
            "Recommendation (Application problem):\n"
            "  - Restart the application completely (close all of its windows).\n"
            "  - Check for updates to the application and install any available version.\n"
            "  - Restart the computer and try the application again."
        )
    elif choice == "5":
        # Rule 5: Pop-ups/warnings -> antivirus scan, avoid unknown links/downloads.
        return (
            "Recommendation (Pop-ups or security warnings):\n"
            "  - Run a full antivirus/security scan and remove anything it finds.\n"
            "  - Avoid clicking unknown links or pop-ups.\n"
            "  - Do not download unfamiliar files or programs."
        )
    else:
        # Rule 6: No recognized problem (catch-all else) -> restart and update.
        return (
            "Recommendation (No recognized problem):\n"
            "  - Restart the computer.\n"
            "  - Check for operating system updates and install them.\n"
            "  - Check for driver updates (especially graphics and network drivers)."
        )


def main() -> None:
    """Run the assistant loop until the user chooses to quit."""
    print("Welcome to the PC Troubleshooting Assistant.")
    print("Answer with 1-6, or press Enter alone to quit.")

    while True:
        show_menu()
        choice = input("Your choice: ").strip().lower()

        # Allow the user to quit with an empty input or q/quit.
        if choice in ("", "q", "quit", "exit"):
            print("Goodbye! Stay trouble-free.")
            break

        # Rule-based decision-making: the if-elif-else chain in
        # get_recommendation() picks the output for the chosen rule.
        print(get_recommendation(choice))

        again = input("\nTroubleshoot another problem? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Goodbye! Stay trouble-free.")
            break


if __name__ == "__main__":
    main()
