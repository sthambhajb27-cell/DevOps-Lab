# Exercise 5: Docker Security with AppArmor

This exercise shows how to secure a Docker container using an AppArmor profile.

## Setup

1. Note: AppArmor requires Linux. If you are on a Mac using Docker Desktop, it may not fully support custom AppArmor profiles natively, but you can still run these scripts to test the Docker Python SDK functionality.

2. Install Docker Python SDK:
   ```bash
   pip install docker
   ```

3. Ensure the AppArmor profile is available to the system (Linux only):
   ```bash
   sudo cp my-apparmor-profile /etc/apparmor.d/
   sudo apparmor_parser -r /etc/apparmor.d/my-apparmor-profile
   ```

## Running the SDK Scripts

1. Build and apply AppArmor using Python SDK:
   ```bash
   python apply_apparmor.py
   ```

2. Test that restricted actions (like reading `/etc/passwd` or executing `/bin/bash`) fail:
   ```bash
   python test_restricted_actions.py
   ```
