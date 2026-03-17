# The Ultimate Windows Development Setup: WSL, VS Code, and `uv`

Welcome! If you are reading this, you are about to set up a professional, modern, and lightning-fast development environment on your Windows machine. 

Whether you are a seasoned developer or writing your first line of code, setting up your environment is often the most frustrating part of a project. "It works on my machine" is a common nightmare. This guide solves that problem permanently.

## 🌟 Why this specific setup?

In the past, developers had to choose: use Windows and fight with incompatible tools, or wipe their computer and install Linux. Later, tools like Anaconda (Conda) became popular, but they were incredibly heavy, slow, and complex. 

Today, we have the ultimate stack:
1. **WSL (Windows Subsystem for Linux):** You keep using Windows (with all your familiar apps), but you get a real, native Linux engine running in the background. Since 90% of the world's code and servers run on Linux, you are now developing in the native language of the internet, without sacrificing Windows.
*A Note on Native Linux: While this setup allows you to keep using Windows hassle-free, running Linux natively remains the absolute best environment for programming. If you are motivated to make the full switch to Linux, I highly encourage it! Consider this WSL workflow the best possible alternative.*
2. **Visual Studio Code (VS Code):** The most popular editor in the world. We will connect it to WSL. The magic here is that the "UI" runs on Windows, but the "Brain" (the terminal, the code execution) runs inside Linux.
3. **`uv`:** This is the game-changer. Written in Rust, `uv` replaces `pip`, `virtualenv`, `conda`, and even Python installers. It is blazingly fast. It manages your project's dependencies and **automatically downloads the correct version of Python** for you. No more messing with system environment variables!
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

Let's test the whole setup by creating a new, isolated project environment.

1. Open your **Ubuntu** terminal again.
2. Create a new folder for your project and move inside it:
   ```bash
   mkdir my_first_project
   cd my_first_project
   ```
3. Initialize a Git repository to start tracking changes:
   ```bash
   git init
   ```
4. Create the virtual environment using `uv`. A virtual environment is like a clean, isolated bubble for your project so its dependencies don't mix with other projects.
   ```bash
   uv venv
   ```
   *(Notice how fast it is! `uv` will automatically download the correct Python version if you don't have it, and set up the `.venv` folder in milliseconds).*
5. Finally, open this project in VS Code by typing:
   ```bash
   code .
   ```
   *(The `.` means "this current folder"). The first time you do this, it will take a few seconds to install the VS Code Server inside Linux. Then, the VS Code window will pop up.*

---

## Step 6: Final VS Code Configuration

You are almost done! Look at the bottom-left corner of your VS Code window. You should see a green/blue button that says **"WSL: Ubuntu"**. This proves you are writing code on Windows, but executing it on Linux!

1. In VS Code, open the **Extensions** panel again (`Ctrl+Shift+X`).
2. Search for the **Python** extension (published by Microsoft) and click **Install**. 
   *(Notice it says "Install in WSL: Ubuntu" - this is exactly what we want).*
3. Open or create a `.py` file. In the bottom right corner of VS Code, you can click on the Python version to select your interpreter. Choose the one that points to `./.venv/bin/python` (the isolated bubble we created in Step 5).

---

## Step 7: The Final Test 🧪

Let's make sure everything is working perfectly. You can test your new setup using the script provided in this repository.

1. Download or copy the `test_setup.py` file from this repository into your new project folder.
2. In your VS Code terminal (which should be running on WSL and have your virtual environment active), run this command:
   ```bash
   uv run python test_setup.py
   ```
3. If your setup is correct, you will see a congratulatory message confirming your OS, your Python version, and that your `uv` Virtual Environment is active. 

Welcome aboard!