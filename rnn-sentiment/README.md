# RNN Sentiment Exercise

> Task: build an RNN to do sentiment analysis.

## 💻 Setting up development environment

To do this exercise, you'll want to install some Python libraries. Run the following in the working directory to create a virtual environment called `venv`:

```shell
python3 -m venv venv
```

Then, activate the virtual environment:

```shell
source venv/bin/activate
```

Then, install `requirements.txt`:

```shell
pip install -r requirements.txt
```

## 🏋️‍♂️ Training data

Keras has the IMDB movie review dataset, which we can use!

## 🏃‍♀️ Running the exercise

To run the exercises, run:

```shell
python sentiment.py
```

## 📚 Tasks

Here are the tasks:

1. Read [this guide](https://www.tensorflow.org/guide/keras/rnn) and [this guide](https://towardsdatascience.com/a-beginners-guide-on-sentiment-analysis-with-rnn-9e100627c02e) to making RNN's in Keras.
2. Build out the `get_model` function according to specification.
3. Add the required lines for training and testing the model.
4. Experiment with different numbers of units and see how it affects the accuracy.