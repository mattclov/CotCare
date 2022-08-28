gender=input('Gender:')
dept=input('Dept:')
hospital=input("Hospital:")
if gender == 'm':
        gender = "Male Wing of"
        gcode = 100
if gender == 'f':
        gender = "Female Wing of"
        gcode = 200
if dept == 'normal':
        dept = "the Normal Rooms"
        dcode = 10
if dept == 'icu':
        dept = "the Intensive Care Unit"
        dcode = 20
if dept == "OT" :
        dept = "the operating theatre "
if hospital == "edward":
        hospital = "in Prince Edward hospital"
        hcode = 1
if hospital == "austin":
        hospital = "in Goveneor Austin hospital"
        hcode = 2

print("Bring patient to",gender,dept,hospital)
fcode=gcode+dcode+hcode
print("Bed number:",fcode)
