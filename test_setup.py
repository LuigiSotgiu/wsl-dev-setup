# test_setup.py

import sys
import platform
import os

def main():
    print("\n🎉 SUCCESS! 🎉")
    print("If you are reading this, your development environment is correctly set up!\n")

    print("-" * 60)
    print("📊 SYSTEM DIAGNOSTICS:")
    
    # 1. Check Operating System & WSL
    os_name = platform.system()
    os_release = platform.release().lower()
    
    print(f"✅ Operating System: {os_name} {platform.release()}")
    
    if "linux" in sys.platform.lower() and "microsoft" in os_release:
        print("✅ WSL Detected: Awesome, you are running Linux inside Windows!")
    elif "linux" in sys.platform.lower():
        print("✅ Native Linux Detected: Great!")
    else:
        print("⚠️ Warning: You do not seem to be running Linux/WSL.")

    # 2. Check Python Version
    print(f"✅ Python Version: {platform.python_version()}")

    # 3. Check Virtual Environment (.venv)
    # This checks if the python executable is running from a virtual environment
    in_venv = sys.prefix != sys.base_prefix or os.environ.get('VIRTUAL_ENV') is not None
    
    if in_venv:
        print("✅ Virtual Environment: ACTIVE (Your 'uv' bubble is working flawlessly!)")
    else:
        print("❌ Virtual Environment: NOT ACTIVE.")
        print("   Did you forget to run 'uv venv' or select the right interpreter in VS Code?")
    
    print("-" * 60)
    print("\n🚀 You are fully equipped to build amazing things. Happy coding!\n")

if __name__ == "__main__":
    main()