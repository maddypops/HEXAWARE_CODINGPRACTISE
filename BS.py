import file
from bs4 import BeautifulSoup4
xml_data= """
    <books>
        <book_id="i">
            <title>the Greate catalog</title>
            <author>Marithong</author>
"""
soup = BeautifulSoup(xml_data,"xml")

with open (r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\BS.xml",'w')as f:
    file.write(soup.prettify())
with open (r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\BS.xml",'r')as file:
    soup = BeautifulSoup(file,"xml")
    title = soup.title('author').text
    print(title)