def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal server Error"
        case _:
            return "Unknown Error"

print(http_status(490))