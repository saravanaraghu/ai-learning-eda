def BMI(HEIGHT, WEIGHT):
    BMI_Value = 0
    HEIGHT = HEIGHT / 100
    BMI_Value = WEIGHT / (HEIGHT**2)
    return BMI_Value


Height = float(input("Enter Height in cms"))
Weight = float(input("Enter weight in Kgs"))
if (Height > 0 and Height <= 245) and (Weight > 0 and Weight < 200):
    BMI_Calculated = BMI(Height, Weight)
    print(BMI_Calculated)
    if BMI_Calculated < 16:
        print("Severe Thinness")
    elif 16 <= BMI_Calculated < 17:
        print("Moderate Thinness")
    elif 17 <= BMI_Calculated < 18.5:
        print("Mild Thinness")
    elif BMI_Calculated >= 18.5 and BMI_Calculated < 25:
        print("Normal")
    elif BMI_Calculated >= 25 and BMI_Calculated < 30:
        print("Overweight")
    elif BMI_Calculated >= 30 and BMI_Calculated < 35:
        print("Obese Class I")
    elif BMI_Calculated >= 35 and BMI_Calculated < 40:
        print("Obese Class II")
    else:
        print("Obese Class III")
else:
    if Height <= 0 or Height > 245:
        print("Enter Valid Height")
    elif Weight <= 0 or Weight > 200:
        print("Enter Valid Weight")
