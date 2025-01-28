import subprocess

def check_git_config():
    try:
        # Check Git user name
        user_name = subprocess.check_output(["git", "config", "user.name"]).strip().decode("utf-8")
        print(f"Git User Name: {user_name}")

        # Check Git email
        user_email = subprocess.check_output(["git", "config", "user.email"]).strip().decode("utf-8")
        print(f"Git User Email: {user_email}")

        # Check the Git remote URL
        remote_url = subprocess.check_output(["git", "remote", "get-url", "origin"]).strip().decode("utf-8")
        print(f"Git Remote URL: {remote_url}")

    except subprocess.CalledProcessError as e:
        print("Error checking Git configuration. Please ensure Git is installed and configured properly.")
        print(e)

if __name__ == "__main__":
    check_git_config()
