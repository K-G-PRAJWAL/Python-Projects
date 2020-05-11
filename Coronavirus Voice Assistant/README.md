# Coronavirus Voice Assistant

This app makes use of [ParseHub](https://www.parsehub.com/) which is a powerful web-scraping tool.

The data is extracted from the very popular website [Worldometers](https://www.worldometers.info/coronavirus/) that provides the accurate information about the COVID19 disease worldwide.

---

Steps to be followed:

1. Download [ParseHub](https://www.parsehub.com/quickstart).
2. Start a New Project and paste the link 'https://www.worldometers.info/coronavirus/'.
3. Select the items that you would like to scrape from the page and assign unique tags to each one of them. Get the data.
4. Copy the api key, project token and run token to config file and import them to your main.py file.
5. Install the requirements for this project: requests, certifi, chardet, comtypes, idna, pyttsx3, pywin32, SpeechRecognition, urllib3.
6. Run the main.py file.

---

Steps to run the application:

1. Execute the command "python main.py".
2. Ask the assistant for "number of total cases", "total cases in India", etc.
3. For updating the information, say "update" and wait for a while.
4. Say "stop" to exit the application.

---

Get more information about this project on [Medium](https://medium.com/@KGPrajwal/covid19-voice-assistant-63c37b1f02f9).

---

### Thank You!
