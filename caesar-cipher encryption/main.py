alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

run_condition = True
while run_condition:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift%26
  

  
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
  def encrypt(text_value,shift_value):
    display = ""
    for each_letter in text_value:
      if each_letter in alphabet:
        letter_position = alphabet.index(each_letter)
        shift_position = letter_position + shift_value
        new_letter = alphabet[shift_position]
        display += new_letter
      else:
        display += each_letter
    print(f"The encoded text is '{display}'")
    
  
  def decrypt (text_de,shift_de):  
    display_decrypt = ""
    for letter in text_de:
      if letter in alphabet:
        position_of_letter = alphabet.index(letter)
        left_position = position_of_letter - shift_de
        letter_shift = alphabet[left_position]
        display_decrypt += letter_shift
      else:
        display_decrypt += letter
    print(f"The decode text is '{display_decrypt}'")
  
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
  if direction == "encode":
    encrypt(text_value=text, shift_value=shift)
  elif direction == "decode":
    decrypt(text_de=text,shift_de=shift)
  else:
    print("Wrong input, type 'encode' or 'decode'")
  print("\n")
  stop_loop = input('Do you want to continue? Yes or No: ').lower()
  print("\n")
  if stop_loop == "no":
    run_condition = False
    print("Thank you!!! Bye")