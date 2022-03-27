import time as q

#Enter Name in x variable

x="Dharmanshu"

b=len(x)
def cake():	
	print(" "*23,"\033[1;36mi  i  i  i")
	y=q.sleep(1)
	print(" "*23,"i  i  i  i")
	y=q.sleep(1)
	print(" "*21,"_ i  i  i  i_")
	y=q.sleep(1)
	print(" "*20,"|"," "*12,"|")
	y=q.sleep(1)
	print(" "*20,"|"," "*12,"|")
	y=q.sleep(1)
	print(" "*20,"|"," "*12,"|")
	y=q.sleep(1)
	print(" "*16,"-"*24)
	y=q.sleep(1)
	print(" "*16,"|"," "*20,"|")
	y=q.sleep(1)
	print(" "*16,"|"," "*int((20-b)/2),x," "*int((20-b)/2-2),"|")
	y=q.sleep(1)
	print(" "*16,"|"," "*20,"|")
	y=q.sleep(1)
	print(" "*16,"-"*24)


def menu():
	print()
	for i in range(4):
		if i==3:
			print(" "*13,"\033[1;35m  HAPPY HAPPY BIRTHDAY TO YOU")
		elif i==0 or i==1:
			print(" "*15,"\033[1;35mHAPPY BIRTHDAY TO YOU")
		elif i==2:
			print(" "*15,"\033[1;35mHAPPY BIRTHDAY","",x.upper(),"🎉🎉","\n")
		q.sleep(1.8)
		print()
	
def heart():
	for row in range(6):
		for col in range(7):
			if (row==0 and col %3 != 0)or(row==1 and col %3==0) or(row-col==2) or(row+col==8):
				print("💟",end=" ")
			else:
				print(end="  ")
		print()	
print("🎉"*5,"\033[1;5mBIRTHDAY WISHES FOR MY FRIEND👫",""+x.upper()+"*","🎉"*5)
q.sleep(1.5)
menu()
cake()

print(" "*14,"\033[33m\t\t\n\nMany Many Returns Of The Day\n \n\n".upper())
q.sleep(2)
x="Happy, healthy, exceptional, rocking birthday to you my friend!"
a=x.split()
for i in a:
	print("\t\t",i.title())
	q.sleep(1)
print("")
q.sleep(2)
print(" "*18,"\033[0;33m    god bless you".upper())
q.sleep(1)
print(" "*18,"\033[0;33m    my friend 😀\n\n".upper())
q.sleep(1)
heart()