
dictCar = {
    "brand": "Honda",
    "model": "Honda Civic",
    "year": 1972
}
print('\nGia tri ban dau:', dictCar)
dictCar['year'] = 1189
dictCar['Nationalist'] = 'Vietnam'
dictCar['Level']= 'C1'
print('\nTruy cap cac item cua dict: ',dictCar["year"])
print('\nTruy cap cac item cua dict(Cach 2): ',dictCar.get('ielts listening'))
print('\nThay doi gia tri item cua dict:', dictCar)
print('\nSetdafault: Tương tự get(), nhưng sẽ thiết lập dict[key]=default nếu key là không tồn tại trong dict')
print(dictCar.setdefault('year'))
print('\nvalues(): Trả về tất cả các value của một Dictionary')
print(dictCar.values())
print('\nDo dai cua dict la:', len(dictCar))
print("\nDuyet tung phan tu trong dict: ")
print()
for x in dictCar:
    print(x, ": ", dictCar.get(x))
