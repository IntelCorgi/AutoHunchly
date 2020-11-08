# AutoHunchly
A python script for automating the collection of web pages with [Hunchly](www.hunch.ly).

_Note: I am not affiliated with the Hunchly team in any way!_

## What is AutoHunchly?
Manually archiving webpages as a part of an investigation can be a major pain, especially when you have a list of over 100 domains on your to do list. AutoHunchly is a simple python script which uses Selenium to manually navigate to a ueser-supplied list of target webpages. The webpages will be captured in Hunchly as if the user was taking the time to navigate to each one. The analyst can then further analyze the webpages within Hunchly or retain them for archiving/future analysis.

### How Hunchly Works
[Hunchly](www.hunch.ly) is (IMO) one of the best tools in an investigator's arsenal. While an analyst investigates suspicious or malicious domains, Hunchly archives a copy of the page. From the [Hunchly Evidence Guide:](https://www.hunch.ly/resources/Hunchly%20Evidence%20Guide.pdf)

    Hunchly captures all web pages in the MHTML format. 
    
    This format is very similar to how emails are structured, 
    
    they contain headers with information describing the page itself, 
    
    the timestamp of when Chrome itself captured the page and it also includes all of the text, CSS styles and images that are contained on the page. All in a single file. 
    
    This is superior to PDF or screenshots as all links are maintained, the layout is generally more accurate and all metadata is preserved including the metadata in the captured images.

As investigations become more complex as pivots are made, all the pages are collected in a central case file, along with user defined selectors, metadata, and other handy things. Hunchly also allows an analyst to generate a customized a report.


## Setting up AutoHunchly

AutoHunchly is pretty easy to set up. The only things you really need to do are install the Selenium python package and ensure the Chrome driver is in the correct directory.

1) Install Selenium with the following command:

    pip3 install selenium

2) If you don't have Chrome installed already, go ahead and install it. If you have Chrome installed, ensure it is the latest version. [Then, grab the latest Chrome web driver.](https://chromedriver.chromium.org/downloads). Install the Hunchly Chrome extension and **Ensure it will run in incognito mode.** 

3) [Follow the Hunchly setup guide to get it started](https://www.hunch.ly/downloads)

4) Start a new case in Hunchly, then turn it on in Chrome and point it to your case file. 

5) Place a file called "domains.txt" in the same folder as AutoHunchly.py. Ensure that the file contains only the domain name and there is a return ("\n") after each domain. It should look something like this:

       domain1.com
       domain2.com
       domain3.com

## Using AutoHunchly

***WARNING! ENSURE YOU ARE HIDING YOUR IP ADDRESS WITH A VPN!!!***

Assuming AutoHunchly and Hunchly are configured correctly, simply run it like any other python script.

## Planned Improvements

* Take the domain list as an argument instead of being hardcoded.

* Spidering option: Have selenium get a list of links as it navigates to each page, and append those links to the list of targets.

* Collect data from pages and output them to an excel spreadsheet or db.

* Add an IP rotator or options to set a Digital ocean droplet as an upstream proxy.

## Notes

**OPSEC Warning**

If you are attempting to archive a group webpages that are potentially owned by the same entity, consider how the traffic might look if you are iteratively going through every domain they own. That might stick out as incredibly obvious and be a giveaway they are under investigation.

AutoHunchly will sleep for a random amount of time between 5 and 20 seconds to make the traffic appear more organic, but you may wish to manually expand that range. Also, consider an IP rotator or splitting the domain list up between multiple analysts. 

**About Scraping**

In its current version, AutoHunchly only browses to the targeted domains. Any interaction with the domain comes from Hunchly (and I do not believe there is any besides lifting the MHTML)

**What Breaks AutoHunchly?**

It appears popups may sometimes interfere with the Chrome instance created by AutoHunchly. I recommend installing an ad blocker like UBlock Origin and ensuring it runs in incognito mode.
