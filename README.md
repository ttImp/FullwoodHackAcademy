# Welcome to the Fullwood Hackademy 2025!

Today, we'll be learning about web application security in a hands-on ethical hacking exercise. Our goal is to understand how login forms work and how they can be tested for common vulnerabilities like weak passwords.

**Golden Rule:** The skills you learn here should only **ever** be used on systems you have explicit, written permission to test. Today, we have permission to test our live target: `https://fullwoodhackademy2025.pro/`.

---

### **Getting Started: Setup Instructions**

To begin, you need to get the necessary files onto your computer using your web browser and Python's built-in IDLE editor.

1.  **Create a Project Folder**
    First, create a new folder on your computer to hold the project files. A good place is your Desktop. Name the folder `FullwoodHackademy`.

2.  **Download the Python Script**

    * Go to the script's page in your browser: <https://github.com/ttImp/FullwoodHackAcademy/blob/main/brute_force_attack.py>

    * Click the **"Copy raw contents"** button (it looks like two overlapping squares) to copy all the code.

    * Open **Python IDLE** (you can find it in your Start Menu or Applications folder).

    * In IDLE, go to `File > New File`.

    * Paste the code you copied into the new, empty editor window.

    * Go to `File > Save` and save this file as `brute_force_attack.py` inside the `FullwoodHackademy` folder you created in the first step.

3.  **Download the Password File**

    * Inside your `FullwoodHackademy` folder, create a new subfolder and name it `data`.

    * Click this link to see the password file: <https://github.com/ttImp/FullwoodHackAcademy/blob/main/data/mockyou.txt>

    * In your web browser, go to `File > Save Page As...` and save the file as `mockyou.txt` inside the `data` folder you just created.

4.  **Download the User-Agents File**

    * This file is needed for Step 6.

    * Go to this page: <https://github.com/ttImp/FullwoodHackAcademy/blob/main/user_agents.py>

    * Like before, copy the raw code, open a **new file** in IDLE, paste the code, and save it as `user_agents.py` in your main `FullwoodHackademy` folder.

You are now set up! You will edit and run the `brute_force_attack.py` file directly from IDLE for the rest of the exercise.

---
### A Note on Editing and Running the Script

The Python script is divided into steps with titles that look like `## -- STEP 2 --`. **Do not** remove these `##` title lines, as they are just markers for each section.

You will only need to edit the lines of code that start with a **single** hash (`#`).

* **To uncomment a line of code**, simply remove the single `#` from the beginning.

* **To comment out a line of code**, add a `#` to the beginning.

* **Remember to save your changes** (`File > Save` or `Ctrl+S`) before running the script.

* **To run the script in IDLE**, press the `F5` key. The output will appear in the IDLE Shell window.

---

## Our Mission

Our mission is to gain access to a user's account on the live website. We will start by performing reconnaissance to find a target user and then build up a Python script to "brute-force" their password, trying many combinations until we find the right one.

Let's begin!

### **Step 1: Reconnaissance - Finding a Target**

Before launching an attack, we need to gather information. This is **reconnaissance**.

**Your Task:**

