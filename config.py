import os
import ast
# Copy channel id from discord
channel_id = os.environ.get('CHANNEL_ID')
if channel_id == None:
  channel_id = "765221940667219988"
else:
  print(channel_id)
# 765221940667219988 for simpletown casino

# next collect cooldown time
cooldown_time = 30

# some casino bots take time to recieve next command or slowmode
wait_duration = 1

# change commands to True to if you want to enable it
# Note: crime and slut command can give you huge fine
# if you have a huge amount in casino
try:
  crime = ast.literal_eval(os.environ.get('CRIME'))
  slut = ast.literal_eval(os.environ.get('SLUT'))
  work = ast.literal_eval(os.environ.get('WORK'))
except Exception:
  crime = True
  slut = True
  work = True
