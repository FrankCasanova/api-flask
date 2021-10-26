from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.get("/")
def index():
    """
    Render the home page privided under templates/index.html 
    in the repository
    """
    return render_template("index.html")


@app.get("/search")
def search():
    """
    1. Capture the word that is being searched
    2. Search for the word on Google and display results
    """
    args = request.args.get("q")
    return redirect(f'https://google.com/search?q={args}')

@app.get("/wiki/")
def wiki():
    """
    challenge
    """
    args = request.args.get('q')
    return redirect(f'https://en.wikipedia.org/wiki/{args}')


if __name__ == "__main__":
    app.run()    