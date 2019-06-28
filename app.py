from flask import Flask, render_template,request,jsonify
import evaluator
import questions

app = Flask(__name__)
app.secret_key = 'nitdelhi'

question_text=questions.list

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
   return render_template("index.html")

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        result = request.form
        username=(result['answer'])
        #print(answer)
        return answer
    return render_template("test.html")

@app.route('/details', methods=['GET', 'POST'])
def details():
    if request.method == 'POST':
        result = request.form
        print(result)
        username=(result['login'])
        if username in questions.usernames:
            return render_template("test.html",question_text=question_text)
        else:
            return "Invalid Username"
    else:
        return "Can't GET this page."

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        r = request.form
        #print(r)
        a=[]
        a.append(r['q1'])
        a.append(r['q2'])
        a.append(r['q3'])
        a.append(r['q4'])
        a.append(r['q5'])
        score={}
        for i in range(1,6):
            model_number="d2v"+str(i)+".model"
            gen_score=evaluator.generate_score(model_number,a[i-1],i-1)
            if gen_score< 0:
                score[i]=0
            else:
                score[i]=round(gen_score*100,2)
        avg_score=sum(list(score.values()))/len(list(score.values(  )))
        return render_template('results.html',score=score,avg_score=avg_score)
    else:
        return "Can't GET this page."

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000,use_reloader=True)
