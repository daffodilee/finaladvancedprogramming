
# Spam Filter Bot
This Telegram bot is designed to filter spam messages using a machine learning model trained to classify messages as spam or not spam (ham). It provides a simple interface for users to interact with the bot and receive spam classification results.

# Getting Started
To use the bot, follow these steps:

Start the Bot: Send /start to the bot to launch it.

Send Messages: Once the bot is running, you can send any text message to the bot.

Receive Classification: The bot will analyze your message and reply with whether it is classified as spam or not spam.

Stop the Bot: If you want to stop the bot from analyzing messages temporarily, send /stop.

Restart the Bot: To restart the bot and resume message analysis, send /start again.

# Commands
/start: Launches the bot and enables message analysis.
/stop: Temporarily stops the bot from analyzing messages. Use /start to resume.
Note
This bot is for demonstration purposes and may not provide perfect spam detection. It uses a machine learning model trained on a specific dataset and may not generalize to all types of spam messages.

# TG bot development
This bot was developed using Python and the python-telegram-bot library. It uses a pre-trained machine learning model for spam detection.

# ML model development
The dataset for this project was taken from Kaggle: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset.
But as long as most popular spam phrases were absent, the dataset had been updated in order to detect spam messages more appropriately by our own.

Our workflow
Data Loading: Loading the dataset using Pandas and handle any missing values.
Data Preprocessing: Converting text data into numeric features using TF-IDF vectorization. Preprocessing the text by removing stopwords, converting to lowercase, etc.
Model Training: Splitting the dataset into training and testing sets. Training a logistic regression model using the training data. Performing hyperparameter tuning using GridSearchCV to find the best regularization parameter.
Model Evaluation: Evaluating the trained model on the testing data using accuracy, precision, recall, F1-score, and confusion matrix.

The model training proccess is saved in the sf_training_colab.ipynb file.