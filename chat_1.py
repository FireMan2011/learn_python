# author: Kondratiuk Maksym, kondratiuk.11.maksim@gmail.com

# -----------------------------
# Чат бот на мінімалках
# -----------------------------

from datetime import date

print("Привіт!")
print("Мене звати Максим.")
print("А як тебе звати?")
name = input()
print("Привіт, " + name)
print("Приємно познайомитись!")
print("Скільки тобі років?")

years = int( input() )

print("В якому місяці ти народився (від 1 до 12)?")
month = int(input())
year_now = int(date.today().year)
current_month = int(date.today().month)

if(current_month >= month):
    old_year = year_now - years
else:
    old_year = year_now - years + 1

if(years % 2 == 0):
    old_year = str(old_year) + " (вінтажний дворянмн)"
else:
    old_year = str(old_year) + " (молоденжний аристорат)"

if(month == 1):
    printing_text = "О май гад, то ти народився аж у січні " + str((old_year))
elif(month == 2):
    printing_text = "О май гад, то ти народився аж у лютому " + str((old_year))
elif(month == 3):
    printing_text = "О май гад, то ти народився аж у березні " + str((old_year))
elif(month == 4):
    printing_text = "О май гад, то ти народився аж у квітні " + str((old_year))
elif(month == 5):
    printing_text = "О май гад, то ти народився аж у травні " + str((old_year))
elif(month == 6):
    printing_text = "О май гад, то ти народився аж у червні " + str((old_year))
elif(month == 7):
    printing_text = "О май гад, то ти народився аж у липні " + str((old_year))
elif(month == 8):
    printing_text = "О май гад, то ти народився аж у серпні " + str((old_year))
elif(month == 9):
    printing_text = "О май гад, то ти народився аж у вересні " + str((old_year))
elif(month == 10):
    printing_text = "О май гад, то ти народився аж у жовтні " + str((old_year))
elif(month == 11):
    printing_text = "О май гад, то ти народився аж у листопаді " + str((old_year))
else:
    printing_text = "О май гад, то ти народився аж у грудні " + str((old_year))
    
print(printing_text)
