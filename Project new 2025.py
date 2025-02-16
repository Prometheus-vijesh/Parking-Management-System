
import mysql.connector 
import random 
import datetime 
 
def red(skk): print("\033[91m {}\033[00m".format(skk)) 
 
 
def green(skk): print("\033[92m {}\033[00m".format(skk)) 
 
 
def yellow(skk): print("\033[93m {}\033[00m".format(skk)) 
 
 
def light_purple(skk): print("\033[94m {}\033[00m".format(skk)) 
 
 
def purple(skk): print("\033[95m {}\033[00m".format(skk)) 
 
 
def cyan(skk): print("\033[96m {}\033[00m".format(skk)) 
 
 
def light_gray(skk): print("\033[97m {}\033[00m".format(skk)) 
 
 
def black(skk): print("\033[98m {}\033[00m".format(skk)) 
 
 
 
 
Bikes = 250 
Cars = 100 
bicycle = 50 
EV = 100 
keys= ["AWXFGH128", "SDVHRA555", "VGFYHH363", "JHNGHT767", "RFDNHY454", "AbcDeF123", "gHiJkL456", "mNoPqR789", 
       "sTuVwX123", "yZaBcD456"] 
values = [20, 40, 25, 15, 30, 15, 10, 25, 35, 5] 
 
host = 'localhost' 
user = 'root' 
password = '123456789' 
database = 'parking' 
mydb = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    password='123456789', 
    database = 'parking' 
) 
 
db_config = { 
        "host": host, 
        "user": user, 
        "password": password, 
        "database": database 
} 
 
 
 
 
def coupon(): 
    global keys 
    global values 
    index = random.randint(0, 9) 
    Code = keys[index] 
    discount = values[index] 
    purple(f"Your coupon is {Code} and your dicount for the coupon is Rs:{discount}/-") 
    return discount 
 
 
def create_table_and_update_costs(): 
    import mysql.connector 
    db_config = { 
        "host": host, 
        "user": user, 
        "password": password, 
        "database": database 
    } 
    connection = mysql.connector.connect(**db_config) 
    cursor = connection.cursor() 
 
 
    create_query = """ 
    CREATE TABLE vehicle_info ( 
        id INT AUTO_INCREMENT PRIMARY KEY, 
        car_cost INT, 
        bike_cost INT, 
        bicycle_cost INT, 
        ev_cost INT 
    ) 
    """ 
 
    update_query = "INSERT INTO vehicle_info (car_cost, bike_cost, bicycle_cost, ev_cost) VALUES (%s, %s, %s, %s)" 
    initial_values = (50, 20, 10, 100) 
 
    cursor.execute(create_query) 
    connection.commit() 
 
    print("Table 'vehicle_info' created successfully!") 
 
 
    cursor.execute(update_query, initial_values) 
    connection.commit() 
 
    print("Initial cost values inserted successfully!") 
 
    cursor.close() 
    connection.close() 
 
