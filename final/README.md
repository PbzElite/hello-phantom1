<b>This is the final copy. Everything put here must be considered good-to-run, and the corresponding 'final' folder on the Raspberry Pi will be updated to match.</b>

.py files:
<ul>
  <li><b>run_all.py:</b> Baseline loop in which all code is run. Imports other classes/methods in this directory to control the entire process. <b>This will be the single file run to turn on the Hello Phantom</b></li>
  <li><b>recognizer.py:</b> Takes the voice input as a string, and pulls out relevant tokens (and synonyms) for determining what the user is requesting and how; Outputs an array in the form [webscraper, arg1, arg2, arg3...], where webscraper is the webscraper to use, and args are the arguments to be passed into said webscraper (can be of variable length as long as no IndexOutOfBounds are called)</li>
  <li><b>scrape_control.py:</b> Imports the webscrape files, chooses which one to use (based on output of recognizer.py), and passes the remaining arguments into the webscraper (returns text output)</li>
</ul>
<br>
Folders:
<ul>
  <li><b>webscrape:</b> Contains all the individual webscrape files to be called by scrape_control.py (ex: weather.py, events.py)</li>
</ul>
