# nama file p3.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 10

#netacad email cth: 'abcd@gmail.com'
email='atiakhairunican@gmail.com'
 
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini

# Graded
def caesar_encript(txt,shift):
    chiper = ""
    
    for char in txt:
        if char.isalpha():
            if char.islower():
                code = ord(char) + (shift%26)
                if code > ord("z"):
                    code -= 26
                if code < ord("a"):
                    code += 26
                chiper += chr(code)
            else:
                code = ord(char) + (shift%26)
                if code > ord("Z"):
                    code -= 26
                if code < ord("A"):
                    code += 26
                chiper += chr(code)
        else:
            chiper += char
            
    return chiper
    
# Fungsi Decript caesar
def caesar_decript(chiper,shift):
    return caesar_encript(chiper,-shift)


# Graded
# Fungsi mengacak urutan
def shuffle_order(txt,order):
    return ''.join([txt[i] for i in order])
 
# Fungsi untuk mengurutkan kembali sesuai order
def deshuffle_order(sftxt,order):
    txt = ''
    for i in sorted(order):
        txt += sftxt[order.index(i)]
    return txt


# Graded
# convert txt ke dalam bentuk list teks yang lebih pendek
# dan terenkrispi dengan urutan acak setiap batchnya
def send_batch(txt,batch_order,shift=3):
    txt = caesar_encript(txt,shift)
    sftxt = []
    
    if len(txt) % len(batch_order) == 0:
        for j in range(len(txt) // len(batch_order)):
            batch_txt = ''
            for i in range(len(txt)):
                if i // len(batch_order) == j:
                    batch_txt += txt[i]

            sf = shuffle_order(batch_txt,batch_order)
            sftxt.append(sf)
        
    else:
        txt += "_" * ((((len(txt) // len(batch_order))+1) * len(batch_order)) - len(txt))
        for j in range(len(txt) // len(batch_order)):
            batch_txt = ''
            for i in range(len(txt)):
                if i // len(batch_order) == j:
                    batch_txt += txt[i]

            sf = shuffle_order(batch_txt,batch_order)
            sftxt.append(sf)
            
    return sftxt
    
# batch_cpr: list keluaran send_batch
# fungsi ini akan mengembalikan lagi ke txt semula
def receive_batch(batch_cpr,batch_order,shift=3):
    batch_txt = [caesar_decript(deshuffle_order(i,batch_order),shift) for i in batch_cpr]
    return ''.join(batch_txt).strip('_')