def Edit_cost(): 
    import mysql.connector 
    db_config = { 
        "host": host, 
        "user": user, 
        "password": password, 
        "database": database 
    } 
 
 
    while True: 
        print("Menu:") 
        print("1. Edit car cost") 
        print("2. Edit bike cost") 
        print("3. Edit bicycle cost") 
        print("4. Edit EV cost") 
        print("5. Exit") 
 
        choice = input("Enter your choice: ") 
 
        if choice == "1": 
            new_car_cost = int(input("Enter the new car cost: ")) 
            connection = mysql.connector.connect(**db_config) 
            cursor = connection.cursor() 
 
            query = "UPDATE vehicle_info SET car_cost = %s" 
            values = (new_car_cost,) 
 
            cursor.execute(query, values) 
            connection.commit() 
 
            print("Car cost updated successfully!") 
 
            cursor.close() 
            connection.close() 
        elif choice == "2": 
            new_bike_cost = int(input("Enter the new bike cost: ")) 
            connection = mysql.connector.connect(**db_config) 
            cursor = connection.cursor() 
 
 
            query = "UPDATE vehicle_info SET bike_cost = %s" 
            values = (new_bike_cost,) 
 
            cursor.execute(query, values) 
            connection.commit() 
 
            print("Bike cost updated successfully!") 
 
            cursor.close() 
            connection.close() 
        elif choice == "3": 
            new_bicycle_cost = int(input("Enter the new bicycle cost: ")) 
            connection = mysql.connector.connect(**db_config) 
            cursor = connection.cursor() 
 
 
            query = "UPDATE vehicle_info SET bicycle_cost = %s" 
            values = (new_bicycle_cost,) 
 
            cursor.execute(query, values) 
            connection.commit() 
 
            print("Bicycle cost updated successfully!") 
 
            cursor.close() 
            connection.close() 
        elif choice == "4": 
            new_ev_cost = int(input("Enter the new EV cost: ")) 
            connection = mysql.connector.connect(**db_config) 
            cursor = connection.cursor() 
 
 
            query = "UPDATE vehicle_info SET ev_cost = %s" 
            values = (new_ev_cost,) 
 
            cursor.execute(query, values) 
            connection.commit() 
 
            print("EV cost updated successfully!") 
 
            cursor.close() 
            connection.close() 
        elif choice == "5": 
            print("Exiting...") 
            break 
        else: 
            print("Invalid choice. Please select a valid option from the menu.") 
 
 
def Count_parked_vehicles(): 
    Parked_Vehicles = Bikes + Cars + bicycle + EV 
    Spots = 500 - Parked_Vehicles 
    purple(Spots) 
 
 
def Remaining_spots(): 
    Parked_Vehicles = Bikes + Cars + bicycle + EV 
    cyan(Parked_Vehicles) 
 
 
def revenue_report(): 
    import mysql.connector 
    db_config = { 
        "host": host, 
        "user": user, 
        "password": password, 
        "database": database 
    } 
    connection = mysql.connector.connect(**db_config) 
    cursor = connection.cursor() 
    query = "SELECT SUM(revenue) FROM v_info" 
    cursor.execute(query) 
    total_revenue = cursor.fetchone()[0] 
    cursor.close() 
    connection.close() 
    green("Total Revenue:", total_revenue) 
 
 
def most_popular_vehicle(): 
    l = [] 
    avg_bikes = ((250-Bikes)/250)*100 
    avg_cars = ((100-Cars)/100)*100 
    avg_bicycle = ((50 - bicycle) / 50) * 100 
    avg_ev = ((100 - EV) / 100) * 100 
    l.append(avg_cars) 
    l.append(avg_ev) 
    l.append(avg_bikes) 
    l.append(avg_bicycle) 
    max_index = l.index(max(l)) 
    if max_index == 0: 
        light_purple("most popular vehicle parked is CAR") 
    elif max_index == 1: 
        light_purple("most popular vehicle parked is EV") 
    elif max_index == 2: 
        light_purple("most popular vehicle parked is BIKES") 
    elif max_index == 3: 
        light_purple("most popular vehicle parked is BICYCLE") 
 
def edit_table(): 
    import mysql.connector 
 
 
    db_config = { 
        "host": host, 
        "user": user, 
        "password": password, 
        "database": database 
    } 
 
    def add_new_attribute(): 
        connection = mysql.connector.connect(**db_config) 
        cursor = connection.cursor() 
 
        new_attribute_name = input("Enter the name of the new attribute: ") 
        new_attribute_data_type = input("Enter the data type of the new attribute: ") 
 
 
        query = f"ALTER TABLE v_info ADD {new_attribute_name} {new_attribute_data_type}" 
 
        cursor.execute(query) 
        connection.commit() 
 
        print(f"New attribute '{new_attribute_name}' added successfully!") 
 
        cursor.close() 
        connection.close() 
 
    def remove_attribute(): 
        connection = mysql.connector.connect(**db_config) 
        cursor = connection.cursor() 
 
        attribute_to_remove = input("Enter the name of the attribute to remove: ") 
 
 
        query = f"ALTER TABLE v_info DROP COLUMN {attribute_to_remove}" 
 
        cursor.execute(query) 
        connection.commit() 
 
        print(f"Attribute '{attribute_to_remove}' removed successfully!") 
 
        cursor.close() 
        connection.close() 
 
    while True: 
        print("Menu:") 
        print("1. Add a new attribute") 
        print("2. Remove an attribute") 
        print("3. Exit") 
 
        choice = input("Enter your choice: ") 
 
        if choice == "1": 
            add_new_attribute() 
        elif choice == "2": 
            remove_attribute() 
        elif choice == "3": 
            print("Exited successfully") 
            break 
        else: 
            print("Invalid choice. Please select a valid option from the menu.") 
 
 
 
 
 
