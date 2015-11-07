def min_bef(hh,mm,pm):
	if (pm==0) and hh==12:
		return 1440 
	elif (pm==1):
		if(hh<12):
			hh += 12		
	mm = 60-mm
	return ((24-(hh+1))*60)+mm
	
def min_aft(hh,mm,pm):
	if (pm==0) and hh==12:
		return 0 
	elif (pm==1):
		if(hh<12):
			hh += 12
	return (hh*60)+mm
	
def CountingMinutesI(sen):
	sen = sen.replace('M','')
	sen = sen.replace(':',' ')
	sen = sen.replace('P',' 1')
	sen = sen.replace('A',' 0')
	lit = sen.split("-")
	lit = lit[0].split(" ")	+lit[1].split(" ")
	lita=[]
	for i in lit:
		lita.append(int(i))	
	#print lita
	
	if(lita[2] == lita[5]):
		res = min_bef(lita[0],lita[1],lita[2])-min_bef(lita[3],lita[4],lita[5])
		if res <0 :
			return 1440+res
		else:
			return res
	elif(lita[2] < lita[5]):
		return min_bef(lita[0],lita[1],lita[2])-min_bef(lita[3],lita[4],lita[5])
	elif(lita[2] > lita[5]):
		return min_bef(lita[0],lita[1],lita[2])+min_aft(lita[3],lita[4],lita[5])

def sort_times(times):
	ams = []
	pms = []
	for i in times:
		if i[5].lower()	== 'p' and int(i[0:2])<12:
			pms.append(i)
		else:
			ams.append(i)		
	full = sort_timeList(ams)+sort_timeList(pms)
	return full
	
def sort_timeList(times):
	sortedTimes = sorted(times, cmp=make_comparator(less_than), reverse=False)#[::-1]
	return sortedTimes			

def less_than(x, y):	
	if(int(x[0:2]) < int(y[0:2])):	
		#print int(x[0:2]),int(y[0:2])
		return True
	elif (int(x[3:5]) < int(y[3:5])):
		#print int(x[3:5]),int(y[3:5])
		return True
	else:
		return False		
			
def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        else:
            return 0
    return compare

def MostFreeTime(times):
	times = sort_times(times) 
	#print times
	maxt = 0
	for i in range (0,len(times)-1):
		free = times[i][8:]+"-"+times[i+1][:7]
		maxt = max(maxt,CountingMinutesI(free))
		#print maxt	
	#print "FInal result: "+str(maxt	)
	return str(maxt/60).zfill(2) +":"+str(maxt%60).zfill(2) 
    
    
sen = ["12:15PM-02:00PM","09:00AM-12:11PM","02:02PM-04:00PM"]
# keep this function call here  
# to see how to enter arguments in Python scroll down
print MostFreeTime(sen)  


		
