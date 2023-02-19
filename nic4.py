from datetime import datetime,date
import datetime as dt

nic=input("enter your nic:")
if (len(nic)==10):
	#oldnic
	year="19"+nic[0:2]
	day=int(nic[2:5])
	if day<500:
		print("gender is male")
	else:
		print("gender is female")
		day=day-500
	if int(year)%4!=0:
		#normal year
		if int(year):
			if(day<=31):
				month="01"
				date=day
			elif(day<=60):
				month="02"
				date=day-31
			elif(day<=91):
				month="03"
				date=day-60
			elif(day<=121):
				month="04"
				date=day-91
			elif(day<=152):
				month="05"
				date=day-121
			elif(day<=182):
				month="06"
				date=day-152
			elif(day<=213):
				month="07"
				date=day-182
			elif(day<=244):
				month="08"
				date=day-213
			elif(day<=274):
				month="09"
				date=day-244
			elif(day<=305):
				month="10"
				date=day-274
			elif(day<=335):
				month="11"
				date=day-305
			elif(day<=366):
				month="12"
				date=day-335
			birthDay=(year+"-"+month+"-"+str(date))
	else:
		if int(year):
			if(day<=31):
				month="01"
				date=day
			elif(day<=60):
				month="02"
				date=day-31
			elif(day<=91):
				month="03"
				date=day-60
			elif(day<=121):
				month="04"
				date=day-91
			elif(day<=152):
				month="05"
				date=day-121
			elif(day<=182):
				month="06"
				date=day-152
			elif(day<=213):
				month="07"
				date=day-182
			elif(day<=244):
				month="08"
				date=day-213
			elif(day<=274):
				month="09"
				date=day-244
			elif(day<=305):
				month="10"
				date=day-274
			elif(day<=335):
				month="11"
				date=day-305
			elif(day<=366):
				month="12"
				date=day-335
	birthDay=(year+"-"+month+"-"+str(date))
	print("birthday:", birthDay)

	today=dt.date.today()

	birthDay_type=(year+"-"+month+"-"+str(date))
	birthDay_obj= dt.datetime.strptime(birthDay_type,"%Y-%m-%d")
	if(today.month==birthDay_obj.month and today.day>=birthDay_obj.day or today.month>birthDay_obj.month):
		nextBirthdayYear=today.year+1
	else:
		nextBirthdayYear=today.year

	nextBirthday= dt.date(nextBirthdayYear,birthDay_obj.month,birthDay_obj.day)

	print("next birthday:",nextBirthday)
	diff=nextBirthday-today
	print("remaining days for the next birthday:",diff.days)
else:
	#new nic
	year=nic[0:4]
	day=int(nic[4:7])
	if day<500:
		print("gender is male")
	else:
		print("gender is female")
		day=day-500
	if int(year)%4!=0:
		if int(year):
			if(day<=31):
				month="01"
				date=day
			elif(day<=60):
				month="02"
				date=day-31
			elif(day<=91):
				month="03"
				date=day-60
			elif(day<=121):
				month="04"
				date=day-91
			elif(day<=152):
				month="05"
				date=day-121
			elif(day<=182):
				month="06"
				date=day-152
			elif(day<=213):
				month="07"
				date=day-182
			elif(day<=244):
				month="08"
				date=day-213
			elif(day<=274):
				month="09"
				date=day-244
			elif(day<=305):
				month="10"
				date=day-274
			elif(day<=335):
				month="11"
				date=day-305
			elif(day<=366):
				month="12"
				date=day-335
			birthDay=(year+"-"+month+"-"+str(date))
	else:
		if int(year):
			if(day<=31):
				month="01"
				date=day
			elif(day<=60):
				month="02"
				date=day-31
			elif(day<=91):
				month="03"
				date=day-60
			elif(day<=121):
				month="04"
				date=day-91
			elif(day<=152):
				month="05"
				date=day-121
			elif(day<=182):
				month="06"
				date=day-152
			elif(day<=213):
				month="07"
				date=day-182
			elif(day<=244):
				month="08"
				date=day-213
			elif(day<=274):
				month="09"
				date=day-244
			elif(day<=305):
				month="10"
				date=day-274
			elif(day<=335):
				month="11"
				date=day-305
			elif(day<=366):
				month="12"
				date=day-335
	birthDay=(year+"-"+month+"-"+str(date))
	print("birthday:", birthDay)

	today=dt.date.today()

	birthDay_type=(year+"-"+month+"-"+str(date))
	birthDay_obj= dt.datetime.strptime(birthDay_type,"%Y-%m-%d")
	if(today.month==birthDay_obj.month and today.day>=birthDay_obj.day or today.month>birthDay_obj.month):
		nextBirthdayYear=today.year+1
	else:
		nextBirthdayYear=today.year

	nextBirthday= dt.date(nextBirthdayYear,birthDay_obj.month,birthDay_obj.day)

	print("next birthday:",nextBirthday)
	diff=nextBirthday-today
	print("remaining days for the next birthday:",diff.days)