1.  Open your web browser and go to the live site: [**https://fullwoodhackademy2025.pro/**](https://fullwoodhackademy2025.pro/)

2.  Explore the website and find the "About Us" page.

3.  We'll be targeting an employee named **Ella**. Based on the common corporate format, can you guess her email address?

4.  Try to log in using her email. Note what the website tells you when you fail.

---

### **Step 2: Making a Simple GET Request**

Let's get our Python script to visit the login page, just like our browser did.

**Your Task:**

1.  In IDLE, open the `brute_force_attack.py` file and find the code block for `## -- STEP 2 --`. Uncomment the code below it.

2.  Press `F5` to run the script.

3.  You should see the HTML source code of the live login page printed to the IDLE Shell window.

---

### **Step 3: Sending a POST Request**

Now, let's simulate submitting the login form. A `POST` request sends data to the server.

**Your Task:**

1.  In the script, comment out the code from Step 2.

2.  Uncomment the code block under `## -- STEP 3 --`.

3.  In the `login_data` dictionary, ensure the `'email'` value is set to the target username you discovered in Step 1 (e.g., `ella@example.com`).

4.  Press `F5` to run the script. You'll see an "Invalid login" message, but you've successfully sent a login attempt!

---

### **Step 4: Brute-Force with a Password File**

Real hackers use password lists. We have a small version called `mockyou.txt`.

**Your Task:**

1.  Comment out Step 3.

2.  Uncomment `## -- STEP 4 --`.

3.  Make sure the `username_to_try` variable is set to your target's username.

4.  Press `F5` to run the script. It will now try every password from the file. This will likely fail, but it's the core of a dictionary attack.

---

### **Step 5: Appending Integers to Passwords**

A common user habit is to add a number to a password. Let's make our attack smarter.

**Your Task:**

1.  Comment out Step 4.

2.  Uncomment `## -- STEP 5 --`.

3.  This code reads each password from `mockyou.txt` and then tries appending a number to the end of it.

4.  Press `F5` to run the script. If your target is 'ella', watch closely! You should see a **Success!** message when the script discovers the correct password.

---

### **Step 6: Hiding Our Tracks with User-Agents**

To make our attack less obvious, we can change our "User-Agent" string to look like traffic from different real browsers.

**Your Task:**

1.  Comment out Step 5.

2.  Uncomment `## -- STEP 6 --`.

3.  Replace the placeholder `discovered_password` with the correct password you just found.

4.  Press `F5` to run the script and observe how the "User-Agent" changes in the output for each successful login.

---

## **Mission Accomplished!**

You've completed a full ethical hacking workflow against a live target: reconnaissance, initial access attempts, and password cracking. The principles you learned today are the foundation of professional penetration testing. Always remember to act ethically and responsibly.

---

## **Part 4: Detecting Brute-Force Attacks (Using Kibana)**

Now that you understand how a brute-force attack works from the attacker's side, let's learn how to detect it using the web server logs collected in Kibana. This is what a defender (like a Security Operations Center analyst) would do.

### **Concept: What is a Brute-Force Attack?**

Imagine someone trying to guess a password by trying every possible combination, one after another. This is called a **brute-force attack**. On a website, this often involves repeatedly trying to log in with different usernames and passwords until one works.

### **How to Detect in Logs (The Context)**

In Apache access logs, a common pattern for a brute-force attack on a login page looks like this:

1.  **Many `401 Unauthorized` responses:** This means the attacker is trying many incorrect username/password combinations. They are repeatedly failing to log in. The server is telling them, "You're not allowed in!"

2.  **Followed by a `200 OK` or `302 Found` response:** If the attacker is successful, eventually one of their guesses will work, and the server will return a successful login code (like `200 OK` for a direct success, or `302 Found` if they are redirected to a dashboard or profile page after logging in).

By looking for a large number of `401`s from the same `clientip` (the attacker's IP address) or `user_agent` (their browser/tool), specifically targeting a login page, and then seeing a successful login from that same source, you can spot a potential brute-force success.

### **Building a Visualization for Brute-Force Attempts**

We can use Kibana's **Lens** tool to create a visualization that highlights this pattern. A good way to start is by identifying which IP addresses are generating many failed login attempts.

1.  **Log in to Kibana:**
    Open your web browser and navigate to your Kibana URL (e.g., `https://kibana.fullwoodhackademy2025.pro`). Log in using your `elastic` username and the password you've set.

2.  **Navigate to the Visualize Tab:**

    * On the left-hand side navigation bar, click on the **Visualize** icon (it looks like a bar chart).

3.  **Create a New Visualization:**

    * Click the **Create visualization** button.

    * From the list of visualization types, select **Lens**.

    * Choose your `filebeat-*` index pattern as the data source.

4.  **Build the Visualization for Brute-Force:**

    * **Step 1: Choose a Chart Type**

        * On the right-hand side, under "Chart type", select **Vertical bar** or **Table**. A **Table** is often very good for this specific task because it clearly lists IPs and their counts.

    * **Step 2: Define the Rows (Client IP)**

        * Drag the **`clientip`** field from the "Fields" list on the left and drop it onto the **`Rows`** area (if using a Table) or **`X-axis`** (if using a Vertical bar chart). This will group your data by the client's IP address.

    * **Step 3: Define the Metric (Count of Failed Logins)**

        * Drag the **`Count of records`** field and drop it onto the **`Metric`** area (if using a Table) or **`Y-axis`** (if using a Vertical bar chart). This shows how many requests each IP made.

    * **Step 4: Filter for Login Attempts and Failed Responses**

        * In the **Filter bar** at the top of the screen (above the visualization), type:
            `request: "/login.php" AND response: 401`
            (Remember to adjust `/login.php` if your target's login page URL is different, e.g., `/admin/login.html`).

        * Press `Enter` to apply the filter. This will show you which IP addresses are generating failed login attempts.

    * **Step 5: Break Down by Response Code (Optional, but helpful)**

        * Drag the **`response`** field from the "Fields" list and drop it onto the **`Columns`** area (if using a Table) or **`Break down by`** (if using a Vertical bar chart). This will show the counts of different response codes (e.g., 401, 200, 302) for each IP.

5.  **Refine and Save:**

    * Adjust the time range in the top-right corner to focus on a period of activity (e.g., "Last 30 minutes" if you just ran your attack script).

    * Save your visualization (e.g., "Failed Login Attempts by IP").

### **Exercise 3: Creating a Brute-Force Detection Visualization**

1.  Using the steps above, create the "Failed Login Attempts by IP" visualization.

2.  Can you modify the filter in your visualization to show only requests to `/wp-admin/` paths that result in `401` errors?
    (Hint: Change the filter in the filter bar to `request: "/wp-admin/*" AND response: 401`).

3.  **Investigating a Potential Brute-Force Success:**
    Once you have a visualization showing IPs with many `401`s, how would you use Kibana to investigate if one of those IPs eventually succeeded in logging in?

    * **Step 1: Identify a Suspicious IP:** From your "Failed Login Attempts by IP" visualization, find a `clientip` that has a very high count of `401` responses.

    * **Step 2: Go to Discover:** Click on the **Discover** icon.

    * **Step 3: Filter by Suspicious IP and Request Path:** In the Discover search bar, enter a filter like:
        `clientip: "THE_SUSPICIOUS_IP_HERE" AND request: "/login.php"`
        (Replace "THE_SUSPICIOUS_IP_HERE" and "/login.php" with the actual values).

    * **Step 4: Sort by Time:** Ensure the events are sorted by `@timestamp` (ascending or descending) to see the sequence of events from that IP.

    * **Step 5: Look for Success:** Scroll through the events. Are there any `200 OK` or `302 Found` responses from that same `clientip` to the login page or a redirect *after* many `401`s? If so, that's a strong indicator of a successful brute-force attack!

You now have the tools to launch a simulated brute-force attack and then detect it in your logs like a real security analyst!