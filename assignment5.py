user_file = input('Input the name of your file to read: ')
output_file = "word_count.txt"  

try:
  with open(user_file, 'r') as file:
      word_count = 0
      for line in file:
          word_count += len(line.split())

  
  with open(output_file, 'w') as output_file:
      output_file.write(f"There are {word_count} words in the file.")

  print(f"Word count written to '{output_file}'.")
except FileNotFoundError:
  print(f"Error: File '{user_file}' not found.")




