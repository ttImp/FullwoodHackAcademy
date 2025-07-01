# Welcome to the Fullwood Hackademy 2025!

Today, we'll be learning about web application security in a hands-on ethical hacking exercise. Our goal is to understand how login forms work and how they can be tested for common vulnerabilities like weak passwords.

**Golden Rule:** The skills you learn here should only **ever** be used on systems you have explicit, written permission to test. Today, we have permission to test our live target: `https://fullwoodhackademy2025.pro/`.

---

### **Getting Started: Setup Instructions**

Before we begin, you need to get the necessary files onto your computer and make sure Python is ready to go.

#### 1. Cloning the Repository

First, you need to download all the project files from GitHub. This is called "cloning".

* Open your terminal or command prompt.
* Run the following command to clone the repository. This will create a new folder called `FullwoodHackAcademy` on your computer.

    ```bash
    git clone https://github.com/ttImp/FullwoodHackAcademy
    ```

* Now, navigate into the new directory you just created:

    ```bash
    cd FullwoodHackAcademy
    ```

You should now see all the project files (`README.md`, `brute_force_attack.py`, etc.) if you type `ls` (on Mac/Linux) or `dir` (on Windows).

#### 2. Basic Python Commands

Our attack script is written in Python. To run it, you'll need Python installed on your computer.

* **Install Dependencies:** Our script needs the `requests` library to send web traffic. You can install it using `pip`, Python's package manager. Run this command:

    ```bash
    pip install requests
    ```

* **Run the Script:** To run the main attack script, you will use the `python` command followed by the filename. We will be doing this in each step of the exercise.

    ```bash
    python brute_force_attack.py
    ```

Now you're all set up and ready to start the mission!

---

## Our Mission

Our mission is to gain access to a user's account on the live website. We will start by performing reconnaissance to find a target user and then build up a Python script to "brute-force" their password, trying many combinations until we find the right one.

Let's begin!

### **Step 1: Reconnaissance - Finding a Target**

Before launching an attack, we need to gather information about our target. This is called **reconnaissance**.

**Your Task:**
1.  Open your web browser and go to the live site: **https://fullwoodhackademy2025.pro/**
2.  Explore the website. Find the "About Us" page.
3.  Look at the employee profiles. Can you guess what their usernames might be? (Hint: Companies often use the first name as a username).
4.  **Choose one person to be your target.** Remember their likely username for the next steps.
5.  Try to login to the account using the name you have chosen, can you learn anything about the how the username must be structured? 

---

### **Step 2: Making a Simple GET Request**

Let's get our Python script to visit the login page, just like our browser did. This is done with a `GET` request.

**Your Task:**
1.  Open the `brute_force_attack.py` file and find the code block for `## -- STEP 2 --`.
2.  Run the script from your terminal: `python brute_force_attack.py`
3.  You should see the HTML source code of the live login page printed to your screen.

---

### **Step 3: Sending a POST Request**

Now, let's simulate submitting the login form. A `POST` request sends data (like a username and password) to the server.

**Your Task:**
1.  In the script, comment out the code from Step 2.
2.  Uncomment the code block under `## -- STEP 3 --`.
3.  In the `login_data` dictionary, **change the `'username'` value** to the target username you discovered in Step 1.
4.  Run the script. You'll see an "Invalid login" message, but you've successfully sent a login attempt to the live server!

---

### **Step 4: Brute-Force with a Password File**

Real hackers use password lists (dictionaries) containing millions of common passwords. We have a small version called `rockyou.txt`.

**Your Task:**
1.  Comment out Step 3.
2.  Uncomment `## -- STEP 4 --`.
3.  Make sure the `username_to_try` variable is set to your target's username.
4.  Run the script. It will now try every password from the file against the user account on the live server. This will likely fail, but it's the core of a dictionary attack.

---

### **Step 5: Appending Integers to Passwords**

A common user habit is to add a number to a password. Let's make our attack smarter by simulating this behavior.

**Your Task:**
1.  Comment out Step 4.
2.  Uncomment `## -- STEP 5 --`.
3.  This code reads each password from `rockyou.txt` and then tries appending a 3-digit number to the end of it.
4.  Run the script. If your target was 'alice', watch closely! You should see a **Success!** message when the script discovers the correct password.

---

### **Step 6: Hiding Our Tracks with User-Agents**

To make our attack less obvious and look like traffic from different real browsers, we can change our "User-Agent" string for each request.

**Your Task:**
1.  Comment out Step 5.
2.  Uncomment `## -- STEP 6 --`.
3.  This code uses the correct password (that you just found!) but sends each request with a different, random browser signature.
4.  Run the script and observe how the "User-Agent" changes in the output for each successful login.

---

## **Mission Accomplished!**

You've completed a full ethical hacking workflow against a live target: reconnaissance, initial access attempts, and password cracking. The principles you learned today are the foundation of professional penetration testing. Always remember to act ethically and responsibly.
