# https://scontent.fdad3-1.fna.fbcdn.net/v/t39.30808-6/433678591_122133547184115447_8305999576824315900_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=5f2048&_nc_ohc=oQNMD1aZ8aYAb5doXeQ&_nc_ht=scontent.fdad3-1.fna&oh=00_AfBstWQ6RJnVUdCEdNuS9sPzCVdKwBFmlV7p1ngkVGeLww&oe=661540D6

def update_customer_details(account_number):
  updated_customer_details = []
  
  with open(CUSTOMER_DATA_FILE, 'r+') as file:
    lines =  file.readlines()
    file.seek(0)
    for line in lines:
      parts = line.strip().split('|')
      if len(parts) >= 6 and parts[2] == account_number:
        display_customer_details(parts)
        
        updated_customer_number = get_updated_customer_numbers(parts)
