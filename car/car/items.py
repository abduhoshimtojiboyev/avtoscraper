from scrapy.item import Item, Field


class Car(Item):
    # define the fields for your item here like:
    brand = Field() # marka
    name = Field() # nomi
    price = Field() # narxi
    year = Field() # yili
    negotiable = Field() #kami_bor
    engine_size = Field() #dvigatel_hajmi
    fuel_type = Field() # yoqilgi_turi
    transmission_box = Field() #uzatish_qutisi
    distance_driven = Field()  # yurgani
    color = Field()  # rang
    color_condition = Field()  # rang holati
    gearbox_type = Field() # uzatma
    optics = Field()  # optika
    salon = Field()  # salon
    media = Field()  # media
    vehicle_option = Field()  # Avtomobil opsiyasi
    region = Field() #viloyat
    city = Field() #shahar
