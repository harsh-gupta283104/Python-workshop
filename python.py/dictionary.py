# # my_dict={
# #     "University":"Gla University",
# #     "Location":"Mathura",
# #     "Year":2023
# # }
# # print(my_dict)

# # my_dict1={
# #     "University":"Gla University",
# #     "Location":"Mathura",
# #     "Year":2023
# # }
# # print(my_dict1["University"])

# # my_dict2={
# #     "University":"Gla University",
# #     "Location":"Mathura",
# #     "Year":2023
# # }
# # print(my_dict2)
# # print(len(my_dict2))
# # print(type(my_dict2))

# # thisdict={
# #     "University":"Gla University",
# #     "Location":"Mathura",
# #     "Year":2023,
# #     "color":["red","white","yellow"]
# # }
# # print(thisdict)

# # thisdict={
# #     "University":"Gla University",
# #     "Location":"Mathura",
# #     "Year":2023,
# #     "color":["red","white","yellow"]
# # }

# # check=thisdict["Year"]
# # print(check)

# # x=thisdict.get("Year")
# # print(x)

# # car={
# #     "brand":"Ford",
# #     "Model":"Musting",
# #     "Year":1964
# # }

# # x=car.keys()

# # print(x)

# # car["color"]="white"
# # print(car)
# # print(x)


# # This_dict={
# #     "Brand":"Ford",
# #     "Model":"Mustang",
# #     "Year":1964
# # }
# # x=This_dict.items()
# # print(This_dict)
# # print(x)

# # This_dict={
# #     "Brand":"Lemborgini",
# #     "Model":"Lemborgini",
# #     "Year":1939
# # }

# # for x in This_dict:
# #     print(x)

# # for x in This_dict:
# #     print(This_dict[x])
    
# # for x in This_dict.values():
# #     print(x)

# # for x in This_dict.keys():
# #     print(x)
# # This_dict.pop("Model")
# # print(This_dict)

# # This_dict.popitem()
# # print(This_dict)

# # Cube={num:num**3 for num in range(1,8)}
# # print(Cube)
# # del Cube[4]
# # print(Cube)
# # a=Cube.get(5)
# # print(a)

# # num={
# #     0:10,
# #     1:20
# # }
# # num[2]=30
# # print(num)
# # num2={
# #     3:40,
# #     4:50
# # }
# # num.update(num2)
# # print(num)

# # d={num:num*num for num in range(1,16)}
# # print(d)
# # d={
# #     "data1":100,
# #     "data2":-54,
# #     "data3":247
# # }
# # a=d.get.Sum("data1","data2","data3")
# # print(a)
# color_dict={'red': '#FF0000', 'green': '#008000', 'black': '#000000', 'white': 'FFFFFF'}
# color_dict1={}
# x=color_dict.keys()
# l_ist=[]
# for i in x:
#     l_ist.append(i)
# l_ist1=sorted(l_ist)
# for j in l_ist1:
#     color_dict1[j] = color_dict[j]
# print(color_dict1)
# print(type(color_dict1))
import turtle
import msvcrt


pen=turtle.Turtle()
 
def move(arrow):
    if arrow==b'1':
        pen.forward(1)
    elif arrow==b'2':
        pen.backward(1)
    elif arrow==b'3':
        pen.right(90)
    elif arrow==b'4':
        pen.left(90)
    elif arrow==b'5':
        pen.left(1)
        pen.forward(1)
    elif arrow==b'6':
        pen.right(1)
        pen.forward(1)
        
                                
 
   
while True:
    arrow = msvcrt.getch().lower()
    move(arrow)
    
    turtle.update()
