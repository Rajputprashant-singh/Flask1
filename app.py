from flask import Flask,request,render_template
app = Flask (__name__)
@app.route('/')
def hello ():
    return "Hello,World"
print(__name__)

if __name__=='__main__':
    app.run(debug=True)