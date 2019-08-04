
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    10: "April"
}

print(monthConversions["Jan"])

print(monthConversions.get("Feb"))

print(monthConversions.get("LOl","Not Found"))
