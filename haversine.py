

from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):
	# convert decimal degrees to radians
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

	# haversine formula
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a))
	r = 3956 # Radius of earth.  Use 3956 for miles or 6371 for km
	return c * r


