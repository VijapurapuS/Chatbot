
### Movie_Recommendation_Bot using Slack and IBM Watson

Installation and Bot Setup
This file will walk you through the steps to setup your bot. Download the entire folder and the follow the steps below. 

### Step 1: 
<br>
Create Slack Bot user

### Step 2: 
<br>
Create a IBM Watson account and Upload the bot.json workspace

### Step 3: 
<br>
Install the required packages listed in the requirements.txt file. To install the required packages, please use the code below.

`pip3 install -r requirements.txt
<br>
It would be recommended to use Python 3.5.x or 3.6.x version for this project.

### Step 4: 
<br>
Update the config files with the Slack and Watson API details
Please make sure that you modified the API details both for Slack and Watson in the config.py file

### Step 5:
<br>
Download data from source and perform Data Preparation.
The data for this example is downloaded from the location below:

https://www.kaggle.com/rounakbanik/movie-recommender-systems/data

Name of the dataset - movies_metadata.csv

"metadata_prep.csv" will be created after you run the data preparation code which will be later used in nlp models to train the movie recommendation system.

### Step 6: 
<br>
Create "onetime.txt" file
Navigate to the folder where the main.py file resides and execute the code below.

`python3 nlp/nlp_solutions/onetime_run_file.py

This will create the "onetime.txt" file automatically.

### Step 7: 
<br>
Initiate Bot
Navigate to the folder where the main python script exists and run the code below.

`python3 main.py

### Bot Design Flow
The Movie bot framework used here is a closed domain chatbot. The entire framework design is shown below.

### Step 1 (User asks question):
Users can interact with Kelly via Slack. Once the user post a question via the interface, the question is passed to the backend system for analysis

### Step 2 (NLP processing):
All the natural language processing happens in step 2.

### Step 3 (Return the NLP results):
After the NLP processing is completed, we have three outputs from it

Intents - What the user is trying to ask or query?
Entities - What is the exact field or column they are looking for?
Dialog/Interaction - Provide the appropriate request/response for the user question.
<br>

### Step 4 and 5(Query the data):
Currently, the data resides in a excel file. However, you can add multiple databases/excel files if needed, to access different sources. Based on the results from step 3, the appropriate database/excel file is queried and the results are returned.

### Step 6 (Post the result to user):
The results obtained from the backend is posted to user via Slack

### Step 7 (Log maintenance):
The interactions between the users are logged and stored in a flatfile format in a log file. Also, if the bot is not able to identify the user questions it will add those questions to a followup file.
