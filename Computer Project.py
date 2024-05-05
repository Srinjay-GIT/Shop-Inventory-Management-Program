import csv

print ( 'Welcome Sir!! How can I help you??' )                                                                                        # Menu Interface
print()
print ( 'Press 1 to insert a product information.' )
print ( 'Press 2 to delete information of a product.' )
print ( 'Press 3 to update the price of a product.' )
print ( 'Press 4 to update the quantity of a product.' )
print ( 'Press 5 to display all the informaton of a product.' )
print ( 'Press 6 to display the current quantity of a product.' )
print ( 'Press Enter to quit.' )
print ()

while True:
      choice = input ( 'Enter your choice : ')

      if choice == '1':                                                                                                                                # 1st choice
            l1 = []
            prod_id = input ( 'Enter a unique 4 digit product id : ')                                             # Taking information
            name = input ( 'Enter product name : ' )                                                                  #  about the product
            price = input ( 'Enter unit price of your product : ' )                                               
            qnty = input ( 'Enter quantity of the product : ' )
            l1 = [prod_id,name,price,qnty]
            f = open ( 'Shop Inventory.csv', 'a', newline = '')                                                       # Opening the file in append mode
            csv_w = csv.writer(f,delimiter = ',')                                         
            csv_w.writerow(l1)                                                                                                 # Writing the records taken
            f.close()                                                                                                                 # Closing the file
            print ( 'Record added successfully.' )

      elif choice == '2':                                                                                                                              # 2nd choice
            delete_id = input ( 'Enter the id of the product to be deleted : ')                              # Information taken
            f = open ( 'Shop Inventory.csv', 'r')                                                                          # Opening the file reading mode
            csv_r = csv.reader(f)
            l1 = []
            l2 = []
            for row in csv_r :                                                                                                   # Using loop for extracting and  
                  l1.append(row)                                                                                                # editing data
            for i in range(1,len(l1)):
                  if l1[i][0] != delete_id:
                        l2.append(l1[i])
            f.close()                                                                                                                 # File closed
            f = open ( 'Shop Inventory.csv', 'w', newline = '')                                                      # File reopened in writing mode
            csv_w = csv.writer(f,delimiter = ',')
            csv_w.writerow(['Prod_Id','Prod_Name','Price','Qnty'])
            csv_w.writerows(l2)                                                                                               # New records written
            f.close()
            print ( 'Record deleted.' )

      elif choice == '3':                                                                                                                             # 3rd choice
            prod_id = input ( 'Enter the id of the product whose price is to be updated : ')       
            updt_price = input ( 'Enter the updated price : ') 
            f = open ( 'Shop Inventory.csv', 'r')                                                                          # File opened in reading mode
            csv_r = csv.reader(f)
            l1 = []
            l2 = []
            for row in csv_r :
                  if row[0] == prod_id:                                                                                       # List slicing is used to change
                        row[2] = updt_price                                                                                  # the price of the product
                  l1.append(row)
            for i in range(1,len(l1)):
                  l2.append(l1[i])
            f.close()
            f = open ( 'D:/Bonny/PYTHON/Shop Inventory.csv', 'w', newline = '')
            csv_w = csv.writer(f,delimiter = ',')
            csv_w.writerow(['Prod_Id','Prod_Name','Price','Qnty'])
            csv_w.writerows(l2)                                                                                              # The data is rewritten along with  
            f.close()                                                                                                               # the new price and file is closed
            print ( 'Price updated.')

      elif choice == '4':                                                                                                                             # 4th choice
            prod_id = input ( 'Enter the id of the product whose quantity is to be updated : ')   
            updt_qnty = input ( 'Enter new quantity : ')
            f = open ( 'Shop Inventory.csv', 'r')                                                                         # File opened in reading mode
            csv_r = csv.reader(f)                                                                                             
            l1 = []
            l2 = []
            for row in csv_r :                                                                                                   # The process of choice 3 is repeated
                  if row[0] == prod_id:
                        row[3] = updt_qnty
                  l1.append(row)
            for i in range(1,len(l1)):                                                                                         # The quantity of the product
                  l2.append(l1[i])                                                                                                # is updated
            f.close()
            f = open ( 'Shop Inventory.csv', 'w', newline = '')
            csv_w = csv.writer(f,delimiter = ',')
            csv_w.writerow(['Prod_Id','Prod_Name','Price','Qnty'])
            csv_w.writerows(l2)
            f.close()
            print ( 'Quantity updated.')

      elif choice == '5':                                                                                                                             # 5th choice
            prod_id = input ( 'Enter the id of the product whose information you are searching for : ')
            f = open ( 'Shop Inventory.csv', 'r')                                                                                     # File opened in reading mode
            csv_r = csv.reader(f)
            l= []
            for row in csv_r :                                                                                                              # Extracting all the values 
                  if row[0] == prod_id:
                        l = row
            print ('Here is the product you are looking for ---' )
            print ('Prod_Id : ',l[0])
            print ('Prod_Name : ',l[1])
            print ('Price : ',l[2])
            print ('Quantity : ',l[3])
            f.close()

      elif choice == '6':                                                                                                                             # 6th choice
            prod_id = input ( 'Enter the id of the product whose quantity you are searching for : ')
            f = open ( 'Shop Inventory.csv', 'r')                                                                                   # The pocess of choice 5
            csv_r = csv.reader(f)                                                                                                       # is repeated
            l= []
            for row in csv_r :
                  if row[0] == prod_id:
                        l = row
            print ('You have',l[3],l[1],'left.')
            f.close()

      elif choice == '':                                                                                                                              # Exit
            break
print ( 'Thank you.' )
      
            
            
            
            
            
            
      
