try:
    from flask import Flask, render_template, request
except:
    print("Flask is required but it's not installed\nInstall this by executing: pip install flask")
    exit()
try:
    from ytdl import yt
except:
    print("Pytube is required but it's not installed\nInstall this by executing: pip install pytube")
    exit()

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    return render_template("form.html")

@app.route("/download",methods=["POST"])
def downloader():
    url = request.form['url']
    ytdict=yt(url)
    return render_template("download.html",
                           yt=ytdict
                           )

if __name__=="__main__":
    app.run(host="127.0.0.1",port=8080,debug=True)