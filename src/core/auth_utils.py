def check_email_valid(email):
  return True

def check_duplicated(list, item):
  return True if item in list else False

def check_password_valid(password):
  return True

def format_id(str_len, new_id):
  new_id_str = str(new_id)
  new_id_len = len(new_id_str)
  if new_id_len > str_len:
    return None
 
  return '0' * (str_len - new_id_len) + new_id_str