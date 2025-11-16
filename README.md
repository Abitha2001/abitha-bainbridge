# **European Parliament Top Stories Extractor**

A Python script that fetches, cleans, and saves “Top Stories” from the European Parliament’s RSS feed.

## **Overview**

1. This project shows how to retrieve and store the latest Top Stories from the European Parliament’s official RSS feed.  
2. The script connects to the RSS link, reads the XML data, removes HTML tags from the descriptions, and saves everything into a clean CSV file.  
3. This makes it easy to use the data for reports, analysis, or dashboards. The code is simple, easy to understand, and works on any computer with Python.

## **Features**

* Fetches live RSS data from the European Parliament website

* Parses XML using Python’s built-in `xml.etree.ElementTree`

* Cleans HTML content using BeautifulSoup

* Saves all stories into a CSV file with UTF-8 encoding

* Prints clear progress messages

* Works on Windows, macOS, and Linux

## **Project Structure**

`european-parliament-top-stories/`  
`│`  
`├── european_parliament_top_stories.py     # Main script`  
`├── README.md                              # Guide`  
`└── european_parliament_top_stories.csv    # Output file (created after running the script)`

## **Prerequisites**

Before running the script, make sure you have:

* Python version 3.8 or higher  
   Check with: `python --version`

* Internet access, because the script downloads live data

## **Installation Steps**

### **1\. Download the project**

Option A: Clone the repository using Git:

`git clone https://github.com/your-username/european-parliament-top-stories.git`  
`cd european-parliament-top-stories`

Option B: Download the ZIP file from GitHub and extract it.

### **2\. Create a virtual environment (optional but recommended)**

`python -m venv venv`

Activate it:

macOS/Linux:

`source venv/bin/activate`

Windows:

`venv\Scripts\activate`

### **3\. Install required Python libraries**

If you have a `requirements.txt` file:

`pip install -r requirements.txt`

Or install manually:

`pip install requests beautifulsoup4`

## **Usage**

Run the script from your terminal:

`python european_parliament_top_stories.py`

The script will:

1. Connect to the European Parliament RSS feed

2. Read each story’s title, link, date, and description

3. Remove HTML tags from the description

4. Save the clean output into:

`european_parliament_top_stories.csv`

You will see progress messages like:

`Fetching RSS feed data...`  
`RSS feed retrieved successfully.`

`Parsing RSS feed data...`  
`Parsed 10 stories successfully.`

`Saving stories to 'european_parliament_top_stories.csv'...`  
`Saved 10 stories successfully.`

`All done! Check your CSV file for the latest top stories.`

## **Output Example**

| Title | Link | Publication Date | Description |
| ----- | ----- | ----- | ----- |
| Top story \- Sakharov Prize 2023 | [https://www.europarl.europa.eu/news/en/headlines/priorities/sakharov-2023](https://www.europarl.europa.eu/news/en/headlines/priorities/sakharov-2023) | Wed, 08 Nov 2023 11:44:00 GMT | The European Parliament's 2023 Sakharov Prize for Freedom of Thought has been awarded to Jina Mahsa Amini and the Woman, Life, Freedom movement in Iran. |

## **Advanced Options**

You can modify the script to:

* Append only new stories

* Export the data to JSON or Excel

* Schedule automatic updates using cron or Task Scheduler

* Connect the output to Power BI or Tableau

## **Troubleshooting**

| Issue | Possible Cause | Solution |
| ----- | ----- | ----- |
| requests.exceptions.ConnectionError | Internet not working or firewall blocking access | Check your network or VPN |
| ModuleNotFoundError: No module named 'bs4' | BeautifulSoup not installed | Run `pip install beautifulsoup4` |
| CSV file not created | No permission to write in the folder | Run as administrator or save in a different directory |

## **Portability**

This script works on:

* Windows

* macOS

* Linux

* Any environment with Python 3 (VS Code, Anaconda, Jupyter, etc.)

There is no platform-specific code, so it should run smoothly on most machines.

## **Example Use Cases**

* Journalists who need fast access to EU political updates

* Data analysts building dashboards

* Developers who need structured political data for applications

* Researchers studying trends in EU communication

