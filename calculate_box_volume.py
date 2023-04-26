# calculate box volume
# by: Kimberly Allison

def main():
    print("Enter the length, width, and height of a box to calculate it's volume")
    
    # get info
    length = int(input("Box length: "))
    width = int(input("Box width: "))
    height = int(input("Box height: "))
    
    # calculate the volume
    volume = length * width * height
    
    # print the results
    print("Volume:", volume)
    
  
main()    
