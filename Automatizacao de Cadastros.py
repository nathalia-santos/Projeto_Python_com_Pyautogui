#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pyautogui.moveTo(603, 758)
pyautogui.click()
pyautogui.moveTo(718, 648)
pyautogui.click()
pyautogui.moveTo(321, 542) #cadastro de produtos
pyautogui.click()
sleep(5)
pyautogui.moveTo(417, 149) #iniciar cadastro
pyautogui.click()
sleep(5)

for rowIndex, row in df.iterrows():
    pyperclip.copy(row['CÓDIGO'])
    pyautogui.moveTo(246, 187) #campo de código
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'v')
    pyperclip.copy(row['DESCRIÇÃO'])
    pyautogui.moveTo(414, 190) #campo de descrição
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'v')
    pyperclip.copy(row['APLICAÇÃO'])
    pyautogui.moveTo(532, 229) #campo de aplicação
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.moveTo(994, 229) #tipo de produto
    pyautogui.click()
    pyautogui.rightClick()
    pyautogui.moveTo(1023, 338) #selecionar tudo
    pyautogui.click()
    pyautogui.press('Delete')
    pyautogui.moveTo(994, 229)
    pyautogui.click()
    pyautogui.write('p') #para selecionar produto
    pyautogui.press('enter')
    pyautogui.moveTo(913, 296)
    pyautogui.click()
    pyautogui.press('enter')
    pyautogui.moveTo(1100, 230) #unidade
    pyautogui.click()
    pyautogui.rightClick()
    pyautogui.moveTo(1129, 338)
    pyautogui.click()
    pyautogui.press('Delete')
    pyautogui.moveTo(1100, 230)
    pyautogui.click()
    pyautogui.press('k') #para colocar em kg
    pyautogui.press('enter')
    pyautogui.moveTo(444, 357) #aba de tributação
    pyautogui.click()
    pyperclip.copy(row['NCM'])
    pyautogui.moveTo(240, 403) #NCM
    pyautogui.click()
    pyautogui.write(row['NCM'])
    pyautogui.press('enter')
    pyautogui.moveTo(230, 521) #peso
    pyautogui.click()
    pyautogui.press('1')
    pyautogui.moveTo(441, 650)#origem
    pyautogui.click()
    pyautogui.press('0')
    pyautogui.press('enter')
    pyautogui.moveTo(263, 121) #salva cadastro
    pyautogui.click()
    pyautogui.moveTo(976, 219) #fechar janela de aviso
    pyautogui.click()
    pyautogui.moveTo(202, 124) #novo cadastro
    pyautogui.click()
print('Código efetuado com sucesso!')

