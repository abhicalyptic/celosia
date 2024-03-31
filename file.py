import requests

def remove_dead_urls(input_file):
    # Open the input file for reading
    with open(input_file, "r") as file:
        # Read all lines from the input file
        urls = file.readlines()
    
    # Open the input file again for writing
    with open(input_file, "w") as file:
        # Iterate through each URL in the list
        for url in urls:
            # Remove leading and trailing whitespaces, including newline characters
            url = url.strip()
            
            # Send a GET request to the URL
            response = requests.get(url)
            
            # Check if the response status code is 200 (OK)
            if response.status_code == 200:
                # If the URL is alive, write it back to the input file
                file.write(url + '\n')

# example
inp = r"C:\Users\abhiy\Desktop\gitGithub\celosia\sources\wallhaven\sources.txt"

remove_dead_urls(inp)
