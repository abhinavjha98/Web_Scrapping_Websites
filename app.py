from flask import *
import pandas as pd
app = Flask(__name__)

data = pd.read_csv('data.csv')
@app.route('/',methods=["GET","POST"])
def index():
	company_name = ""
	company_email = ""
	company_phone = ""
	email=""
	add=""
	company_website=""
	if request.method == "POST":
		if request.form['submit']=="submit":
			email = request.form['email']
			print(email)

			spl = email.split('@')
			cname = spl[1].split('.')
			for ind in data.index: 
				if cname[0] in data['Website'][ind]:
					print(data['Website'][ind])
					company_name = data['Company Name'][ind]
					add = str(data['Address 1'][ind]).split("||")
					company_phone = data['Phone Number'][ind]
					company_email = data['Email'][ind]
					company_website = data['Website'][ind]
	return render_template('index.html',company_name=company_name,add=add,email=email,company_website=company_website,company_phone=company_phone,company_email=company_email)

if __name__ == '__main__':
	app.run(debug=True)