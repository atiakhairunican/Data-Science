# nama file p1.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded
# Isikan juga priority file

# untuk resubmisi, grader hanya akan mengambil priority yang paling besar
# jadi kalau anda ingin merevisi kode anda:
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0

priority = 10


#netacad email cth: 'abcd@gmail.com'
email='atiakhairunican@gmail.com'

# copy-paste semua #Graded cells di bawah ini

# PASTE KODE ANDA DISINI 
#Graded

# Manual, filter, list comprehension

#Graded

def letter_catalog(items,letter='A'):
    pass
    # MULAI KODEMU DI SINI
    item = []
    for i in items:
        if i[0] == letter:
            item.append(i)
    return item


#Graded

def counter_item(items):
    pass
    # MULAI KODEMU DI SINI
    key = []; value = []; lst = []
    for i in items:
        if i not in key and i not in value:
            counter = items.count(i)
            key.append(i)
            value.append(counter)
            
    for j in range(len(key)):
        a = (key[j], value[j])
        lst.append(a)
        
    lst = dict(sorted(lst))
    return lst


#Graded

def total_price(dcounter,fprice):
    pass
    # MULAI KODEMU DI SINI
    count = 0
    for key1 in fruit_price.keys():
        count1 = fruit_price[key1]
        for key2 in dcounter.keys():
            count2 = dcounter[key2]
            if key1 == key2:
                count += count1*count2
    return count

    
# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# MULAI KODEMU DI SINI
# fruit_price = None
fruit_price = []
for f in range(len(fruits)):
    fp = (fruits[f], prices[f])
    fruit_price.append(fp)
        
fruit_price = dict(fruit_price)


#Graded

def discounted_price(total,discount,minprice=100):
    pass
    # MULAI KODEMU DI SINI
    if discount > 0:
        if discount <= 100:
            if total >= minprice:
                priceDiscount = ((100 - discount) / 100) * total
            else:
                priceDiscount = total
        else:
            return 0
    else:
        return total

    return round(priceDiscount, 1)


#Graded

def counter_item(items):
    pass
    # MULAI KODEMU DI SINI
    key = []; value = []; lst = []
    for i in items:
        if i not in key and i not in value:
            counter = items.count(i)
            key.append(i)
            value.append(counter)
            
    for j in range(len(key)):
        a = (key[j], value[j])
        lst.append(a)
        
    lst = dict(sorted(lst))
    return lst

def total_price(dcounter,fprice):
    pass
    # MULAI KODEMU DI SINI
    count = 0
    for key1 in fruit_price.keys():
        count1 = fruit_price[key1]
        for key2 in dcounter.keys():
            count2 = dcounter[key2]
            if key1 == key2:
                count += count1*count2
    return count

    
# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# MULAI KODEMU DI SINI
# fruit_price = None
fruit_price = []
for f in range(len(fruits)):
    fp = (fruits[f], prices[f])
    fruit_price.append(fp)
        
fruit_price = dict(fruit_price)

def discounted_price(total,discount,minprice=100):
    pass
    # MULAI KODEMU DI SINI
    if discount > 0:
        if discount <= 100:
            if total >= minprice:
                priceDiscount = ((100 - discount) / 100) * total
            else:
                priceDiscount = total
        else:
            return 0
    else:
        return total

    return round(priceDiscount, 1)

def print_summary(items,fprice):
    pass
    # MULAI KODEMU DI SINI
    countS = 0
    for key1, value1 in counter_item(items).items():
        for key2, value2 in fprice.items():
            if key1 == key2:
                count = value1 * value2
                countS += count
                print(value1, key1, ":", count)
    
    print("total :", countS)
    
    print("discount price :", discounted_price(countS,10,minprice=100))