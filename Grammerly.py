from textblob import TextBlob
a=TextBlob("i likk apples.")
a=a.correct()
print(a)
blob=TextBlob("Comment vas-tu")
print(blob.detect_language())
print(blob.translate(to='en-us'))