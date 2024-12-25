from flask import Flask 

app = Flask(__name__)  

@app.route('/')
def home(): 
    return "film fav ku" 
if __name__ == "__main__":  
    app.run(debug=True)  

