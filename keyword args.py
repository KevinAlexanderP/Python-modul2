# Define create_spreadsheet():
def create_spreadsheet(title,row_count=1000):
  print("Creating a spreadsheet called "+title+"with "+str(row_count)+" rows ")

# Call create_spreadsheet() below with the required arguments:
create_spreadsheet("Downloads")
create_spreadsheet("Applications",10)

def divide_by_four(input_number):
    return input_number/4
    result = divide_by_four(16)
# result now holds 4
print("16 divided by 4 is " + str(result) + "!")
result2 = divide_by_four(result)
print(str(result) + " divided by 4 is " + str(result2) + "!")

def create_special_string(special_item):
    return "Our special is " + special_item + "."

special_string = create_special_string("banana yogurt")

print(special_string)

# Our special is banana yogurt.

## CALCULATE AGE FUNCTION 
def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age

my_age= calculate_age(2049, 1993)
dads_age= calculate_age(2049,1053)


## multiple return values 

def square_points(x_value,y_value):
    x_2=x_value * x_value
    y_2= y_value * y_value
    return x_2, y_2

x_squared, y_squared = square_point(1, 3)
print(x_squared)
print(y_squared)

## output 1,9

## SCOPE 
def create_special_string(special_item):
    return "Our special is " + special_item + "."

## IF WE TRY TO ACCES TO LOCAL SCOPE, WILL GET NAME ERROR
## THE GLOBAL SCOPE IS

