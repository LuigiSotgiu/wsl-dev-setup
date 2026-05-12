# The Ultimate Windows Python Development Setup: WSL, VS Code, and `uv`

Welcome! If you are reading this, you are about to set up a professional, modern, and lightning-fast Python development environment on your Windows machine. 

Whether you are a seasoned developer or writing your first line of Python code, setting up your environment is often the most frustrating part of a project. "It works on my machine" is a common nightmare. This Zero-to-Hero guide solves that problem permanently.

## 🌟 Why this specific setup?

In the past, developers had to choose: use Windows and fight with incompatible tools, or wipe their computer and install Linux. Later, tools like Anaconda (Conda) became popular, but they were incredibly heavy, slow, and complex. 

Today, we have the ultimate stack:
1. **WSL (Windows Subsystem for Linux):** You keep using Windows (with all your familiar apps), but you get a real, native Linux engine running in the background. Since 90% of the world's code and servers run on Linux, you are now developing in the native language of the internet, without sacrificing Windows.
   *A Note on Native Linux: While this setup allows you to keep using Windows hassle-free, running Linux natively remains the absolute best environment for programming. If you are motivated to make the full switch to Linux, I highly encourage it! Consider this WSL workflow the best possible alternative.*
2. **Visual Studio Code (VS Code):** The most popular editor in the world. We will connect it to WSL. The magic here is that the "UI" runs on Windows, but the "Brain" (the terminal, the code execution) runs inside Linux.
3. **uv:** This is the game-changer. Written in Rust, `uv` replaces `pip`, `virtualenv`, `conda`, and even Python installers. It is blazingly fast. It manages your project's dependencies and **automatically downloads the correct version of Python** for you. No more messing with system environment variables!
4. **Git:** The industry standard for version control. It acts as a time machine for your code.

Let's build it step by step.

---

## Step 1: Install WSL (The Linux Engine)

We need to tell Windows to enable its hidden Linux superpowers.

1. Click on the Windows Start menu, type **PowerShell**.
2. Right-click on "Windows PowerShell" and select **"Run as administrator"**.
3. In the blue/black window, paste this exact command and press Enter:
   ```powershell
   wsl --install
   ```
4. Windows will download Ubuntu (the most user-friendly Linux distribution) and set it up. Once it finishes, **restart your computer**.
5. After restarting, open the Start menu, search for **Ubuntu**, and open it.
6. A black terminal window will appear. It will ask you to create a **UNIX username** and **password**. 
   > ⚠️ **CRITICAL NOTE:** When you type your password, **nothing will show up on the screen** (no dots, no asterisks). This is a standard Linux security feature. Just type your password blindly and press Enter.

---

## Step 2: Equip Linux with the Basics and Git

Now that you have a fresh Linux system, we need to update it and install some essential building blocks.

