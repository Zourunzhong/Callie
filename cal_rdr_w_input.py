from icalendar import Calendar
from icalendar import Event
from datetime import datetime
from datetime import timedelta
import sys
import json


test = '/Users/sherrywu1999/Desktop/untitled/callie/python/timetables/nusmods_calendar.ics'



def modify(x):
    #temp = datetime.strptime(str(x)[:-6], '%Y-%m-%d %H:%M:%S')
    temp = x + timedelta(days=7)
    return temp



def cal_rdr(file):
    file = open(file, 'rb')
    cal = Calendar.from_ical(file.read())

    big_dic= {}
    flist=[]

    for component in cal.walk():
        if component.name=='VEVENT':
            dic = {}

            name = str(component.get('summary'))
            start = component.get('dtstart').dt.replace(tzinfo=None)
            end = component.get('dtend').dt.replace(tzinfo=None)
            dur = end-start

            dic['title'] = str(name)
            dic['start'] = str(start)
            dic['end'] = str(end)
            dic['duration'] = int(dur.total_seconds() )

            flist.append(dic)

            if 'exam' in component['summary'].lower():
                pass
            else:

                for i in range(1,15):
                    dic2 = {}
                    
                    if i ==7:
                        pass
                    start =  modify(start)
                    end =  modify(end)

                    dic2['title'] = str(name)
                    dic2['start'] = str(start)
                    dic2['end'] = str(end)
                    dic2['duration'] = int( dur.total_seconds() )
                    
                    flist.append(dic2)

        
    big_dic['data'] = flist
    return big_dic



with open('/Users/sherrywu1999/Desktop/untitled/callie/python/timetables/caldr.json', 'w') as json_file:
    json.dump(cal_rdr(sys.argv[0]), json_file)
