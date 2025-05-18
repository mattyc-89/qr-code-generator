import qrcode

def main():
    print("Generate a QR code for a website URL")
    url = input("Enter the website URL: ")    
    file_name = input("Enter the name of the file to save the QR code (don't add the extension): ")
    code = qrcode.make(url)
    code.save(f"{file_name}.png")  
    print(f"QR code saved as {file_name}.png")  

if __name__ == "__main__":
    main()