# -*- This is flask excercise -*-
"""
Created on Sat Feb 17 17:54:06 2018

@author: User
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index.html') # port 5000
def index():
    return render_template('index.html')

@app.route('/create.html') # port 5000
def create():
    return render_template('create.html')

#def create():
   # return render_template('create.html')
#app.add_url_rule('/create', 'create', create)

#write methode search_type
#if({{n.value === "search"}}):

#else:
    #do filter here
    
#write methode keyword (search in main.py)
#def search():

#write methode stop_crol
    #methode to stop feching data


@app.route('/update.html') # port 5000
def update():
    return render_template('update.html')

@app.route('/delete.html') # port 5000
def delete():
    return render_template('delete.html')

@app.route('/networkE.html') # port 5000
def networkE():
    return render_template('networkE.html')

if __name__ == '__main__':
    app.run(debug=True) #debug=True to avoid every time restart the server from cmd
                        #Just refresh from the browser
                        

    

