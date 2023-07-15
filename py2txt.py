import time
import msvcrt
from selenium import webdriver
from selenium.webdriver.common.by import By


def messageCollector():
    driver = webdriver.Chrome()

    driver.get("https://web.whatsapp.com")
    time.sleep(5)
    confirm = int(input("Giriş başarılı işe 1'e basın, çıkış yapmak için 0'a basın : "))
    if confirm == 1:
        print("Whatsapp dinleniyor çıkmak isterseniz q ya basın...")
    elif confirm == 0:
        driver.close()
        exit()
    else:
        print("Sorry Please Try again")
        driver.close()
        exit()

    groupName = str(input("Grup adını giriniz: "))
    scopeSender = str(input("Kimin mesajlarını kaydetmek istiyorsunuz: "))

    group_chat = driver.find_element(By.XPATH, f"//span[@title='{groupName}']")
    group_chat.click()

    msg_blocks = driver.find_elements(
        By.XPATH,
        '//div[@class="_1BOF7 _2AOIt"]//div[@class="cm280p3y to2l77zo n1yiu2zv ft2m32mm oq31bsqd e1yunedv"]',
    )

    collected_msgs = []

    for block in msg_blocks:
        # Göndericiyi ve mesajı ayır
        block_text = block.text
        sender, msg = block_text.split("\n", 1)
        if sender == scopeSender:
            collected_msgs.append(msg)

    # Mesajları txt dosyasına kaydet
    with open("collected_msgs.txt", "w", encoding="utf-8") as f:
        for msg in collected_msgs:
            f.write(msg + "\n")

    collected_msgs_set = set(collected_msgs)

    while True:
        if msvcrt.kbhit():
            key_stroke = msvcrt.getch()
            if key_stroke == b"q":  # q ya basılırsa döngüyü kır
                print("Dinleme işlemi durduruldu..")
                break

        # Yeni mesaj bloklarını topla
        new_msg_blocks = driver.find_elements(
            By.XPATH,
            '//div[@class="_1BOF7 _2AOIt"]//div[@class="cm280p3y to2l77zo n1yiu2zv ft2m32mm oq31bsqd e1yunedv"]',
        )

        # Yeni mesajları bul
        new_msgs = []

        for block in new_msg_blocks[len(msg_blocks) :]:
            # Göndericiyi ve mesajı ayır
            block_text = block.text
            sender, msg = block_text.split("\n", 1)
            if sender == scopeSender:
                new_msgs.append(msg)

        # Yeni mesajları txt dosyasına ekle
        with open("collected_msgs.txt", "a", encoding="utf-8") as f:
            for msg in new_msgs:
                # Mesajın daha önce kaydedilip kaydedilmediğini kontrol et
                if msg not in collected_msgs_set:
                    f.write(msg + "\n")
                    collected_msgs_set.add(msg)
                    print("1 mesaj kaydedildi")

        # Mesaj bloklarını güncelle
        msg_blocks = new_msg_blocks

        time.sleep(5)

    # Tarayıcıyı kapatın
    driver.close()
