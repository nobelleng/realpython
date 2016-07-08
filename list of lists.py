def enrollment_stats(uni_stats):
    total_student=[]
    total_fee=[]
    count=0
    for stats in uni_stats:
        total_student.append(stats[1])
        total_fee.append(stats[2])
        count+=1
    return total_student, total_fee, count

def mean(uni_list):
    student_total=0
    fee_total=0
    newlist = enrollment_stats(uni_list)
    for n in range(0,newlist[2]):
        student_total = student_total + newlist[0][n]
        fee_total = fee_total + newlist[1][n]
    student_mean = student_total/newlist[2]
    fee_mean = fee_total/newlist[2]
    return student_total, fee_total, int(student_mean), int(fee_mean)
        

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]


print (mean(universities))

print ("********************************")
print ("Total Students: ", mean(universities)[0])
print ("********************************")
