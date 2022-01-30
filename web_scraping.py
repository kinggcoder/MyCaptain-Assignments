import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import web_scraper_db

parser=argparse.ArgumentParser()
parser.add_argument("--page_num_max",help="Enter the number of pages to be parsed",type=int)
parser.add_argument("--dbname",help="Enter the database name",type=str)
args=parser.parse_args()

web_url="https://www.oyorooms.com/hotels-in-bangalore/?page="
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.20 Safari/537.36"}

page_num_MAX=args.page_num_max
scraped_info_list=[]
web_scraper_db.connect(args.dbname)

for page_num in range(1,page_num_MAX):

#headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.20 Safari/537.36"}

    req=requests.get(web_url+str(page_num),headers=headers)

    content=req.content

    soup=BeautifulSoup(content,"html.parser")
    all_hotels=soup.find_all("div",{"class":"hotelCardListing"})



    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict["name"]=hotel.find("h3",{"class":"listingHotelDescription__hotelName"}).text
        hotel_dict["address"]=hotel.find("span",{"itemprop":"streetAddress"}).text
        hotel_dict["price"]=hotel.find("span",{"class":"listingPrice__finalPrice"}).text
        try:
            hotel_dict["rating"]=hotel.find("span",{"class":"hotelRating__ratingSummary"}).text
        except AttributeError:
            hotel_dict[rating]=None
        parent_amenities_element=hotel.find("div",{"class":"amenityWrapper"})
        amenities_list=[]
        for amenity in parent_amenities_element.find_all("div",{"class":"amenityWrapper__amenity"}):
            amenities_list.append(amenity.find("span",{"class":"d-body-sm"}).text.strip())

        hotel_dict["amenities"]=", ".join(amenities_list[:-1])
        scraped_info_list.append(hotel_dict)
        web_scraper_db.insert_into_table(args.dbname,tuple(hotel_dict.values()))

        # print(hotel_name,hotel_address,hotel_price,hotel_rating,amenities_list)
dataFrame=pandas.DataFrame(scraped_info_list)
print("updating the csv file!!!!!")
dataFrame.to_csv("Data.csv")
web_scraper_db.get_hotel_info(args.dbname)


"""code for database connectivity"""

import sqlite3

def connect(dbname):
    conn=sqlite3.connect("dbname")
    conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTELS(NAME TEXT,ADDRESS TEXT,PRICE INT,AMENITIES TEXT,RATING TEXT)")

    print("table created sucessfully!!!!")
    conn.close()

def insert_into_table(dbname,values):
    conn = sqlite3.connect(dbname)
    inserrt_sql="INSERT INTO OYO_HOTELS (NAME,ADDRESS,PRICE,AMEMITIES,RATING) VALUES(?,?,?,?,?)"
    conn.execute(insert_sql,values)
    conn.commit()
    conn.close()

def get_hotel_info(dbname):
    conn = sqlite3.connect(dbname)



    cur=conn.cursor()
    cur.execute("SELECT *FROM OYO_HOTELS")
    table_data=cur.fetchall()
    for record in table_data:
        print(record)
    conn.close()
