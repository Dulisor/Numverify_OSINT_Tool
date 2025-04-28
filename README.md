# Numverify OSINT Tool

![NUMVERIFY-TOOL](https://github.com/user-attachments/assets/e02e988a-af39-41a2-b119-1553a6038cea)



## Overview

This Python program validates phone numbers using the Numverify API. It allows users to input a phone number (including the country code), and then fetches and displays various details about the phone number such as its validity, country, carrier, and format.

## Features

- Validate a phone number with a given country code.
- Retrieve details like the number’s validity, local and international formats, country of origin, and more.
- Error handling for invalid API requests.

## Requirements

- Python 3.x
- `requests` library (to make API calls)

To install the required library, run the following command:
```
pip install -r requirements.txt
```

## Setup

1. Clone or download the repository.
2. Replace `api_key` in the script with your own valid API key from the Numverify API. You can get an API key by signing up on [Numverify](https://numverify.com/).
3. Ensure you have Python installed on your system.
4. Run the script from the command line.

## Usage

Run the program by executing the Python script:

```bash
python numverify_osint_tool.py
```

You will be prompted to input a phone number with the country code (e.g., `+14158586273`). After input, the program will return various details about the phone number, such as:

- **Number**: The phone number.
- **Valid**: Whether the phone number is valid or not.
- **Local Format**: The phone number in a local format.
- **International Format**: The phone number in an international format.
- **Country Prefix**: The international dialing prefix for the country.
- **Country Code**: The numeric country code.
- **Country Name**: The country of origin for the phone number.
- **Location**: The location of the phone number.
- **Carrier**: The telecom carrier of the number.
- **Line Type**: The type of phone line (e.g., mobile, landline).

## Note

Before using the tool specify your Numverify API key:

```bash
export NUMVERIFY_API_KEY="your_actual_api_key_here"
```


## Example Output

```
Enter the phone number to validate (with country code, e.g., +14158586273): +14158586273

Phone Number Details:
Number: +14158586273
Valid: true
Local Format: (415) 858-6273
International Format: +14158586273
Country Prefix: +1
Country Code: US
Country Name: United States
Location: California
Carrier: T-Mobile USA, Inc.
Line Type: mobile
```

## Error Handling

If there is an issue with the API request (e.g., invalid API key, no internet connection), the program will output an error message indicating the status code or the specific problem.

Example of error:
```
Failed to retrieve data. Status code: 401
```

## License

This project is licensed under the GNU General Public License.

