waits =[
    {"wait_type":"LCK_M_X","duration":20},
    {"wait_type":"PAGEIOLATCH_SH","duration":60},
    {"wait_type":"CXPACKET","duration":140}
]

def analyze_wait(wait_list):
    waits_results=[]

    for wait in wait_list:
        try:
            duration=wait["duration"]
        except KeyError:
            print("invalid wait entry:",wait)
            continue
        waits_results.append(wait)
    return waits_results

def analyze_wait_high(wait_list):
    high_waits=[]

    for wait in wait_list:

        if wait["duration"] > 100:
            high_waits.append(wait)

    return high_waits

def total_high_wait_duration(wait_list):
    duration_waits=0
    total=0
    for wait in wait_list:
       # duration_waits=wait.get("duration",0)
        duration_waits=wait["duration"]
        total = total + int(duration_waits)
    return total

def count_of_high_waits(wait_list):
    return len(wait_list)

def severity_level_threshold(wait_list):
    wait_duration = 0
    counts = {"total_waits":0,"High": 0, "Medium": 0, "Low": 0}
    
    for wait in wait_list:
    
        wait_duration=wait["duration"]

        if wait_duration >=100:
            counts["High"] +=1
        elif wait_duration >=50:
            counts["Medium"] +=1
        else:
            counts["Low"]+=1

    counts["total_waits"] +=len(wait_list)
    return counts

result=analyze_wait(waits)
    
high_waits=analyze_wait_high(result)
if len(high_waits) == 0:
        print ("System Is Healthy") 
else:
        print ("Hight waits deteched:")
        for r in high_waits:
            print (r)

total_high_wait_duration_result=total_high_wait_duration(result)
print("Total wait Duration in Sec :" ,total_high_wait_duration_result)
    
count_of_high_wait=count_of_high_waits(result)
print("Count of High Waits:",count_of_high_wait)

slt=severity_level_threshold(result)
print("Wait_Summary :",slt)