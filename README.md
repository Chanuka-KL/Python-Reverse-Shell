# Reverse Shell in Python 🐍

This project demonstrates a simple reverse shell setup using Python, allowing an attacker to execute shell commands on a remote victim machine.

## Project Structure 📕

- **attacker.py**: The attacker's script to listen for a connection and send commands.
- **victim.py**: The victim's script that connects back to the attacker and executes commands.

## How to Use 🧾

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Chanuka-Kl/Python-Reverse-Shell.git
    cd Python-Reverse-Shell
    ```

2. **Configure the Attacker's Script**:
    - Edit `attacker.py` and set the `attacker_ip` to your public IP address.
  
3. **Configure the Victim's Script**:
    - Edit `victim.py` and set the `attacker_ip` to your public IP address.

4. **Run the Attacker's Script**:
    On your machine (attacker):
    ```bash
    python3 attacker.py
    ```

5. **Run the Victim's Script**:
    On the victim's machine:
    ```bash
    python3 victim.py
    ```

6. **Send Commands**:
    Once the victim is connected, you can execute commands from the attacker's machine. To exit, type `exit`.

## Security Warning ⚠️

This tool is for educational purposes only. Do not use it on machines or networks you do not own or have explicit permission to test. Misuse of this tool could result in legal consequences.

## License

This project is licensed under the MIT License.

---

_Developed by [Chanuka-Kl](https://github.com/Chanuka-Kl)_
