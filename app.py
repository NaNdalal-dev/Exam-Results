from flask import*
#from results import result,field
import sqlite3 as sq3


app=Flask(__name__)
@app.route('/')
def home():
	return render_template('index.html',title='Degree Results')

@app.route('/result',methods=['POST'])
def degree_result():
	try:	
		conn=sq3.connect('results.db')
		c=conn.cursor()
		uid_=int(request.form['uid'])
		crse_=request.form['course']
		c.execute('select * from {} where uid=:UID'.format(crse_),{'UID':uid_})
		res=c.fetchone()

		c.execute('pragma table_info("{}")'.format(crse_))
		desc=c.fetchall()
		columns=[]
		for i in desc:
			columns.append(i[1])

		finalresult=dict(zip(columns,res))

		return render_template('result.html',result=finalresult)
	except:
		return '<center><h1 style="color:red">Error! Invalid UID or Course</h1></center>'


if(__name__=='__main__'):
	app.run(debug=True)