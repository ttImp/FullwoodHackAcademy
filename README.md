# Welcome to the Fullwood Hackademy 2025!

Today, we'll be learning about web application security in a hands-on ethical hacking exercise. Our goal is to understand how login forms work, how they can be tested for common vulnerabilities like weak passwords, and **crucially, how to detect such attacks using web server logs in Kibana.** We'll also explore what happens *after* a successful login and how seemingly small details, like cookies, can sometimes be manipulated if a website isn't built securely.

**Golden Rule:** The skills you learn here should only **ever** be used on systems you have explicit, written permission to test. Today, we have permission to test our live target: `https://fullwoodhackademy2025.pro/`.

---

## **Part 1: Launching a Brute-Force Attack (Offensive Security)**

This section guides you through setting up a Python script to perform a simulated brute-force attack.

### **Section 1.1: Setup Instructions**

To begin, you need to get the necessary files onto your computer. These files are part of this GitHub repository.

1.  **Create a Project Folder**
    First, create a new folder on your computer to hold the project files. A good place is your Desktop. Name the folder `FullwoodHackademy`.

2.  **Download the Python Script (`brute_force_attack.py`)**

    * Go to the script's page in your browser: <https://github.com/ttImp/FullwoodHackAcademy/blob/main/brute_force_attack.py>

    * Click the **"Copy raw contents"** button (it looks like two overlapping squares) to copy all the code.

    * Open **Python IDLE** (you can find it in your Start Menu or Applications folder).

    * In IDLE, go to `File > New File`.

    * Paste the code you copied into the new, empty editor window.

    * Go to `File > Save` and save this file as `brute_force_attack.py` inside the `FullwoodHackademy` folder you created in the first step.

3.  **Download the Password File (`mockyou.txt`)**

    * Inside your `FullwoodHackademy` folder, create a new subfolder and name it `data`.

    * Click this link to see the raw password file content: <https://raw.githubusercontent.com/ttImp/FullwoodHackAcademy/main/data/mockyou.txt>
    *(This link shows the plain text content directly in your browser.)*

    * **To save this file:**
        * **Option A (Most direct):** Right-click anywhere on the page, select "Save As..." or "Save Page As...", and save the file as `mockyou.txt` inside the `data` folder you just created.
        * **Option B (Copy/Paste):** Copy all the text from the browser page. Open a new text file in your `data` folder (e.g., using Notepad on Windows or TextEdit on Mac), paste the content, and save it as `mockyou.txt`.

4.  **Download the User-Agents File (`user_agents.py`)**

    * This file is needed for Step 6.

    * Go to this page to see the raw code: <https://raw.githubusercontent.com/ttImp/FullwoodHackAcademy/main/user_agents.py>
    *(This link shows the plain text content directly in your browser.)*

    * Like before, copy all the raw code from the browser page. Open a **new file** in IDLE, paste the code, and save it as `user_agents.py` in your main `FullwoodHackademy` folder.

You are now set up! You will edit and run the `brute_force_attack.py` file directly from IDLE for the rest of the exercise.

---
### **Section 1.2: A Note on Editing and Running the Script**

The Python script is divided into steps with titles that look like `## -- STEP 2 --`. **Do not** remove these `##` title lines, as they are just markers for each section.

You will only need to edit the lines of code that start with a **single** hash (`#`).

* **To uncomment a line of code**, simply remove the single `#` from the beginning.

* **To comment out a line of code**, add a `#` to the beginning.

* **Remember to save your changes** (`File > Save` or `Ctrl+S`) before running the script.

* **To run the script in IDLE**, press the `F5` key. The output will appear in the IDLE Shell window.

---

### **Section 1.3: Our Mission (Offensive)**

Our mission is to gain access to a user's account on the live website. We will start by performing reconnaissance to find a target user and then build up a Python script to "brute-force" their password, trying many combinations until we find the right one. After gaining access, we'll see if we can trick the website into giving us more power than we should have.

Let's begin!

**Step 1: Reconnaissance - Finding a Target and Understanding Password Complexity**

