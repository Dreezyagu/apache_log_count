import sys 
import re

def get_byte_size(log_entry):
  """
  Retrieves the byte size from a given log entry string.

  Args:
    log_entry: The log entry string.

  Returns:
    The byte size as an integer, or None if not found.
  """
  parts = log_entry.split()
  if len(parts) >= 9:
    try:
      byte_size = int(parts[-1])
      return byte_size
    except ValueError:
      pass
  return None

for line in sys.stdin: 
    # remove leading and trailing whitespace 
    line = line.strip() 
    size = get_byte_size(line)
    #get the domain name
    if size is not None:
        print('%s\t%s' % (size, 1))