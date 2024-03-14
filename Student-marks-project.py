print("\n\n Welcome to Student Marks Project\n\n")

tel=float(input("Enter Telugu Subject Marks: "))
eng=float(input("Enter English Subject Marks: "))
mat=float(input("Enter Maths Subject Marks: "))
sci=float(input("Enter Science Subject Marks: "))
soc=float(input("Enter Soc Subject Marks: "))
hin=float(input("Enter Hindi Subject Marks: "))




print("\n\n\n\n-------------------------------------------------------------------")
print("\n\n Scored Subjects ")

print("\n The Telugu Subject Marks are ",tel)
print("\n The English Subject Marks are ",eng)
print("\n The Maths Subject Marks are ",mat)
print("\n The Science Subject Marks are ",sci)
print("\n The Social Subject Marks are ",soc)
print("\n The Hindi Subject Marks are ",hin)




print("\n\n\n\n-------------------------------------------------------------------")
print("\nTotal Marks on 6 Subjects")

tot=tel+eng+mat+sci+soc+hin 
print ("\n\n The Total Six Subject Marks are: ",tot)





print("\n\n\n\n-------------------------------------------------------------------")
print("\n Average Marks")
avg=tot/6
print ("\n The Six Subjects Average Marks are: ",avg)



print("\n\n\n\n\n-------------------------------------------------------------------")
print("\n\n Highest Marks Subjects")
if(tel>eng and tel>mat and tel>sci and tel>soc and tel>hin):
	print("\n The Telugu Subject Marks are Highest in Given Six Subjects: ",tel)

elif(eng>tel and eng>mat and eng>sci and eng>soc and eng>hin):
	print("\n The English Subject Marks are Highest in Given Six Subjects: ",eng)

elif(mat>tel and mat>eng and mat>sci and mat>soc and mat>hin):
	print("\n The Maths Subject Marks are Highest in Given Six Subjects: ",mat)

elif(sci>tel and sci>eng and sci>mat and sci>soc and sci>hin):
	print("\n The Science Subject Marks are Highest in Given Six Subjects: ",sci)

elif(soc>tel and soc>eng and soc>mat and soc>sci and soc>hin):
	print("\n The Social Subject Marks are Highest in Given Six Subjects: ",soc)

elif(hin>tel and hin>eng and hin>mat and hin>sci and hin>soc):
	print("\n The Hindi Subject Marks are Highest in Given Six Subjects: ",hin)		



print("\n\n\n\n\n-------------------------------------------------------------------")
print("\n\n Lowest Marks Subjects")
if(tel<eng and tel<mat and tel<sci and tel<soc and tel<hin):
	print("\n The Telugu Subject Marks are Lowest in Given Six Subjects: ",tel)

elif(eng<tel and eng<mat and eng<sci and eng<soc and eng<hin):
	print("\n The English Subject Marks are Lowest in Given Six Subjects: ",eng)

elif(mat<tel and mat<eng and mat<sci and mat<soc and mat<hin):
	print("\n The Maths Subject Marks are Lowest in Given Six Subjects: ",mat)

elif(sci<tel and sci<eng and sci<mat and sci<soc and sci<hin):
	print("\n The Science Subject Marks are Lowest in Given Six Subjects: ",sci)

elif(soc<tel and soc<eng and soc<mat and soc<sci and soc<hin):
	print("\n The Social Subject Marks are Lowest in Given Six Subjects: ",soc)

elif(hin<tel and hin<eng and hin<mat and hin<sci and hin<soc):
	print("\n The Hindi Subject Marks are Lowest in Given Six Subjects: ",hin)	



print("\n\n\n\n-------------------------------------------------------------------")
print("\n\n Failed Subjects")

if(tel<35):
	print("\n Failed in Telugu Subject ",tel)

if(eng<35):
	print("\n Failed in English Subject ",eng)

if(mat<35):
	print("\n Failed in Maths Subject ",mat)

if(sci<35):
	print("\n Failed in Science Subject ",sci)

if(soc<35):
	print("\n Failed in Social Subject ",soc)

if(hin<35):
	print("\n Failed in Hindi Subject ",hin)




