import os

if os.path.isfile("Financial Log Parse Engine\Data.csv") == True:
    s=os.path.getsize("Financial Log Parse Engine\Data.csv")
    print(s)
    if os.path.isdir("Financial Log Parse Engine/Processed_Financial_Reports folder") ==True:
        print("Folder already exist")
    else:    
        os.mkdir("Financial Log Parse Engine/Processed_Financial_Reports folder")
else:
    print("File does not exist")