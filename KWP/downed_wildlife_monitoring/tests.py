from datetime import date
import datetime

from django.test import TestCase

# Create your tests here.
from lookup_tables.models import *
from .models import *

import datetime
#Build lookup_tables


defaultSizeClass = SizeClass(size_txt = 'Hugemongous')
defaultStatus = Status(status_txt = 'sneaky')
defaultSpecies = SpeciesDef(common_name = 'Schmoo',
							scientific_name = 'Schmoo deliciousii',
							species_code = 'smoo',
							species_status = defaultStatus,
							size_class=defaultSizeClass)
defaultAge = Age(age_text = 'old AF')
defaultPlantSpecies = PlantSpecies(common_name = 'Money Tree',
									hawaiian_name = 'none',
									scientific_name = 'skrillicus maximus',
									status = 'no status',
									family = 'bankaceae',
									distribution = 'indigenous',
									notes = ''
									)
defaultDirection = Direction(direction_text = 'South',
							 direction_short = 'S',
							 direction_deg = 180)
defaultBait = Bait(bait_text = 'cat food')
defaultPersonnel = Personnel(first_name = 'Mr.',
							 last_name = 'T',
							 organization = 'Power Rangers',
							 initials = 'MT',
							 staff_type = 'Precious Metal Specialist',
							 hire_date = '1990-01-01',
							 phone = '111-11-11',
							 email = 'mr.t@twilight.com',
							 active = False)
defaultCanine = Canine(name = 'Ghost')

defaultSite = Site(locations = 'Area 51', short = 'a51')

defaultInfrastructure = Infrastructure(name='My House',
										physical_phase=defaultSite,
										phase=defaultSite)

defalutTrapType = TrapType(trap_type_text = "Chineese Finger",
							cost = '$50',
							check_frequency = '1')

defaultWeather = Weather(rain="soggy")

defaultNightSurvey_Behavior = NightSurvey_Behavior(behavior = "swooping")

defaultNightSurvey_Elevation = NightSurvey_Elevation(elevation = "below")

defaultNightSurvey_Distance = NightSurvey_Distance(distance_range = "10-20m")

defaultBandColor = BandColor(color_text = "Aqua")



defaultDWL = DownedWildlifeMonitoring(loc = '0101000020E6100000C5E6BD6F8F9163C0A272078CA1CF3440',
													 discovery_date= '2016-05-05',
													 discovered_by = defaultPersonnel ,
													 search_type= 'Visual' ,
													 search_incidental= 'Search' ,
													 affiliation = 'Pickles',
													 canine_searcher = defaultCanine,
													 species = defaultSpecies,
													 age = defaultAge,
													 sex =  'Male',
													 time_discovered = datetime.datetime.now(),
													 location_description = 'Next to turbine',
													 latitude = 2303177.0522595006,
													 longitude = 755132.3294488939,
													 site = defaultSite,
													 turbine = defaultInfrastructure,
													 distance = 1,
													 bearing = 1,
													 ground_cover = 'Shag carpet',
													 wind_dir = defaultDirection,
													 wind_speed = 0,
													 cloud_cover = 1,
													 cloud_deck = 'high',
													 precip = defaultWeather,
													 temp = 70,
													 animal_condition = 'Dead',
													 description = 'We found a pack of pickled peppers by the seashore',
													 collected_by = defaultPersonnel,
													 photo_structure = '',
													 photo_as_found = '',
													 photo_injury = '',
													 photo_other = '',
													 notes = '',
													 report_date = datetime.datetime.now(),
													 time_reported = datetime.datetime.now(),
													 time_responded = datetime.datetime.now(),
													 time_collected = datetime.datetime.now(),
													 date_last_searched = datetime.datetime.now(),
													 weather_TOD = 'Unknown',
													 outside = False)


class DownedWildlifeTestCase(TestCase):
	pass




	