import requests
import os

print('''
    _   __                                     _  ____          ____  _____  ____ _   __ ______   ______               __
   / | / /__  __ ____ ___  _   __ ___   _____ (_)/ __/__  __   / __ \/ ___/ /  _// | / //_  __/  /_  __/____   ____   / /
  /  |/ // / / // __ `__ \| | / // _ \ / ___// // /_ / / / /  / / / /\__ \  / / /  |/ /  / /      / /  / __ \ / __ \ / / 
 / /|  // /_/ // / / / / /| |/ //  __// /   / // __// /_/ /  / /_/ /___/ /_/ / / /|  /  / /      / /  / /_/ // /_/ // /  
/_/ |_/ \__,_//_/ /_/ /_/ |___/ \___//_/   /_//_/   \__, /   \____//____//___//_/ |_/  /_/      /_/   \____/ \____//_/  v1.0
                                                   /____/                                                               Made by Dulisor''')

class NumverifyAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://apilayer.net/api/validate"            
    def validate_phone_number(self, phone_number):
        params = {
            'access_key': self.api_key,
            'number': phone_number,
            'format': 1
            }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve data. Status code: {response.status_code}"}

def main():
    api_key = os.getenv("NUMVERIFY_API_KEY")
    numverify = NumverifyAPI(api_key)
    while 1>0:
        phone_number = input("Enter the phone number to validate (with country code, e.g., +14158586273): ")
        result = numverify.validate_phone_number(phone_number)
        if 'error' in result:
            print(result['error'])
        else:
            print("\nPhone Number Details:")
            print(f"Number: {result.get('number')}")
            print(f"Valid: {result.get('valid')}")
            print(f"Local Format: {result.get('local_format')}")
            print(f"International Format: {result.get('international_format')}")
            print(f"Country Prefix: {result.get('country_prefix')}")
            print(f"Country Code: {result.get('country_code')}")
            print(f"Country Name: {result.get('country_name')}")
            print(f"Location: {result.get('location')}")
            print(f"Carrier: {result.get('carrier')}")
            print(f"Line Type: {result.get('line_type')}")
        con = input("\nThe programme has ended. Press \'Y\' if you want to run the programme again: ")
        if con == 'Y':
            continue
        else:
            break
if __name__ == "__main__":
    main()