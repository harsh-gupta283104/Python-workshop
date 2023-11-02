text="Python Programing"
text1="My university name is : GLA Uninversity"

trimed_text=text.strip()
print(trimed_text)

lower_case= text.lower()
upper_case=text.upper()
print("Lowercse:", lower_case)
print("Uppercase:",upper_case)



replaced_text=text.replace("Programing","Coding")
print(replaced_text)

index=text1.find("GLA")
print("Index for 'GLA': ", index)