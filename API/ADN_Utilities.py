'''
	Program:	ADN_Utilities.py, utilities used by my various App.Net related
					projects.

				Copyright (C) 2013 Dale Weber. ALL Rights Reserved. License to be chosen.

	Author:		Dale Weber <hybotics.pdx@gmail.com, @hybotics (App.Net and Twitter)>

	Version:	0.3.1 (Unstable)
	Date:		25-Nov-2013
	Purpose:	Preliminary, VERY ALPHA release

	Requires:	Python v3.3.1 or later
				PyTZ 2013b or later

'''

from datetime import datetime
from time import mktime, sleep, time

from Hybotics_Utils import getTimeZone

# You need the pytz 2013b version, or later
from pytz import utc, timezone

'''
	Parse a UTC creation date and convert it to local time. The timezone is read from
		/etc/timezone.  Returns a tuple of [date time timezone]. For instance, the Pacific
		timezone would have TZ=America/Los_Angeles . You really should have this set anyway. :)

		NOTICE: This ONLY handles the SPECIFIC case of creation dates that App.net uses.
'''
def local_datetime(iso_utc):
	local_tz = getTimeZone()
	local_timezone = timezone(local_tz)

	fmt = '%m/%d/%Y %I:%M%p %Z'

	stime = iso_utc.split("T")

	sdate = stime[0]
	stime = stime[1]
	stime = stime[0 : len(stime) - 1]

	sdate = sdate.split("-")
	stime = stime.split(":")

	zyear = int(sdate[0])
	zmonth = int(sdate[1])
	zday = int(sdate[2])

	zhours = int(stime[0])
	zminutes = int(stime[1])
	zseconds = int(stime[2])

	utc_datetime = datetime(zyear, zmonth, zday, zhours, zminutes, zseconds)
	utc_timestamp = mktime(utc_datetime.timetuple())
	utc_localized = utc.localize(datetime.fromtimestamp(utc_timestamp))
	local_dt = local_timezone.normalize(utc_localized.astimezone(local_timezone))

	# You get the Date, Time, and Timezone
	local = local_dt.strftime(fmt)

	return local.split(" ")

