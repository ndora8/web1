from flask import Flask, render_template, redirect, request, session
import csv

app=Flask(__name__)

@app.route('/index')
def route_main():
    global id
    id = 1
    try:
        csvreader()
        for data in table:
            id +=1
    except:
        return redirect('/index.html')

    return render_template('index.html', tbl=table)

@app.route('/add_story', methods=["POST"])
def add_story():
    story_title = request.args.get('title')
    user_story = request.args.get('story')
    accept_criteria = request.args.get('criteria')
    business_value = request.args.get('value')
    estimation = request.args.get('estim')
    status = request.args.get('statu')
    user_id = id
    story_info = [user_id,story_title, user_story, accept_criteria, business_value, estimation, status]
    cswriter(request.form)
    

def csvwriter(data):
    with open("data.csv", "a") as file:
        for data in story_info:
            if data == story_info[-1]:
                file.write(str(data) + "\n")
            else:
                file.write(str(data) + ",")
    return (data)

def csvreader():
    with open("data.csv", "r") as file:
        lines = file.readlines()
        table = [element.replace("\n", "").split(",") for element in lines]



if __name__=="__main__":
    app.secret_key='keyword'
    app.run(
        debug=True,
        port=5000
    )