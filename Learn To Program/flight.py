def report_status(scheduled_time, estimated_time):
  '''(number, number) -> str

  Report status of flight(on time, early, delayed)
  which has to arrive at scheduled time but now will
  arrive at estimated time.

  Pre-condition: 0.0 <= scheduled_time < 24 and
  0.0 <= estimated_time < 24

  >>> report_status(14.0, 14.0)
  'on time'
  >>> report_status(12.5, 12.0)
  'early'
  >>> report_status(9.0, 11.0)
  'delayed'
  '''
  if scheduled_time == estimated_time:
    return 'on time'
  elif scheduled_time > estimated_time:
    return 'early'
  else:
    return 'delayed'
