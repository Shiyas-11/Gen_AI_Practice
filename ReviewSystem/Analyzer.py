

def Analyzer(name,email,rev,Emailchain,Reviewchain):
	resp={}
	mails={}
	resp["name"]=name
	resp["email"]=email
	response=Reviewchain.invoke({"review":rev})
	
	print(response)
	resp["review"]=response
	mail=Emailchain.invoke({"review":rev,"details":resp})
	mails[email]=mail

	return {"Rating":resp,"Mail":mails}








