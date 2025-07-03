#pseudo-code

#ตัวแปรที่ระบุสถานะของเกม

score = 0
lives = 3
word = ['great','cherprang','jaa']

#ตราบใดที่ยังมีคำให้ทายอยู่ และชีวิตยังเหลือ ---> เล่นต่อไป
while (ยังมีคำให้ทาย)and (และชีวิตยังเหลือ)
    # สุ่มคำจาก words แล้วดึงคำนั้นออกจาก list
    secret_word = คำที่สุ่ม
    clue = ['?','?',...] จำนวนเท่ากับตัวอักษรของ secret_word

    #ตราบใดที่ยังทายคำนี้ยังไม่เสร็จหรือชีวิตยังไม่หมด
    while ยังทายไม่เสร็จ:
        print(clue)
        print('ชีวิตที่เหลือ: '+ lives)
        guess = input('ทายตัวอักษรมาซิ: ')

        #check ว่าตัวอักษรที่ทาย อยู่ใน secret_word ป่าว?
        if guess in secret_word:
            win = update_clue(guess, secret_word)
            if win:
                print('Yayyyy it is :'+secret_word)
                score = score+1
                print('Score: '+score)
        else: # ที่ guess มา ไม่อยู่ใน secret_word
            print('ผิด! เลือดลด')
            lives = lives - 1
            if lives == 0:
                print('เจ้าแพ้แล้ว! คำนั้นก็คือ :'+secret_word)
                break

print('Final Score: '+score)
print('Game end!')