Before launching an attack, we need to gather information. This is **reconnaissance**. This helps us understand what kind of users might exist and what kind of passwords the website might accept, which can make our brute-force attack more efficient.

**Your Task:**

1.  Open your web browser and go to the live site: [**https://fullwoodhackademy2025.pro/**](https://fullwoodhackademy2025.pro/)

2.  Explore the website and find the "About Us" page.

3.  We'll be targeting an example user. Based on the common corporate format, can you guess a potential email address for an employee (e.g., `firstname.lastname@example.com`)? This will be your `target_username`.

4.  Try to log in using this example email with a random password. Note what the website tells you when you fail.

5.  **Understanding Password Complexity (In the Wild):** In a real-world scenario, you might try to sign up for a new account on the target website. Even if you don't complete the signup, the website's registration form often gives clues about password complexity requirements (e.g., "Password must be at least 8 characters long," "Must include a number and a special character"). This information is super valuable for building a smarter password list for your brute-force attack.

    * **Try This:** On the live site, look for a "Sign Up" or "Register" link. Click it and try to create a new account (you don't need to finish the whole process). Pay attention to any messages the website gives you about password rules as you type. What are they? (Note: This might not work on our live target, but it's a key step in real hacking).

---

**Step 2: Security Through Obscurity (A Bad Idea!)**

Some websites try to hide sensitive areas or pages (like an admin dashboard) by putting them in a `robots.txt` file. This file tells search engines (like Google) which pages *not* to index.

But `robots.txt` is public – anyone (even a hacker) can read `robots.txt` and see what pages the website is trying to keep secret!

**Lesson:** If something is sensitive, don't just hide it – you must protect it properly with things like strong passwords and access controls.

**Your Task:**

1.  In your web browser, go to: `https://fullwoodhackademy2025.pro/robots.txt`
2.  Look at the `Disallow:` lines. Can you find any interesting paths that might lead to a hidden admin dashboard or a special user area?
3.  Try to visit these paths in your browser (e.g., `https://fullwoodhackademy2025.pro/admin-dashboard`). What happens if you try to access them without logging in? (You should see an error or a login page, because you don't have credentials yet).

---

**Step 3: Making a Simple GET Request**

Let's get our Python script to visit the login page, just like our browser did.

**Your Task:**

1.  In IDLE, open the `brute_force_attack.py` file and find the code block for `## -- STEP 2 --`. Uncomment the code below it.

2.  Press `F5` to run the script.

3.  You should see the HTML source code of the live login page printed to the IDLE Shell window.

---

**Step 4: Sending a POST Request**

Now, let's simulate submitting the login form. A `POST` request sends data to the server.

**Your Task:**

1.  In the script, comment out the code from Step 3.

2.  Uncomment the code block under `## -- STEP 3 --`.

3.  In the `login_data` dictionary, ensure the `'email'` value is set to the `target_username` you discovered in Step 1 (e.g., `target.user@example.com`).

4.  Press `F5` to run the script. You'll see an "Invalid login" message, but you've successfully sent a login attempt!

---

**Step 5: Brute-Force with a Password File**

Real hackers use password lists. We have a small version called `data/mockyou.txt`.

**Your Task:**

1.  Comment out Step 4.

2.  Uncomment `## -- STEP 4 --`.

3.  Make sure the `username_to_try` variable is set to your `target_username`.

4.  Press `F5` to run the script. It will now try every password from the file. This will likely fail, but it's the core of a dictionary attack.

---

**Step 6: Appending Integers to Passwords**

A common user habit is to add a number to a password. Let's make our attack smarter.

**Your Task:**

1.  Comment out Step 5.

2.  Uncomment `## -- STEP 5 --`.

3.  This code reads each password from `data/mockyou.txt` and then tries appending a number to the end of it.

4.  Press `F5` to run the script. If your target is the example user, watch closely! You should see a **Success!** message when the script discovers the correct password.

---

**Step 7: Gaining User Credentials & Understanding Cookies**

Now that we have the password for our example user, let's gain access and understand how websites use cookies.

**Context: How a Website Uses Cookies**

When you log into a website, it often gives your browser a **cookie**. A cookie is a small text file that your browser stores, and it helps the website remember who you are. Cookies are used for things like:
* Keeping you logged in as you move between pages.
* Remembering your preferences (like language or theme).
* Tracking your visits to a website.

The website might store a cookie that says something like `session_id=12345` (to identify your current visit) or `user_level=basic` (to tell the site you're a regular user, not an admin).

**Your Task:**

1.  Comment out Step 6.
2.  Uncomment `## -- STEP 6 --`.
3.  Replace the placeholder `discovered_password` with the correct password you just found for your target user.
4.  Press `F5` to run the script. It will successfully log in as your target user.
5.  **Now, open your Edge browser (or Chrome/Firefox) and go to the live site: `https://fullwoodhackademy2025.pro/`.** You should be logged in as the example user.
6.  **Open Developer Tools:** Press `F12` (or right-click anywhere on the page and select "Inspect").
7.  **Go to the "Application" Tab:** In the Developer Tools window, find the tab named "Application".
8.  **Look for Cookies:** On the left-hand side, under "Storage," click on "Cookies." You'll see a list of cookies the website has given your browser.
9.  **Find the `Admin` Cookie:** Look for a cookie named `Admin`. What value does it have?

---

**Step 8: The Browser = Untrusted Data (Cookie Manipulation for Privilege Escalation)**

Anything in your browser – like cookies, form fields, or even the JavaScript code running on the page – can be changed by the user.

That means websites can't blindly trust what the browser sends back. If a website stores sensitive information (like whether you're an admin or not) directly in a cookie and doesn't double-check it on the server, it can be a security hole! This is a form of **client-side validation bypass**, where the website relies too much on what the user's browser tells it, instead of verifying everything on the server.

Tools like the browser’s Developer Tools, `cURL`, or specialized hacking tools like `Burp Suite` let ethical hackers see and modify what’s being sent to and from the site.

**Lesson:** Let's try and elevate our normal user to be an admin user by modifying the cookie.

**Your Task:**

1.  **Ian will now demonstrate how to modify the `Admin` cookie value in your Edge browser's Developer Tools (Application tab, Cookies section).**
    * **Context:** If the `Admin` cookie is set to `0` for a regular user, what do you think setting it to `1` might do? This is a common, but very insecure, way for websites to manage user roles.
    * **Observe:** After Ian changes the cookie value and you refresh the page, do you notice any new features or different content on the website? Has your level of access changed?

---

## **Part 2: Detecting Brute-Force Attacks (Defensive Security)**

Now that you understand how a brute-force attack works from the attacker's side, let's learn how to detect it using the web server logs collected in Kibana. This is what a defender (like a Security Operations Center analyst) would do.

### **Section 2.1: Exploring Raw Log Entries in Discover**

The **Discover** tab in Kibana is your window into the raw log data. It's where you can view every single log entry, search through them, and inspect all the structured pieces of information (called "fields") that Logstash has extracted.

1.  **Log in to Kibana:**
    Open your web browser and navigate to your Kibana URL (e.g., `https://kibana.fullwoodhackademy2025.pro`).
    Log in using your `elastic` username and the password you've set.

2.  **Navigate to the Discover Tab:**

    * On the left-hand side navigation bar, click on the **Discover** icon (it looks like a compass or magnifying glass).

3.  **Select the Correct Index Pattern:**

    * In the top-left corner of the Discover page, you'll see a dropdown menu that says "Index pattern".

    * Click on this dropdown and select `filebeat-*`. This tells Kibana to show you all the logs collected by Filebeat from your Apache server.

4.  **Adjust the Time Range:**

    * In the top-right corner of the screen, you'll see a time range selector (e.g., "Last 15 minutes").

    * Click on this and choose a relevant time range where you know you've generated some Apache traffic (e.g., "Last 1 hour" or "Last 24 hours"). This will update the displayed logs.

5.  **Inspect Log Entries:**

    * You should now see a list of individual log entries. Each row represents a single event that happened on your Apache web server.

    * Click on any log entry in the main table to expand it. This will show you the raw `message` field (the original log line) and all the structured fields that Logstash has parsed.

### **Understanding Your Apache Log Fields**

When Logstash processes your Apache logs, it breaks down each raw log line into many smaller, meaningful pieces of information called "fields." Here's what some of the most important ones mean:

* **`virtual_host`**: This tells you the website (Virtual Host) that the request was made to. For example, `fullwoodhackademy2025.pro`.

* **`server_port`**: The port on the server that received the request (e.g., `80` for HTTP, `443` for HTTPS). This is useful for knowing if the original request was secure or not.

* **`clientip`**: The IP address of the client (the visitor's computer) that made the request. This is super important for identifying who is accessing your server.

* **`ident`**: (Identity) and **`auth`**: (Authenticated User) - These fields are often `-` (a dash) unless you have specific Apache modules configured for user identification or authentication.

* **`@timestamp`**: This is the exact date and time (in UTC) when the event happened on the server. Kibana uses this field to organize events on a timeline.

* **`verb`**: The HTTP method used for the request, like `GET` (asking for a page), `POST` (submitting form data), `PUT`, `DELETE`, etc.

* **`request`**: The specific path or resource that was requested on your website (e.g., `/index.html`, `/login.php`, `/images/logo.png`).

* **`httpversion`**: The version of the HTTP protocol used (e.g., `1.1`).

* **`response`**: The HTTP status code returned by the server. This is a crucial field!

    * `200 OK`: Everything worked fine.

    * `301 Moved Permanently`: The page has permanently moved to a new address (often used for HTTP to HTTPS redirects).

    * `401 Unauthorized`: The client tried to access something that requires authentication, but failed (e.g., wrong username/password).

    * `403 Forbidden`: The client is not allowed to access this resource.

    * `404 Not Found`: The requested page or resource doesn't exist.

    * `500 Internal Server Error`: Something went wrong on the server's side.

* **`bytes`**: The size of the response sent back to the client, in bytes.

* **`response_time_us`**: The time it took for the server to process the request and send a response, in microseconds. This helps you find slow pages.

* **`referrer`**: The URL of the page that linked to the requested page. Useful for understanding traffic sources.

* **`http.user_agent`**: The raw, full string that identifies the client's browser, operating system, and sometimes device (e.g., `Mozilla/5.0 (Windows NT 10.0; Win64; x64) ... Chrome/137.0.0.0 Safari/537.36`).

* **`user_agent` (as an object)**: This is a structured breakdown of the `http.user_agent` string, provided by Logstash's `useragent` filter. It contains sub-fields like:

    * `user_agent.name`: The browser name (e.g., "Chrome", "Firefox").

    * `user_agent.os.name`: The operating system name (e.g., "Windows", "macOS").

    * `user_agent.device.name`: The type of device (e.g., "Other", "Tablet", "Mobile").

* **`ssl_protocol`**: The SSL/TLS protocol used for the connection (e.g., `TLSv1.2`, `TLSv1.3`). This only appears for HTTPS (port 443) requests.

* **`ssl_cipher`**: The encryption cipher suite used for the SSL/TLS connection. This also only appears for HTTPS requests.

* **`ssl_session_id`**: A unique ID for the SSL/TLS session. This also only appears for HTTPS requests.

### **Exercise 1: Finding Specific Log Entries**

1.  In the Discover tab, use the search bar at the top to find specific types of logs.

2.  Try searching for:

    * `response:404` (to see all "Not Found" errors).

    * `clientip: "YOUR_OWN_IP_ADDRESS"` (replace with your computer's public IP to see your own activity).

    * `request: "/login.php"` (to see all requests to your login page).

    * `user_agent.os.name: "Windows"` (to see requests from Windows computers).

    * Combine them: `response:401 AND request: "/admin"` (to find unauthorized attempts on admin pages).

---

### **Section 2.2: Customizing Your Discover View**

The Discover tab shows many fields by default, but you can customize it to only display the most relevant information for your investigation. This makes it easier to spot patterns quickly.

**How it should look:** [https://kibana.fullwoodhackademy2025.pro/app/discover#/view/391e2a12-b02a-41f2-9e2a-766777be856c?_g=()](https://kibana.fullwoodhackademy2025.pro/app/discover#/view/391e2a12-b02a-41f2-9e2a-766777be856c?_g=())

1.  **Go to the Discover Tab:** (If you're not already there).

2.  **Locate the Fields List:** On the left side of the Discover screen, you'll see a list of available fields.

3.  **Add/Remove Columns:**

    * To **add** a field to the main table, hover over the field name in the left list and click the **"+ Add"** button that appears.

    * To **remove** a field from the main table, hover over the field name in the main table's column header and click the **"Remove column"** (trash can) icon.

4.  **Add these specific fields as columns to your Discover table:**

    * `@timestamp`
    * `event.dataset`
    * `virtual_host`
    * `verb`
    * `request`
    * `response`
    * `clientip`
    * `geoip.geo.region_name`
    * `user_agent.name`
    * `response_time_us`

    Arrange them in an order that makes sense to you by dragging the column headers. This customized view will help you focus on the most important details for security analysis.

---

### **Section 2.3: Creating a Lens Visualization for Response Codes**

**Lens** is a powerful and easy-to-use visualization tool in Kibana that lets you drag and drop fields to create charts. We'll use it to visualize how HTTP response codes are changing over time.

1.  **Navigate to the Visualize Tab:**

    * On the left-hand side navigation bar, click on the **Visualize** icon (it looks like a bar chart).

2.  **Create a New Visualization:**

    * Click the **Create visualization** button.

    * From the list of visualization types, select **Lens**.

3.  **Select Your Data Source:**

    * In the "Select a data source" prompt, choose your `filebeat-*` index pattern.

4.  **Build the Visualization:**

    * **Step 1: Choose a Chart Type**

        * On the right-hand side, under "Chart type", select **Vertical bar**. This is good for showing counts over time.

    * **Step 2: Define the Y-axis (What to Count)**

        * Drag the **`Count of records`** field from the "Fields" list on the left and drop it onto the **`Y-axis`** area (or click the "Add" button next to "Count of records" under "Suggestions"). This will show the number of log entries.

    * **Step 3: Define the X-axis (Time Component)**

        * Drag the **`@timestamp`** field from the "Fields" list on the left and drop it onto the **`X-axis`** area.

        * Lens will automatically create a "Date histogram" for you (e.g., showing counts per minute or per hour).

    * **Step 4: Break Down by Response Code (Color)**

        * Drag the **`response`** field from the "Fields" list on the left and drop it onto the **`Break down by`** area.

        * Lens will automatically create different colored bars for each unique HTTP response code (e.g., 200, 301, 404, 500).

5.  **Refine and Customize (Optional):**

    * **Time Range:** Adjust the time range in the top-right corner to see data for different periods.

    * **Labels:** You can click on the axis labels (e.g., "Count of records", "response") to rename them for clarity.

    * **Sort Order:** You can adjust how the response codes are sorted if needed.

6.  **Save Your Visualization:**

    * In the top-right corner, click the **Save** button.

    * Give your visualization a meaningful name (e.g., "Apache Response Codes Over Time").

    * Click **Save**.

### **Exercise 2: Modifying Your Response Code Visualization**

1.  Open your "Apache Response Codes Over Time" visualization in Lens.

2.  Change the chart type from "Vertical bar" to **"Area"** or **"Line"**. How does it change your view of the data?

3.  Instead of `response` for "Break down by", try dragging `verb` (HTTP method) to "Break down by". What does this visualization tell you about your website traffic?

---

### **Section 2.4: Building a Visualization for Brute-Force Attempts**

We can use Lens to create a visualization that highlights this pattern. A good way to start is by identifying which IP addresses are generating many failed login attempts.

1.  **Navigate to the Visualize Tab:**

    * Click on the **Visualize** icon.

2.  **Create a New Visualization:**

    * Click the **Create visualization** button.

    * Select **Lens**.

    * Choose your `filebeat-*` index pattern as the data source.

3.  **Build the Visualization for Brute-Force:**

    * **Step 1: Choose a Chart Type**

        * On the right-hand side, select **Vertical bar** or **Table**. A **Table** is often very good for this specific task because it clearly lists IPs and their counts.

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

4.  **Refine and Save:**

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