def edit_attribute(plate_number): 
    import mysql.connector 
    db_config = { 
        "host": host, 
        "user": user, 
        "password": password, 
        "database": database 
    } 
    connection = mysql.connector.connect(**db_config) 
    cursor = connection.cursor() 
 
    attribute_to_edit = input("Enter the name of the attribute to edit: ") 
    new_value = input(f"Enter the new value for '{attribute_to_edit}': ") 
 
 
    query = f"UPDATE v_info SET {attribute_to_edit} = %s WHERE plate_number = %s" 
    values = (new_value, plate_number) 
 
    cursor.execute(query, values) 
    connection.commit() 
 
    print(f"Attribute '{attribute_to_edit}' updated successfully!") 
 
    cursor.close() 
    connection.close() 
 
 
    while True: 
        print("Menu:") 
        print("1. Edit attributes") 
        print("2. Exit") 
 
        choice = input("Enter your choice: ") 
 
        if choice == "1": 
            plate_number = input("Enter the plate number for the vehicle: ") 
            edit_attribute(plate_number) 
        elif choice == "2": 
            print("Exiting...") 
            break 
        else: 
            print("Invalid choice. Please select a valid option from the menu.") 
 
 
def disp(): 
    import mysql.connector 
    db_config = { 
        "host": host, 
        "user": user, 
        "password": password, 
        "database": database 
    } 
    connection = mysql.connector.connect(**db_config) 
    cur = connection.cursor() 
    query="select * from v_info" 
    x=cur.execute(query) 
    a = cur.fetchall() 
    light_purple(a) 
    connection.close() 
 
def edit_cost(): 
    cyan(''' 
    which cost do you want to edit: 
    1.Cars 
    2.Bikes 
    3.bicycle 
    4.EV 
    ''') 
    o = int(input(">")) 
    if o == 1 : 
        R = int(input("Enter new cost for cars:")) 
        cost_Cars = R 
    elif o == 2 : 
        R = int(input("Enter new cost for bikes:")) 
        cost_Bikes = R 
    elif o == 3 : 
        R = int(input("Enter new cost for bicycle:")) 
        cost_bicycle = R 
    elif o == 4 : 
        R = int(input("Enter new cost for Ev:")) 
        cost_EV = R 
