# Sentiment Analysis Bot

This project is **a Streamlit application** that **analyzes the sentiment of user-input text**. It uses **Hugging Face's pre-trained cardiffnlp/twitter-roberta-base-sentiment model** to determine whether the text is positive, negative, or neutral.

## 📌 Features
- ✅ User-Friendly Interface: A simple and interactive web interface built with Streamlit.
- ✅ Sentiment Analysis: Analyzes the sentiment of input text (positive, negative, or neutral).
- ✅ Confidence Score: Displays how confident the model is in its prediction.

  ---

## 🛠️ How It Works
- The user enters a text in the input box.
- When the "Analyze" button is clicked, the model analyzes the sentiment of the text.
- The result (sentiment and confidence score) is displayed on the screen.

## 🛠️ Installation
To run this project locally, follow these steps:
# Prerequisites
- Python 3.7 or higher
- Streamlit
- Transformers (Hugging Face)
- PyTorch
# Installation Steps
Clone the repository:
```
git clone https://github.com/your-username/sentiment-analysis-bot.git
cd sentiment-analysis-bot
```
Install the required libraries:
```
pip install -r requirements.txt
```
Launch the Streamlit app:
```
streamlit run app.py
```
The app will automatically open in your browser.
## Usage
After launching the app, you will see a text box on the browser.
Enter the text you want to analyze in the text box.
Click the "Analyze" button.
The sentiment and confidence score will be displayed on the screen.
## Example Input and Output
- Input: "I love this product! It's amazing."
- Output: "Sentiment: positive, Confidence Score: 0.98"
## Contributing
If you'd like to contribute to this project, please follow these steps:
- Fork the repository.
- Create a new branch
```
git checkout -b new-feature
```
- Commit your changes
```
git commit -am 'Add new feature'
```
- Push to the branch
```
git push origin new-feature
```
Create a Pull Request.
## License
This project is licensed under the MIT License. See the LICENSE file for more details.
