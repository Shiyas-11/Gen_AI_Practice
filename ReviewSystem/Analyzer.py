

def Analyzer(name,email,rev,Emailchain,Reviewchain):
	resp={}
	mails={}
	resp["name"]=name
	resp["email"]=email
	response=Reviewchain.invoke({"review":rev})
	resp["review"]=response
	mail=Emailchain.invoke({"review":rev,"details":rev,"name":resp["name"],"email":resp["email"]})
	mails[email]=mail

	return {"Rating":resp,"Mail":mails}