1. In your Ubuntu terminal, paste the following command. (The `sudo` command means "Super User DO", which gives you administrative rights. It will ask for the password you just created):
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```
2. Next, install the basic compiler tools, a web downloader (`curl`), and `git`:
   ```bash
   sudo apt install build-essential curl git -y
   ```
3. Finally, tell Git who you are so your code contributions are properly credited. Run these two commands (replace with your actual name and email):
   ```bash
   git config --global user.name "Your First and Last Name"
   git config --global user.email "your.email@example.com"
   ```

---

## Step 3: Install `uv` (The Package & Python Manager)

Forget about downloading Python from a website or installing bulky Anaconda distributions. `uv` handles everything.

1. In your Ubuntu terminal, paste this command to download and install `uv`:
   ```bash
   curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
   ```
2. For the system to recognize the new `uv` command, you need to refresh your terminal. The easiest way is to simply **close the Ubuntu window and open it again** from the Start menu.

---

## Step 4: Install VS Code and the WSL Bridge

Now we set up the interface where you will actually write your code.

1. On your normal Windows system, open your web browser and download **Visual Studio Code** from [https://code.visualstudio.com/](https://code.visualstudio.com/). Install it normally.
2. Open VS Code. 
3. On the far left menu bar, click the icon that looks like four squares (this is the **Extensions** marketplace), or press `Ctrl+Shift+X`.
4. Search for an extension called **WSL** (published by Microsoft) and click **Install**. 
   *This extension is the bridge. It allows VS Code on Windows to peek inside the Linux system.*

---

## Step 5: Create Your First Project!

Let's test the whole setup by creating a new, properly structured project.

1. Open your **Ubuntu** terminal again.
2. Create a new folder for your project and move inside it:
   ```bash
   mkdir my_first_project
   cd my_first_project
   ```
3. Initialize the Python project using `uv`. This is the modern standard way to start:
   ```bash
   uv init
   ```
   *(Notice how fast it is! Instead of just creating a blank folder, `uv` instantly sets up the best practices for you: it creates a `pyproject.toml` file to manage your future packages, sets the Python version, and gives you a sample `hello.py` script).*
4. Initialize a Git repository to start tracking your code changes:
   ```bash
   git init
   ```
5. Finally, open this project in VS Code by typing:
   ```bash
   code .
   ```
   *(The `.` means "this current folder"). The first time you do this, it will take a few seconds to install the VS Code Server inside Linux. Then, the VS Code window will pop up.*

---

## Step 6: The `uv` Workflow (Packages & Execution)

Now that you are in VS Code, look at the bottom-left corner of the window. You should see a green/blue button that says **"WSL: Ubuntu"**. This proves you are writing code on Windows, but executing it on Linux!

Let's open the **Integrated Terminal** in VS Code (Go to the top menu: `Terminal -> New Terminal`). Ensure you are using this terminal for the next steps.

### 1. Adding Packages
Unlike older tools where you had to manually create a virtual environment first, `uv` is smart. Let's add a popular web package called `requests`:
```bash
uv add requests
```
**What just happened?** Two amazing things: 
1. `uv` downloaded the package and added it to your `pyproject.toml` file.
2. It **automatically created** a hidden `.venv` folder. This is your isolated project bubble! 

### 2. Running Code
To run your Python scripts using this isolated environment, you don't need to manually "activate" it. Just use the `uv run` command:
```bash
uv run hello.py
```
This guarantees that your code always uses the exact dependencies defined in your project.

---

## Step 7: VS Code & Jupyter Configuration

To get features like autocomplete and error checking, we need to tell VS Code where our new `uv` environment is.

1. In VS Code, open the **Extensions** panel (`Ctrl+Shift+X`).
2. Search for the **Python** extension (published by Microsoft) and click **Install**. 
   *(Notice it says "Install in WSL: Ubuntu" - this is exactly what we want).*
3. Open any `.py` file. In the bottom right corner of VS Code, click on the Python version to **Select Interpreter**. Choose the one that points to your new project bubble: `./.venv/bin/python`.

### 📓 Bonus for Data Scientists (Jupyter Notebooks)
If you work with Data Science or AI, you probably use Jupyter Notebooks (`.ipynb` files). To make your `uv` environment work seamlessly with notebooks, you need to install a "kernel".
Run this in your terminal:
```bash
uv add --dev ipykernel
```
*(Note the `--dev` flag. This tells `uv` that this tool is only for your development environment and isn't required for the final application to run!).* Now you can open any Notebook in VS Code and select your `.venv` as the kernel!

---

## Step 8: The Final Test 🧪

Let's make sure everything is working perfectly. You can test your new setup using the script provided in this repository.

1. Download or copy the `test_setup.py` file from this repository into your new project folder.
2. In your VS Code terminal, run this command:
   ```bash
   uv run python test_setup.py
   ```
3. If your setup is correct, you will see a congratulatory message confirming your OS, your Python version, and that your `uv` Virtual Environment is active. 

Welcome aboard! 🚀

---

## 📚 Resources & Next Steps

Now that your environment is running perfectly, it's time to start building! Here are the best resources to continue your journey, divided by how you prefer to learn.

### 1. Technical Resources (The Official Manuals)
* **[The Official `uv` Documentation](https://docs.astral.sh/uv/):** Learn the granular details of what your new lightning-fast tool can do.
* **[VS Code for Python](https://code.visualstudio.com/docs/python/python-tutorial):** Microsoft's official guide on getting the most out of VS Code.
* **[WSL Documentation](https://learn.microsoft.com/en-us/windows/wsl/):** Dive deeper into how the Linux engine works alongside Windows.
* **[GitHub Skills](https://skills.github.com/):** Free, interactive courses built by GitHub to help you master version control.
* **[Ubuntu Command Line for Beginners](https://ubuntu.com/tutorials/command-line-for-beginners):** A great, step-by-step tutorial to learn how to move around your new Linux terminal (`cd`, `ls`, `mkdir`, etc.).
* **[The Official Python Tutorial](https://docs.python.org/3/tutorial/index.html):** The ultimate source of truth if you are learning Python from scratch.

### 2. Informal Resources (Mental Models & Mindsets)
Sometimes reading the manual isn't enough. To truly master these tools, you need to understand how they "think". Here are some fantastic, community-written articles focused on the philosophy of our stack:
* **`uv`:** [*The Zen-style Intro into uv. What most people miss when starting…*](https://medium.com/data-science-collective/the-zen-style-intro-into-uv-a53b1e6e467e) (by Gwang-Jin) – A great read on the mindset shift required for modern Python package management.
* **Git:** [*Git Commands Mental Map*](https://medium.com/@hossain.shomik/git-commands-mental-map-16cba44cc406) (by Ekram Hossain) – Stop memorizing commands and start visualizing Git as a graph. It changes everything.
* **WSL:** [*WSL: Bridging the Gap Between Windows and Linux*](https://thebytestream.medium.com/windows-subsystem-for-linux-wsl-bridging-the-gap-between-windows-and-linux-03602fc569fe) – A conceptual overview of why WSL is a game-changer compared to old-school Virtual Machines.

### 3. Cheat Sheets (Keep these bookmarked!)
Don't try to memorize everything. Real developers use cheat sheets every day.
* **[Git Cheat Sheet (PDF)](https://training.github.com/downloads/github-git-cheat-sheet.pdf):** The legendary official GitHub cheat sheet. Print it out and keep it on your desk.
* **[VS Code Keyboard Shortcuts (PDF)](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf):** The fastest way to code is to stop using your mouse.
* **[Linux Command Line Cheat Sheet](https://cheatography.com/davechild/cheat-sheets/linux-command-line/):** A highly condensed, single-page cheat sheet for all the essential Linux terminal commands.

### ⚡ Bonus: The `uv` Mini-Cheat Sheet
*(Since `uv` is a modern tool, keep this quick reference guide handy!)*

**Project Setup & Execution**
* `uv init` ➔ Initialize a new Python project (creates `pyproject.toml` and a default setup).
* `uv run <script.py>` ➔ Run a script using your project's isolated environment.
* `uv run <tool>` ➔ Run a command-line tool securely (e.g., `uv run pytest` or `uv run ruff`).

**Managing Dependencies**
* `uv add <package>` ➔ Install a package, add it to `pyproject.toml`, and update the `.venv`.
* `uv add --dev <package>` ➔ Add a package meant only for development (e.g., `ipykernel`, `black`).
* `uv remove <package>` ➔ Uninstall a package and cleanly update your configuration files.
* `uv sync` ➔ Install or update all dependencies listed in your project (perfect for when you clone a repo from GitHub).

**Python Versions & Classic Environments**
* `uv python pin 3.12` ➔ Lock your project to use a specific Python version.
* `uv venv` ➔ Create a traditional `.venv` virtual environment manually.
* `uv pip install <package>` ➔ Use `uv` as a blazing-fast, drop-in replacement for standard `pip` inside an active environment.