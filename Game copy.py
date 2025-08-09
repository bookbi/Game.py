#pseudo-code
import random 

#ตัวแปรที่ระบุสถานะของเกม

score = 0
lives = 3
words = ['great','cherprang','jaa']

def update_clue(guess, secret_word, clue):
    #guess ไล่ไปทีละตัวอักษรใน secret_word ดูว่าตัวไหนบ้างตรงกับที่ทาย
    for i in range(len(secret_word)):
        #ถ้าทายตรงตัวไหน ก็อัพเดต clue ตรงตำแหน่งนั้้น
        if guess == secret_word[i]:
            clue[i] = guess
    win = ''.join(clue) == secret_word
    return win #guess till end is True, if not yet they will be False

#ตราบใดที่ยังมีคำให้ทายอยู่ และชีวิตยังเหลือ ---> เล่นต่อไป
while (len(words) > 0)and (lives > 0):
    # สุ่มคำจาก words แล้วดึงคำนั้นออกจาก list
    random.shuffle(words)
    secret_word = words.pop()
    clue = list('?'*len(secret_word)) #จำนวนเท่ากับตัวอักษรของ secret_word

    #ตราบใดที่ยังทายคำนี้ยังไม่เสร็จหรือชีวิตยังไม่หมด
    while True :
        print(clue)
        print('ชีวิตที่เหลือ: '+ str(lives))
        guess = input('ทายตัวอักษรมาซิ: ')

        #check ว่าตัวอักษรที่ทาย อยู่ใน secret_word ป่าว?
        if guess in secret_word:
            win = update_clue(guess, secret_word, clue)
            if win:
                print('Yayyyy it is : '+secret_word)
                score = score+1
                print('Score: '+str(score))
                break #ทายคำนี้เสดแล้ว
            
        else: # ที่ guess มา ไม่อยู่ใน secret_word
            print('ผิด! เลือดลด')
            lives = lives - 1
            if lives == 0:
                print('เจ้าแพ้แล้ว! คำนั้นก็คือ :'+secret_word)
                break #end

print('Final Score: '+str(score))
print('Game end!')