Plate_present = True 
def add_vehicle_info(): 
    global Cars 
    global Bikes 
    global bicycle 
    global EV 
    mydb = mysql.connector.connect( 
        host="localhost", 
        user="root", 
        password="123456789", 
        database="parking" 
    ) 
    o = True 
    p = True 
    typee = True 
    while typee: 
 
        vehicle_type = input("Enter vechicle type car/bike/bicycle/Ev: ") 
        if vehicle_type.lower() == "car": 
            while True: 
                if Cars > 0: 
                    Cars -= 1 
                    typee = False 
                    continue 
                else: 
                    red("oops the spots for your vehicles are full!!") 
                    red("You cant park here for now...") 
                    Plate_present =False 
                    o = False 
                    p = False 
                    break 
 
        elif vehicle_type.lower() == "bike": 
            while True: 
                if Bikes > 0 : 
                    Bikes -= 1 
                    typee = False 
                    continue 
                else: 
                    red("oops the spots for your vehicles are full!!") 
                    red("You cant park here for now...") 
                    Plate_present = False 
                    o = False 
                    p = False 
                    break 
 
        elif vehicle_type.lower() == "bicycle": 
            while True: 
                if bicycle > 0: 
                    bicycle -= 1 
                    typee = False 
                    continue 
                else: 
                    red("oops the spots for your vehicles are full!!") 
                    red("You cant park here for now...") 
                    Plate_present = False 
                    o = False 
                    p = False 
                    break 
        elif vehicle_type.lower() == "ev": 
             while True: 
                if EV>0: 
                    EV -= 1 
                    typee = False 
                    continue 
                else: 
                    red("oops the spots for your vehicles are full!!") 
                    red("You cant park here for now...") 
                    Plate_present = False 
                    o = False 
                    p = False 
                    break 
        else: 
            red("Enter the proper vehicle type: ") 
            typee = True 
 
 
        while o: 
            otp = input("Enter a 4 digit numerical password: ") 
            if len(otp) == 4: 
                break 
            else: 
                red("Enter only 4 digits") 
                continue 
 
        while o: 
            plate_number = input("enter plate number:") 
            if len(plate_number) == 10: 
                break 
            else: 
                red("Enter proper plate Number") 
                continue 
 
        vehicle_type = input("enter vehicle type:") 
        vehicle_name = input("enter vehicle name:") 
        owner_name = input("enter owner name:") 
        in_time = datetime.datetime.now().time() 
        pa = True 
        while pa: 
            parking_type = input("enter parking type (vip / normal)? :") 
            if parking_type.lower() == 'vip' or parking_type.lower() == 'normal': 
                break 
            else: 
                red("Enter proper parking type") 
                continue 
 
    cursor = mydb.cursor() 
    query = "INSERT INTO v_info (plate_number, vehicle_type, vehicle_name, owner_name, otp, parking_type, in_time) VALUES (%s, %s, %s, %s, %s, %s, %s)" 
    values = (plate_number, vehicle_type, vehicle_name, owner_name, otp, parking_type, in_time) 
    cursor.execute(query, values) 
    mydb.commit() 
    green("Vehicle information added successfully!") 
 
 
import mysql.connector 
db_config = { 
        "host": host, 
        "user": user, 
        "password": password, 
        "database": database 
} 
 
def check_primary_key_presence(v_info, plate_number, value): 
    global Plate_present 
    connection = mysql.connector.connect(**db_config) 
    cursor = connection.cursor() 
 
    query = f"SELECT * FROM {v_info} WHERE {plate_number} = %s" 
    values = (value,) 
 
    cursor.execute(query, values) 
    result = cursor.fetchone() 
    print(result[0][0]) 
    cursor.close() 
    connection.close() 
 
    if result: 
        Plate_present = True 
    else: 
        Plate_present = False 
