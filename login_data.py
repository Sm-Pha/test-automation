# Dictionaries
valid_email = "@gmail.com" 
valid_password = ""
invalid_email = "14ngbx" + "@gmail.com"
invalid_password = "IF1mtr@R"


test_data = [
    {
        "username": "14ngbx" + "@gmail.com",
        "password": "IF1mtr@R",
        "expected_result": "fail",
    },
    # {
    #     "username": "14ngb" + "@gmail.com",
    #     "password": valid_password,
    #     "expected_result": "fail",
    # },
    # {
    #     "username": valid_email,
    #     "password": "IF1mtr@",
    #     "expected_result": "fail",
    # },
    # {
    #     "username": valid_email,
    #     "password": invalid_password,
    #     "expected_result": "fail",
    # },
    # {
    #     "username": invalid_email,
    #     "password": valid_password,
    #     "expected_result": "fail",
    # },
    # {
    #     "username": invalid_email,
    #     "password": invalid_password,
    #     "expected_result": "fail",
    # },
    # {
    #     "username": valid_email,
    #     "password": valid_password,
    #     "expected_result": "pass",
    # },
]

