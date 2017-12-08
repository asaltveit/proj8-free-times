from free_times import calculate_free
import nose    # Testing framework
import logging


def test_free_cover():
	"""
	Free block covers busy block.
	"""
	busy_times = [{ 'start': '2017-11-09T10:00:00-08:00', 'end': '2017-11-09T11:20:00-08:00'}]
	start_time = '2017-11-09T08:00:00-08:00'
	end_time = '2017-11-09T12:00:00-08:00'
	free_times = [['2017-11-09T08:00:00-08:00', '2017-11-09T10:00:00-08:00'], ['2017-11-09T11:20:00-08:00', '2017-11-09T12:00:00-08:00']]

	assert calculate_free(busy_times, start_time, end_time) == free_times

def test_no_overlap():
	"""
	Busy block does not over lap free block.
	"""
	busy_times = [{ 'start': '2017-11-09T10:00:00-08:00', 'end': '2017-11-09T11:20:00-08:00'}]
	start_time = '2017-11-09T08:00:00-08:00'
	end_time = '2017-11-09T09:00:00-08:00'
	free_times = [['2017-11-09T08:00:00-08:00', '2017-11-09T09:00:00-08:00']]

	assert calculate_free(busy_times, start_time, end_time) == free_times

def test_start_overlap():
	"""
	End of busy block overlaps start of free block.
	"""
	busy_times = [{ 'start': '2017-11-09T08:00:00-08:00', 'end': '2017-11-09T12:00:00-08:00'}]
	start_time = '2017-11-09T10:00:00-08:00'
	end_time = '2017-11-09T14:00:00-08:00'
	free_times = [['2017-11-09T12:00:00-08:00', '2017-11-09T14:00:00-08:00']]

	assert calculate_free(busy_times, start_time, end_time) == free_times

def test_end_overlap():
	"""
	Start of busy block overlaps end of free block.
	"""
	busy_times = [{ 'start': '2017-11-09T12:30:00-08:00', 'end': '2017-11-09T16:00:00-08:00'}]
	start_time = '2017-11-09T10:00:00-08:00'
	end_time = '2017-11-09T14:00:00-08:00'
	free_times = [['2017-11-09T10:00:00-08:00', '2017-11-09T12:30:00-08:00']]

	assert calculate_free(busy_times, start_time, end_time) == free_times

def test_all_overlap():
	"""
	Busy block totally covers free block.
	"""
	busy_times = [{ 'start': '2017-11-09T12:30:00-08:00', 'end': '2017-11-09T16:00:00-08:00'}]
	start_time = '2017-11-09T12:30:00-08:00'
	end_time = '2017-11-09T16:00:00-08:00'
	free_times = []

	assert calculate_free(busy_times, start_time, end_time) == free_times

def test_two_blocks():
	"""
	Tests a list of two busy times.
	"""
	busy_times = [{ 'start': '2017-11-09T10:00:00-08:00', 'end': '2017-11-09T11:00:00-08:00'}, {'start': '2017-11-09T12:30:00-08:00', 'end': '2017-11-09T13:00:00-08:00'}]
	start_time = '2017-11-09T10:30:00-08:00'
	end_time = '2017-11-09T16:00:00-08:00'
	free_times = [['2017-11-09T11:00:00-08:00' , '2017-11-09T12:30:00-08:00'], ['2017-11-09T13:00:00-08:00', '2017-11-09T16:00:00-08:00']]

	assert calculate_free(busy_times, start_time, end_time) == free_times

def test_multiple_blocks():
	"""
	Tests a list of multiple busy times.
	"""
	busy_times = [
	{'start': '2017-11-09T10:00:00-08:00', 'end': '2017-11-09T12:00:00-08:00'}, 
	{'start': '2017-11-09T12:30:00-08:00', 'end': '2017-11-09T13:00:00-08:00'}, 
	{'start': '2017-11-09T08:00:00-08:00', 'end': '2017-11-09T09:00:00-08:00'},
	{'start': '2017-11-09T15:00:00-08:00', 'end': '2017-11-09T18:00:00-08:00'}
	]
	start_time = '2017-11-09T09:00:00-08:00'
	end_time = '2017-11-09T16:00:00-08:00'
	free_times = [['2017-11-09T09:00:00-08:00', '2017-11-09T10:00:00-08:00'], ['2017-11-09T12:00:00-08:00', '2017-11-09T12:30:00-08:00'], ['2017-11-09T13:00:00-08:00', '2017-11-09T15:00:00-08:00']]

	assert calculate_free(busy_times, start_time, end_time) == free_times

