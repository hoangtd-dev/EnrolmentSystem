def format_id(str_len, new_id):
  new_id_str = str(new_id)
  new_id_len = len(new_id_str)

  if new_id_len > str_len:
    return None
 
  return int('0' * (str_len - new_id_len) + new_id_str)