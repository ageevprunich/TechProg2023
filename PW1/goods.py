from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque() #Проводиться ініціалізація черги

    def add_item(self, item):
        if isinstance(item, str):
            self.queue.append(item) #Якщо передані користувачем данні це строка, тоді вона додається в чергу, інакше 
            #додавання не проводиться
            return True
        return False
    
    def pop(self):
        if self.queue:
            self.queue.popleft()#Видалення елемента черги

    def view_list(self):
        return list(self.queue)#Вивід черги на екран як список
    
order = Queue() #Ініціалзуємо екземпляр класу Queue
i=0
while(i != 4): #Поки не буде введена команда 4, буде виводитися меню програми
    print("1.Add item to the queue.\n2.Delete item from queue. \n3.View list. \n4.Exit")
    i = int(input())
    match i :
        case 1: #Команда 1. Очікуємо назву замовлення від користувача і за допомогою відповідної функції додаємо до черги
            print("Enter your order")
            if(order.add_item(input()) == True): #Якщо функція повертає True, значить замовлення додано успішно
                print("Your order was added")
            else: # Інакше виводимо повідомлення що щось пішло не так
                print("Something went wrong")
        case 2: #Команда 2. Видаляємо елемент черги за допомогою відповідної функції
            order.pop()
            print("Order was deleted!")
        case 3: #команда 3. Виводимо список черги
            print(order.view_list())


