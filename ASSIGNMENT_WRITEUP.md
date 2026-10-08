# PC Troubleshooting Assistant — Assignment Writeup

## Part 1 – Prompting the AI for Project Ideas

**Project ideas suggested by AI:**

- **PC Troubleshooting Assistant** — asks questions about symptoms such as no power, network problems, slow performance, or application errors, then recommends troubleshooting steps based on predefined rules.
- **Cybersecurity Incident Triage Assistant** — asks about symptoms such as suspicious login activity, malware alerts, or unusual network traffic and provides basic recommended actions based on predefined rules.
- **Vehicle Maintenance Troubleshooting Assistant** — asks about symptoms such as warning lights, noises, starting problems, or overheating and suggests possible causes/actions.

**Chosen idea: PC Troubleshooting Assistant**

I chose the PC Troubleshooting Assistant because it is something I am already somewhat familiar with and would be useful in a real-world situation. I also think it will work well as a rule-based system because different symptoms can be used as conditions to provide specific troubleshooting steps.

---

## Part 2 – Designing Your Rule-Based System

**System idea:** A rule-based assistant that asks the user about common computer problems and provides basic troubleshooting steps based on their answers.

**Rules and logic:**

1. **Power problem**
   - **IF** the computer does not turn on
   - **THEN** recommend checking that the power cable is connected, the outlet works, and the power button is functioning.
2. **Internet connection**
   - **IF** the computer is on but cannot connect to the internet
   - **THEN** recommend checking the network connection, restarting the router/modem, and reconnecting to Wi-Fi or Ethernet.
3. **Slow performance**
   - **IF** the computer is running slowly
   - **THEN** recommend closing unnecessary programs, checking available storage, and restarting the computer.
4. **Application problem**
   - **IF** a specific application is not working correctly
   - **THEN** recommend restarting the application, checking for updates, and restarting the computer.
5. **Unexpected pop-ups or warnings**
   - **IF** the user reports unusual pop-ups or security warnings
   - **THEN** recommend running an antivirus/security scan and avoiding clicking unknown links or downloading unfamiliar files.
6. **No recognized problem**
   - **IF** none of the above problems apply
   - **THEN** recommend restarting the computer and checking for operating system or driver updates.

**Logic:** The user picks a numbered problem from a menu using `input()`, or describes the problem in their own words. An if-elif-else chain matches the choice or keywords to the corresponding rule and prints that rule's recommendation. Unrecognized text does not match any rule, so the user is asked to try again instead of receiving wrong advice; the final `else` branch in the rule engine implements Rule 6 for anything that resolves to "none of these." A loop lets the user troubleshoot multiple problems before quitting.

---

## Part 3 – Coding Your Rule-Based System

**Repository:** https://github.com/JPDeuce/PC_Troubleshooting_Assistant.git

**Inputs and Results:**

1. **Input:** `Can't access the internet`

   **Result:**
   ```
   Can other devices (like a phone) connect to the same network? (y/n) n

   Recommendation (Internet connection):
     - Check the network connection (Wi-Fi enabled or Ethernet cable plugged in).
     - Restart the router/modem and wait for the lights to return to normal.
     - Reconnect to your Wi-Fi network or try a different Ethernet port/cable.
     Follow-up: If no devices can connect, the problem is the router/modem or the internet service itself.
   ```

2. **Input:** `Email isn't working`

   **Result:**
   ```
   Sorry, I didn't recognize that problem. Pick a number 1-6 or try describing it differently.
   ```

   **Second attempt input:** `Email application isn't working`

   **Result:**
   ```
   Did the problem start after an update or other recent change? (y/n) y

   Recommendation (Application problem):
     - Restart the application completely (close all of its windows).
     - Check for updates to the application and install any available version.
     - Restart the computer and try the application again.
     Follow-up: A recent update likely caused it — reinstall the app or check the update history for a rollback option.
   ```

3. **Input:** `Computer running slow`

   **Result:**
   ```
   Does the slowdown happen even after a restart? (y/n) n

   Recommendation (Slow performance):
     - Close unnecessary programs and startup items.
     - Check available storage and free up space if the drive is nearly full.
     - Restart the computer to clear memory and finish pending updates.
     Follow-up: If a restart fixes it, look for a program that re-opens itself at startup.
   ```

   **Follow-up (if `y` is selected instead of `n` above):**
   ```
   Follow-up: Still slow after a restart — check Task Manager for heavy consumers and consider a drive or hardware check.
   ```

---

## Part 4 – Reflection and Submission

For being a very basic troubleshooting assistant, I think my rule-based system works pretty well, at least as a first version. The system lets the user either select a problem from a numbered list or describe the problem in their own words. The program uses keywords to determine which rule applies and then provides a troubleshooting recommendation. It also asks a follow-up question for each problem to provide a little more specific advice. It could use more keywords, more follow-up questions, and more testing, but I am happy with the current state of it.

I didn't really encounter too many major issues while prompting the AI to assist with the design and code. The first suggestions were pretty good to start with, and I did ask it to expand on them a little. When it came to designing and coding, things worked pretty well from the start. I did end up working with the AI to expand beyond just putting in the number inputs and adding keyword matching so users could describe their problems instead. After a few rounds of testing, I was able to add a few more keywords and results just to cover some more common issues.

One challenge I noticed was that keyword matching is not perfect. For example, when I entered "Email isn't working," the program did not recognize it because email was not one of the keywords. Changing the description to "Email application isn't working" allowed it to match the application rule. This showed me that a rule-based system can work well for common problems, but it depends heavily on how the rules and keywords are defined. Testing different inputs helped me find these limitations and improve the system without making the rules overly complicated.

This also showed me one of the differences between a rule-based system and modern machine learning. A rule-based system only knows the conditions and responses that are programmed into it, while a machine learning system could potentially recognize patterns from a much larger amount of data.
