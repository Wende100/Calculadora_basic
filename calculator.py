print("=====================================HELCOME_THE_CALCULATOR=======================================")

name_user=str(input("My Name:"))
print(f"===================================={name_user}=======================================")

number_1= int(input("Number: "))
number_2= int(input("Number: "))

def sum_c():
 return number_1 + number_2

def sub_c():
  return number_1 - number_2

def mult_c():
 return number_1 * number_2

def div_c():
 return number_1 / number_2


while True:
 opcao = int(input("\noptions aritmetics\nSum[1]:\nSub[2]:\nMult[3]:\nDiv[4]:\nBack_of_calculator[5]:\n"))

 if opcao==1:
   print("calculator..... result",sum_c())

 elif opcao==2:
  print(sub_c())

 elif opcao==3:
  print(mult_c())
  
 elif opcao==4:
  print(div_c())

 elif opcao ==5:
  print("back........")
  break