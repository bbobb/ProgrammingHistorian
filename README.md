
In this tutorial for sentiment analysis, you can learn how to locate a text online, install the appropriate sentimental analysis hardware, and interpret the results. For this tutorial, we'll be using Textblob, which is a Python library for common NLP tasks, such as sentiment analysis. Sentiment analysis itself involves attempting to gauge the author's sentiment towards their writing (or the object of their writing) at any particular point in a document. The particular sentiment analysis we'll be running with Textblob will assess a paragraph's polarity (meaning, the overall positive or negative term connotation), as well as its subjectivity (meaning, the degree to which a document expresses emotion rather than facts). 

For this sake of this tutorial, I've downloaded the contents of an open source book into a .txt file. I've chosen to use Sigmund Freud's "The Interpretation of Dreams," but you can use any open source document you'd like. Once you have your source material copied into a .txt file in your folder, create a "sentiment-analysis.py" file, in which to store your python commands. Begin by installing textblob with the following code: 

"from textblob import TextBlob"


Then, open the .txt file and read its contents: 

"with open("freud.txt", "r", encoding="utf-8") as f:
    text = f.read()
paragraphs = text.split('\n\n')"

Here I'm splitting the text up by paragraph for the sake of brevity, but use your discretion. You can also perform a line-by-line or sentence-level sentiment analysis. The following text sorts each paragraph with its corresponding level of polarity: 

"results = []
for i, para in enumerate(paragraphs):
    blob = TextBlob(para)
    polarity = blob.sentiment.polarity
    results.append((i, polarity))"

Finally, save and write your output to a separate .csv file, which I've named "sentiment_scores" here: 

"with open("sentiment_scores.csv", "w") as f:
    f.write("Paragraph,Polarity\n")
    for i, p in results:
        f.write(f"{i},{p}\n")"

The file should be created within your folder, and it should hold a long list of polarity scores for each paragraph of the given source material. From here, you can use visualization software such as Matlab to visualize your results. You could create a graph of Freud's sentiment over time throughout the work, as well as his subjectivity in certain matters compared to others. I hope this tutorial has been useful!
