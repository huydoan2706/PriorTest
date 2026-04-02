import Citizen
import Driving_License
import Driving_Citizen
import Province

if __name__ == "__main__":
    provinces = []
    provinces.append(Province.Province(1, "Ha Noi"))
    provinces.append(Province.Province(2, "Ho Chi Minh City"))
    provinces.append(Province.Province(3, "Da Nang"))
    provinces.append(Province.Province(4, "Hai Phong"))
    provinces.append(Province.Province(5, "Hue"))
    provinces.append(Province.Province(6, "Can Tho"))
    provinces.append(Province.Province(7, "Tuyen Quang"))
    provinces.append(Province.Province(8, "Thai Nguyen"))
    provinces.append(Province.Province(9, "Cao Bang"))
    provinces.append(Province.Province(10, "Lang Son"))
    provinces.append(Province.Province(11, "Ninh Binh"))
    provinces.append(Province.Province(12, "Quang Ninh"))
    provinces.append(Province.Province(13, "Bac Ninh"))
    provinces.append(Province.Province(14, "Hung Yen"))
    provinces.append(Province.Province(15, "Phu Tho"))
    provinces.append(Province.Province(16, "Son La"))
    provinces.append(Province.Province(17, "Dien Bien"))
    provinces.append(Province.Province(18, "Lai Chau"))
    provinces.append(Province.Province(19, "Lao Cai"))
    provinces.append(Province.Province(20, "Thanh Hoa"))
    provinces.append(Province.Province(21, "Nghe An"))
    provinces.append(Province.Province(22, "Ha Tinh"))
    provinces.append(Province.Province(23, "Quang Tri"))
    provinces.append(Province.Province(24, "Quang Ngai"))
    provinces.append(Province.Province(25, "Gia Lai"))
    provinces.append(Province.Province(26, "Dak Lak"))
    provinces.append(Province.Province(27, "Khanh Hoa"))
    provinces.append(Province.Province(28, "Lam Dong"))
    provinces.append(Province.Province(29, "Dong Nai"))
    provinces.append(Province.Province(30, "Tay Ninh"))
    provinces.append(Province.Province(31, "An Giang"))
    provinces.append(Province.Province(32, "Dong Thap"))
    provinces.append(Province.Province(33, "Vinh Long"))
    provinces.append(Province.Province(34, "Ca Mau"))

    citizen_1 = Citizen.Citizen('001200345678',
                                'Nguyen',
                                'Van',
                                'A',
                                provinces[2],
                                provinces[6])

    citizen_2 = Driving_Citizen.Driving_Citizen('002088006644',
                                'Nguyen',
                                'Thi',
                                'B',
                                provinces[23],
                                provinces[31],
                                '987654321',
                                ['A', 'B'])

    print(citizen_2.get_full_name())
    print(citizen_1.get_hometown_name())
    print(citizen_1.get_living_area_id())
    print(citizen_1.get_hometown_id())
    print(citizen_2.get_living_area_name())
    print(citizen_2.vehicle_type())
