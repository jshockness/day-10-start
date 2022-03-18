# Functions Outputs

def format_name(f_name, l_name):
  """Takes first and last name and format it to return the title case verison of the name."""
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  first = f_name.title()
  last = l_name.title()
  return f"{first} {last}"

print(format_name(input("What is your first name? :"), input("What is your last name? :")))