Plate_present = True 
def Reserve_vehicle(): 
    global Cars 
    global Bikes 
    global bicycle 
    global EV 
    mydb = mysql.connector.connect( 
        host="localhost", 
        user="root", 
        password="123456789", 
        database="parking" 
    ) 
    o = True 
    p = True 
    typee = True 
    while typee: 
 
        vehicle_type = input("Enter vechicle type car/bike/bicycle/Ev: ") 
        if vehicle_type.lower() == "car": 
            while True: 
                if Cars > 0: 
                    Cars -= 1 
                    typee = False 
                    continue 
                else: 
                    red("oops the spots for your vehicles are full!!") 
                    red("You cant park here for now...") 
                    Plate_present = False 
                    o = False 
                    p = False 
                    break 
 
        elif vehicle_type.lower() == "bike": 
            while True: 
                if Bikes > 0: 
                    Bikes -= 1 
                    typee = False 
                    continue 
                else: 
                    red("oops the spots for your vehicles are full!!") 
                    red("You cant park here for now...") 
                    Plate_present = False 
                    o = False 
                    p = False 
                    break 
 
        elif vehicle_type.lower() == "bicycle": 
            while True: 
                if bicycle > 0: 
                    bicycle -= 1 
                    typee = False 
                    continue 
                else: 
                    red("oops the spots for your vehicles are full!!") 
                    red("You cant park here for now...") 
                    Plate_present = False 
                    o = False 
                    p = False 
                    break 
        elif vehicle_type.lower() == "ev": 
            while True: 
                if EV > 0: 
                    EV -= 1 
                    typee = False 
                    continue 
                else: 
                    red("oops the spots for your vehicles are full!!") 
                    red("You cant park here for now...") 
                    Plate_present = False 
                    o = False 
                    p = False 
                    break 
        else: 
            red("Enter the proper vehicle type: ") 
            typee = True 
 
        while o: 
            otp = input("Enter a 4 digit numerical password: ") 
            if len(otp) == 4: 
                break 
            else: 
                red("Enter only 4 digits") 
                continue 
 
        while o: 
            plate_number = input("enter plate number:") 
            if len(plate_number) == 10: 
                break 
            else: 
                red("Enter proper plate Number") 
                continue 
 
        vehicle_type = input("enter vehicle type:") 
        vehicle_name = input("enter vehicle name:") 
        owner_name = input("enter owner name:") 
        in_time = datetime.datetime.now().time() 
        pa = True 
        while pa: 
            parking_type = input("enter parking type (vip / normal)? :") 
            if parking_type.lower() == 'vip' or parking_type.lower() == 'normal': 
                break 
            else: 
                red("Enter proper parking type") 
                continue 
 
    cursor = mydb.cursor() 
    query = "INSERT INTO v_info (plate_number, vehicle_type, vehicle_name, owner_name, otp, parking_type, in_time) VALUES (%s, %s, %s, %s, %s, %s, %s)" 
    values = (plate_number, vehicle_type, vehicle_name, owner_name, otp, parking_type, in_time) 
    cursor.execute(query, values) 
    mydb.commit() 
    green("Vehicle information added successfully!") 
 
 
import mysql.connector 
 
db_config = { 
    "host": host, 
    "user": user, 
    "password": password, 
    "database": database 
} 
 
 
def check_primary_key_presence(v_info, plate_number, value): 
    global Plate_present 
    connection = mysql.connector.connect(**db_config) 
    cursor = connection.cursor() 
 
    query = f"SELECT * FROM {v_info} WHERE {plate_number} = %s" 
    values = (value,) 
 
    cursor.execute(query, values) 
    result = cursor.fetchone() 
    print(result[0][0]) 
    cursor.close() 
    connection.close() 
 
    if result: 
        Plate_present = True 
    else: 
        Plate_present = False 
 
 
def in_current_time(Plate): 
    connection = mysql.connector.connect(**db_config) 
    cursor = connection.cursor() 
 
    query = (f"select in_time from v_info where plate_number = {Plate}") 
    cursor.execute(query) 
    intime = cursor.fetchall() 
    outtime = datetime.datetime.now().time() 
    query2 = (f"insert into v_info(out_time) values({outtime}) where plate_number = {Plate} ") 
    cursor.execute(query2) 
    query3 = (f"select out_time from v_info where plate_number = {Plate}") 
    cursor.execute(query3) 
    O_T = cursor.fetchall() 
    Time_difference = O_T - intime 
    print(Time_difference) 
'''in_current_time('1234567890')''' 
 
def del_veh(): 
    db_config = { 
        "host": host, 
        "user": user, 
        "password": password, 
        "database": 'parking' 
    } 
    connection = mysql.connector.connect(**db_config) 
    cur = connection.cursor() 
    while True: 
        Plate = input("Enter your vehicle number:") 
        check_primary_key_presence('v_info', 'plate_number',Plate) 
        if Plate_present == False: 
            red("Plate number not present!!") 
            red("Enter proper plate number") 
            continue 
        else: 
            green("PLate present") 
            break 
        query1 = (f"select otp from v_info where plate_number = {Plate}") 
        cur.execute(query1) 
        otp = cursor.fetchall() 
        while True: 
            Password = int(input("enter the password that you eneterd while parking the vehicle: ")) 
            if Password == otp: 
                break 
            else: 
                red("the password you have entered is wrong !!") 
                red("Enter the correct password") 
                continue 
 
 
        query2 = (f"delete from v_info wheredriver" 
                f" plate_number={Plate}") 
        x = cur.execute(query2) 
        connection.commit() 
        connection.close() 
        green("Successfully removed") 
 
 
 
 
