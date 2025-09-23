#  and
# or
# not

high_income=True
good_credit =True
student =False
if high_income and good_credit:
    print("eligible")
else:
    print("non eligible")

if high_income or student:
    print("eligible")
else:
    print("non eligible")

if not student:
    print("eligible")
else:
    print("not eligible")

# combination of all
if (high_income or  good_credit) and not student:
    print("eligible")
else:
    print("not eligible")