import arrow
import logging
import re

def calculate_free(ordered_events, start_time, end_time):
	"""
	Calculate free times based on busy times.
	"""
	# start with full block
	start = arrow.get(start_time)
	end = arrow.get(end_time)
	free_times = [[start.isoformat(), end.isoformat()]]
	for event in ordered_events:
		
		e_start = arrow.get(event['start'])
		e_end = arrow.get(event['end'])

		new_free_times = []

		for free_time in free_times:
			
			na_free_start = free_time[0]
			na_free_end = free_time[1]
			free_start = arrow.get(na_free_start)
			free_end = arrow.get(na_free_end)
			# free block covers busy block
			if (e_start > free_start and e_end < free_end):
				# make 2 new time blocks
				time1 = [free_start.isoformat(), e_start.isoformat()]
				time2 = [e_end.isoformat(), free_end.isoformat()]
				new_free_times.append(time1)
				new_free_times.append(time2)
				
			# busy time overlaps free time
			elif (e_start < free_end and e_end > free_end):
				time = [free_start.isoformat(), e_start.isoformat()]
				new_free_times.append(time)

			elif (e_start < free_start and e_end > free_start):
				time = [e_end.isoformat(), free_end.isoformat()]
				new_free_times.append(time)

		free_times = new_free_times

	return free_times










