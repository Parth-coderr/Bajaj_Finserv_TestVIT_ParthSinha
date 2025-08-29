from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def get_user_id(full_name, dob):
    return f"{full_name.lower()}_{dob}"

def alternating_caps(s):
    result = ''
    upper = True
    for c in s[::-1]:
        if c.isalpha():
            result += c.upper() if upper else c.lower()
            upper = not upper
    return result

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        data = request.json.get("data", [])
        full_name = "john_doe"
        dob = "17091999"
        email = "john@xyz.com"
        roll_number = "ABCD123"

        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        numbers_sum = 0
        concat_str_alpha = ''

        for item in data:
            str_item = str(item)
            if str_item.isdigit():
                if int(str_item) % 2 == 0:
                    even_numbers.append(str_item)
                else:
                    odd_numbers.append(str_item)
                numbers_sum += int(str_item)
            elif str_item.isalpha():
                alphabets.append(str_item.upper())
                concat_str_alpha += str_item
            elif re.search(r'[^a-zA-Z0-9]', str_item):
                special_characters.append(str_item)

        concat_string = alternating_caps(concat_str_alpha)

        response = {
            "is_success": True,
            "user_id": get_user_id(full_name, dob),
            "email": email,
            "roll_number": roll_number,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(numbers_sum),
            "concat_string": concat_string
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

if __name__ == "__main__":
    app.run()
