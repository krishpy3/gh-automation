# Setup Instructions

To ensure the security of personal access tokens and usernames, our script uses environment variables stored in a `.env` file. This file should be located in the root directory of the project. Please follow the instructions below to set up your environment correctly.

## Creating the `.env` File

1. **Navigate to the Project Directory**

   Open a terminal or command prompt and navigate to the root directory of the project where the script is located.

2. **Create a New `.env` File**

   Create a new file named `.env` in the root directory of the project. You can do this using a text editor of your choice or via the command line:

   - On Windows:
     ```cmd
     type nul > .env
     ```
   - On macOS and Linux:
     ```bash
     touch .env
     ```

3. **Open the `.env` File**

   Open the `.env` file with a text editor of your choice.

4. **Add Environment Variables**

   Copy and paste the following content into the `.env` file, replacing `your_github_username` and `your_personal_access_token` with your GitHub username and personal access token, respectively:

   ```
   GH_USERNAME=your_github_username
   GH_TOKEN=your_personal_access_token
   ```

   Ensure there are no spaces before or after the `=` signs.

5. **Save the `.env` File**

   After adding the necessary details, save the file and close your text editor.

## Final Steps

Ensure that the `.env` file is located in the root directory of the project and is not accidentally moved or deleted. This file should not be shared or committed to version control to protect your credentials.

By following these setup instructions, you have securely configured the environment variables required for the script to run properly.
