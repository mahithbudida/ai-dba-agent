def check_blocking(database_name: str, time_window_hours:int):
    print(f"Checking blocking in {database_name} fro last {time_window_hours} hours..")
    return{"status":"success", "blocking_found": True}

def generate_report(format: str):
    print(f"Generating report in {format} format..")
    return{"status":"success","file":"blocking_report.pdf"}

def general_response():
    print("General reponse triggered.")
    return{"status":"success"}