cursor = mydb.cursor() 
'''cursor.execute("create database Parking ")''' 
'''cursor.execute("CREATE TABLE V_info (" 
               "plate_number INT PRIMARY KEY," 
               "vehicle_type VARCHAR(10)," 
               "vehicle_name VARCHAR(30)," 
                
              "owner_name VARCHAR(15)," 
               "date DATE," 
               "otp INT," 
               "parking_type VARCHAR(5)," 
               "in_time TIME);")''' 
mydb.close() 
User_Who = True 
while User_Who: 
# Display - main menu 
    cyan("Who is using the program - ADMIN/DRIVER") 
    User = input(">") 
    if User.lower() == 'admin': 
        Admin_status = True 
        while Admin_status: 
            Admin_name = input("Enter user name: " ) 
            Admin_password = input("Enter the password: " ) 
            if Admin_name == 'lucifer' and Admin_password == '666': 
                Admin_status = False 
                print(''' 
                1. View number of vehicles parked 
                2. View number of vehicles spots remaining  
               3. View revenue report 
                4. View most popular vehicle type parked 
                5. Edit table - attributes 
                6. Edit vehicle information 
                7. Display all vehicle info 
                8. Edit costs of parking 
                9. Exit''') 
 
 
                choice_status = True 
                while choice_status: 
                    choice = int(input("Enter your choice (1-9): ")) 
                    if choice < 1 or choice > 9: 
                        red("Enter the correct option") 
                        continue 
                    else: 
                        break 
 
            elif Admin_name == 'lucifer' and Admin_password != '666': 
                red("Enter the correct login details") 
                continue 
            elif Admin_name != 'lucifer' and Admin_password == '666': 
                red("Enter the correct login details") 
                continue 
            elif  Admin_name != 'lucifer' and Admin_password != '666': 
                red("Enter the correct login details") 
                continue 
            else: 
                print("Enter the correct login details") 
                continue 
 
        if choice == 1: 
            Count_parked_vehicles() 
 
        if choice == 2: 
            Remaining_spots() 
        if choice == 3: 
            revenue_report() 
        if choice == 4: 
            most_popular_vehicle() 
        if choice == 5: 
            edit_table() 
        if choice == 6: 
            plate_number=input("enter the vechile plate number:") 
            edit_attribute(plate_number) 
        if choice == 7: 
            disp() 
        if choice == 8: 
            Edit_cost() 
        if choice == 9: 
            green("Exited successfully") 
            break 
 
 
 
    elif User.lower() == 'driver': 
        print(''' 
                    1. Add Vehicle 
                    2. Reserve spot 
                    3. Parking status 
                    4. Cancel Parking Reservation 
                    5. Remove vehicle 
                    6. Coupon- Discounts 
                    7. Exit 
                     
                   ''') 
        choice_status = True 
        while choice_status: 
            choice = int(input("Enter your choice (1-7): ")) 
            if choice < 1 or choice > 7: 
                red("Enter the correct option") 
                continue 
            else: 
                break 
        if choice == 1: 
            add_vehicle_info() 
        if choice == 2: 
            add_vehicle_info() 
            print("spot reserved successfully!!") 
        if choice == 3: 
            Remaining_spots() 
        if choice == 4: 
            del_veh() 
        if choice == 5: 
            del_veh() 
        if choice == 6: 
            coupon() 
        if choice == 7: 
            cyan("thanks for using our service... :) ") 
            break 
 
    else: 
        red("Invalid user type") 
 
 
 
 
 
