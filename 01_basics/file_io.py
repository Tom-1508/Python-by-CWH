s = "Tamal is a good boy. He will achieve everything which he is dreaming for."

'''
# Writing to a file 
# method 1 : ( using context manager)

with open("test.txt","w") as f:
    f.write(s)

# this is a general process :
fp = open("test.txt","w")
fp.write(s)
fp.close()

'''



'''

# Reading to a file 
# method 1 : ( using context manager)

# with open("test.txt", "r") as f:
#     s = f.read()
#     print(s)

# This is a general process :
# fp = open("test.txt", "r")
# s = fp.read()
# print(s)
# fp.close()

'''



'''

# Appending to a file 
# method 1 : ( using context manager)

# with open("test.txt","a") as f:
#     f.write("Tamal have a very kind heart. his main ideal is Honesty")

# this is a general process :
fp = open("test.txt","a")
fp.write("Tamal have a very kind heart. his main ideal is Honesty")
fp.close()

'''