
import datetime 

# ---------------------------------------------------------------------------------------------------------------------

#! List of Class Methods of Specific Classes : 
datetime_date_list = ("ctime","day","fromisocalendar","fromisoformat","fromordinal","fromtimestamp","isocalendar","isoformat","isoweekday","max","min","month","replace","resolution",
"strftime","timetuple","today","toordinal","weekday","year") 

datetime_datetime_list = ("astimezone","combine","ctime","date","day","dst","fold","fromisocalendar","fromisoformat","fromordinal","fromtimestamp","hour",
"isocalendar","isoformat","isoweekday","max","microsecond","min","minute","month","now","replace","resolution","second","strftime","strptime","time","timestamp","timetuple","timetz","today","toordinal","tzinfo","tzname",
"utcfromtimestamp","utcnow","utcoffset","utctimetuple","weekday","year")

datetime_time_list = ("dst","fold","fromisoformat","hour","isoformat","max",
"microsecond","min","minute","replace","resolution","second","strftime","tzinfo","tzname","utcoffset")

datetime_timedelta_list = ("days","max","microseconds","min","resolution","seconds","total_seconds")

datetime_tzinfo_list = ("dst","fromutc","tzname","utcoffset")

datetime_timezone_list = ("dst","fromutc","max","min","tzname","utc","utcoffset")

# ---------------------------------------------------------------------------------------------------------------------

#! List of Class Methods Info of Specific Classes : 
from file_for_datetime_classes import date as d
from datetime import date
datetime_date_info = (date.ctime.__doc__,date.day.__doc__,date.fromisocalendar.__doc__,date.fromisoformat.__doc__,date.fromordinal.__doc__,date.fromtimestamp.__doc__,d.isocalendar.__doc__,date.isoformat.__doc__,date.isoweekday.__doc__,date.max.__doc__,date.min.__doc__,date.month.__doc__,date.replace.__doc__,date.resolution.__doc__,
date.strftime.__doc__,date.timetuple.__doc__,date.today.__doc__,date.toordinal.__doc__,date.weekday.__doc__,date.year.__doc__) 

from datetime import datetime
datetime_datetime_info = (datetime.astimezone.__doc__,datetime.combine.__doc__,datetime.ctime.__doc__,datetime.date.__doc__,datetime.day.__doc__,datetime.dst.__doc__,datetime.fold.__doc__,datetime.fromisocalendar.__doc__,datetime.fromisoformat.__doc__,datetime.fromordinal.__doc__,datetime.fromtimestamp.__doc__,datetime.hour.__doc__,datetime.isocalendar.__doc__,datetime.isoformat.__doc__,datetime.isoweekday.__doc__,datetime.max.__doc__,datetime.microsecond.__doc__,datetime.min.__doc__,datetime.minute.__doc__,datetime.month.__doc__,datetime.now.__doc__,datetime.replace.__doc__,datetime.resolution.__doc__,datetime.second.__doc__,datetime.strftime.__doc__,datetime.strptime.__doc__,datetime.time.__doc__,datetime.timestamp.__doc__,datetime.timetuple.__doc__,datetime.timetz.__doc__,datetime.today.__doc__,datetime.toordinal.__doc__,datetime.tzinfo.__doc__,datetime.tzname.__doc__,datetime.utcfromtimestamp.__doc__,datetime.utcnow.__doc__,datetime.utcoffset.__doc__,datetime.utctimetuple.__doc__,datetime.weekday.__doc__,datetime.year.__doc__)

from datetime import time
datetime_time_info = (time.dst.__doc__,time.fold.__doc__,time.fromisoformat.__doc__,time.hour.__doc__,time.isoformat.__doc__,time.max.__doc__,time.microsecond.__doc__,time.min.__doc__,time.minute.__doc__,time.replace.__doc__,time.resolution.__doc__,time.second.__doc__,time.strftime.__doc__,time.tzinfo.__doc__,time.tzname.__doc__,time.utcoffset.__doc__)

from datetime import timedelta
datetime_timedelta_info = (timedelta.days.__doc__,timedelta.max.__doc__,timedelta.microseconds.__doc__,timedelta.min.__doc__,timedelta.resolution.__doc__,timedelta.seconds.__doc__,timedelta.total_seconds.__doc__)

from file_for_datetime_classes import tzinfo
datetime_tzinfo_info = (tzinfo.dst.__doc__,tzinfo.fromutc.__doc__,tzinfo.tzname.__doc__,tzinfo.utcoffset.__doc__)#!!!!!!!!! 

import datetime
from file_for_datetime_classes import timezone
datetime_timezone_info = (timezone.dst.__doc__,timezone.fromutc.__doc__,datetime.timezone.max.__doc__,datetime.timezone.min.__doc__,timezone.tzname.__doc__,datetime.timezone.utc.__doc__,timezone.utcoffset.__doc__)

# ---------------------------------------------------------------------------------------------------------------------

#! Making Tuples To use them in making of a zip object
 
#!  List of Classes Under Datetime Module : 
import datetime
datetime_all_classes_list = tuple(datetime.__all__)

#! Combined List of All Classes Info :  
datetime_all_classes_info = (datetime.date.__doc__,datetime.datetime.__doc__,datetime.time.__doc__,datetime.timedelta.__doc__,datetime.timezone.__doc__,datetime.tzinfo.__doc__,datetime.MINYEAR,datetime.MAXYEAR)

#! Combined List of Methods of all Classes : 
datetime_all_classes_methods_list = (datetime_date_list,datetime_datetime_list,datetime_time_list,datetime_timedelta_list,datetime_timezone_list,datetime_tzinfo_list,[],[])

#! Combined List of Method Info of all Classes : 
datetime_all_classes_methods_info = (datetime_date_info,datetime_datetime_info,datetime_time_info,datetime_timedelta_info,datetime_timezone_info,datetime_tzinfo_info,[],[])

# ---------------------------------------------------------------------------------------------------------------------

#! We make a zip object in which each element containing a tuple containing (class name , class info , class methods list , class methods info) 

a = zip(datetime_all_classes_list , datetime_all_classes_info , datetime_all_classes_methods_list , datetime_all_classes_methods_info)
b = tuple(a)